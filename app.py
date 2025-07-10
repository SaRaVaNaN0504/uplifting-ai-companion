# app.py (UPGRADED - With Dynamic Empathy Generation)

import os
import random
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# --- Configuration ---


VECTOR_DB_PATH = "./chroma_db_final"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# --- PART 1: Initialize Models and Bot Brain ---
app = FastAPI(title="Dynamic Empathy Wellness Chatbot")

# A. Initialize the LLM (we will use this for both RAG and Empathy)
try:
    print("Initializing LLM...")
    llm = ChatGroq(temperature=0.3, model_name="llama3-70b-8192") # Slightly higher temp for more creative empathy
except Exception as e:
    print(f"FATAL ERROR: Could not initialize LLM. Check API Key. Error: {e}")
    llm = None

# B. Initialize the RAG system for advice
try:
    print("Initializing RAG system...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vector_db = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)
    rag_chain_prompt_template = """
    You are a caring and empathetic wellness chatbot. The user is asking for advice on a specific topic. Use the following context to provide a helpful, actionable, and encouraging answer. Speak like a kind, wise friend.
    Context: {context}
    User's Question: {question}
    Your Answer:
    """
    RAG_PROMPT = PromptTemplate(template=rag_chain_prompt_template, input_variables=["context", "question"])
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vector_db.as_retriever(), chain_type_kwargs={"prompt": RAG_PROMPT}
    )
    print("RAG system initialized successfully.")
except Exception as e:
    print(f"FATAL ERROR: Could not initialize RAG system. Error: {e}")
    rag_chain = None

# C. The Guided Conversation Engine's knowledge
conversation_memory = {}
# --- UPDATED: We no longer need 'final_responses' ---
CONVERSATIONAL_FLOWS = {
    'sadness': {
        'keywords': ['sad', 'down', 'unhappy', 'crying', 'heartbroken'],
        'probe_questions': ["I'm really sorry to hear that, {name}. It's okay to feel this way. To help me understand, could you tell me a little about what's causing this sadness?"]
    },
    'anxiety': {
        'keywords': ['anxious', 'worried', 'stressed', 'nervous', 'panicking'],
        'probe_questions': ["Anxiety can feel so overwhelming, {name}. Can you tell me what's on your mind that's making you feel this way?"]
    },
    'work_stress': {
        'keywords': ['work', 'job', 'manager', 'boss', 'coworker', 'deadline'],
        'probe_questions': ["Ugh, stress from work is the worst. I get it, {name}. What part of your job is feeling the most heavy right now?"]
    },
    'study_stress': {
        'keywords': ['study', 'exam', 'homework', 'grades'],
        'probe_questions': ["Study stress is so real. The pressure can be immense. I hear you, {name}. Is it a specific subject or the overall workload?"]
    },
    'loneliness': {
        'keywords': ['lonely', 'alone', 'isolated'],
        'probe_questions': ["Feeling lonely is incredibly tough, {name}. Is this a recent feeling or something you've been carrying for a while?"]
    },
    'tiredness': {
        'keywords': ['tired', 'exhausted', 'sleepy', 'drained'],
        'probe_questions': ["That feeling of being completely drained is so hard to push through. Is this more of a physical tiredness or a mental exhaustion, {name}?"]
    },
    'happiness': {
        'keywords': ['happy', 'great', 'awesome', 'wonderful', 'joyful'],
        # Happiness is still a one-shot response, but we will generate it.
    }
}
SELF_HARM_RESPONSE = (
    "I'm really sorry you're feeling this way. Your safety and wellbeing truly matter. "
    "Please consider speaking to someone who can help — you're not alone:\n\n"
    "🆘 KIRAN Mental Health Helpline (Govt. of India): 1800-599-0019 (24x7, multilingual)\n"
    "🆘 iCall Helpline (TISS): +91 9152987821\n"
    "🆘 AASRA Helpline (Mumbai, 24x7): +91 9820466726\n"
    "🆘 Vandrevala Foundation: 1860 266 2345 or 9999 666 555\n\n"
    "Help is available. There are people who care and want to support you. ❤️"
    "Think of your Mother ,Father and your beatuiful Family — they want to see you happy, healthy, and reaching your full potential."
    "Even when it feels impossible, please remember: this pain is temporary. You are not."

)

DEFAULT_RESPONSE = "I'm listening, {name}. Walk me through what's on your mind."

# --- NEW: A dedicated prompt template for generating empathy ---
empathy_prompt_template = """
You are a caring and empathetic wellness chatbot. Your friend, {name}, has just shared something with you.
Their initial feeling was: {initial_feeling}
Their explanation is: "{user_explanation}"

Your task is to respond with a short, deeply validating, and warm message. Do NOT give advice. Just make them feel heard and understood. Be a kind, supportive friend.
"""
EMPATHY_PROMPT = PromptTemplate(template=empathy_prompt_template, input_variables=["name", "initial_feeling", "user_explanation"])

# --- PART 2: FastAPI Application Logic ---
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="frontend"), name="static")
class ChatRequest(BaseModel):
    message: str; session_id: str

@app.get("/")
async def read_root():
    with open("frontend/index.html") as f: return HTMLResponse(content=f.read(), status_code=200)

@app.post("/chat")
def handle_chat(chat_request: ChatRequest):
    session_id, user_message = chat_request.session_id, chat_request.message.lower()
    
    if session_id not in conversation_memory:
        user_name = user_message.strip().title()
        conversation_memory[session_id] = {'name': user_name, 'state': 'idle'}
        return {"response": f"It's so nice to meet you, {user_name}! What's on your mind today?"}
    
    user_info = conversation_memory[session_id]
    user_name = user_info['name']
    current_state = user_info.get('state', 'idle')

    # 1. Unbreakable Safety Net
    crisis_keywords = ['kill myself', 'suicide', 'wanna die', 'want to die', 'end my life', 'want to live anymore']
    if any(keyword in user_message for keyword in crisis_keywords):
        return {"response": SELF_HARM_RESPONSE}

    # 2. Path Decision: Is the user asking for advice?
    advice_keywords = ['how to', 'how do i', 'how can i', 'help me with', 'what can i do for', 'overcome']
    is_asking_for_advice = any(keyword in user_message for keyword in advice_keywords)

    if is_asking_for_advice and rag_chain:
        print(f"Routing to RAG for advice: '{user_message}'")
        try:
            input_data = {"query": user_message}
            llm_response = rag_chain.invoke(input_data)
            return {"response": llm_response['result']}
        except Exception as e:
            print(f"Error during RAG chain execution: {e}")
            return {"response": "I tried to find some advice, but ran into an issue."}
    else:
        # --- PATH 2: FEELING EXPRESSER (Now with Dynamic Empathy) ---
        print(f"Routing to Guided Conversation. Current state: {current_state}")
        
        # --- UPDATED LOGIC: Handle replies with Dynamic Empathy ---
        if current_state != 'idle':
            print(f"Generating dynamic empathy for state '{current_state}' and user explanation.")
            try:
                # Combine the prompt template with the user's information
                empathy_chain = EMPATHY_PROMPT | llm
                llm_response = empathy_chain.invoke({
                    "name": user_name,
                    "initial_feeling": current_state,
                    "user_explanation": user_message
                })
                response = llm_response.content
            except Exception as e:
                print(f"Error during empathy generation: {e}")
                response = DEFAULT_RESPONSE.format(name=user_name) # Fallback on error
            
            user_info['state'] = 'idle' # Reset state
            return {"response": response}
        
        # B. Detect initial intent and start a conversation
        for intent, flow_data in CONVERSATIONAL_FLOWS.items():
            if any(keyword in user_message for keyword in flow_data['keywords']):
                if 'probe_questions' in flow_data:
                    user_info['state'] = intent
                    response = random.choice(flow_data['probe_questions']).format(name=user_name)
                else: # For one-shot intents like happiness
                    # We can also generate happiness responses now for variety
                    happy_chain = EMPATHY_PROMPT | llm
                    response = happy_chain.invoke({
                        "name": user_name,
                        "initial_feeling": "happiness",
                        "user_explanation": user_message
                    }).content
                return {"response": response}

        # C. If no intent is detected, give a default response
        return {"response": DEFAULT_RESPONSE.format(name=user_name)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)