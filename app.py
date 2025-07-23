# app.py (FINAL, STATELESS, AND RELIABLE VERSION)

import random
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# --- PART 1: The Chatbot's Entire Brain ---
app = FastAPI(title="Stateless and Reliable Wellness Chatbot")

conversation_memory = {}

# The complete knowledge base, organized from most specific to most general
INTENT_HIERARCHY = [
    'work_stress', 'study_stress', 'sadness', 'loneliness', 'stress', 'happiness'
]

INTENT_DATA = {
    'sadness': {
        'keywords': ['sad', 'down', 'unhappy', 'crying', 'heartbroken'],
        'empathy': ["I'm so sorry to hear you're feeling this way, {name}. It's completely okay to not be okay. I'm here to listen.", "That sounds incredibly heavy. Thank you for sharing that with me. Please know your feelings are valid."],
        'advice': ["When sadness feels heavy, sometimes a small change of scenery can help. Could you try stepping outside for just a minute or two? Just to feel the air. It can be a small reset for the mind."]
    },
    'stress': {
        'keywords': ['stress', 'stressed', 'anxious', 'worried', 'overwhelmed', 'nervous', 'panicking'],
        'empathy': ["It sounds like you're carrying a lot right now, {name}. That feeling of being overwhelmed is tough, but you're not alone in it.", "I hear you. That sounds incredibly stressful, and it's completely understandable to feel that way."],
        'advice': ["When you feel overwhelmed, try the 'box breathing' technique: Inhale for 4 seconds, hold for 4, exhale for 4, and wait for 4. It's a simple way to calm your nervous system."]
    },
    'work_stress': {
        'keywords': ['work', 'job', 'manager', 'boss', 'coworker', 'deadline', 'office', 'overwhelming'],
        'empathy': ["Ugh, stress from work is the worst because it can follow you home. I get it, {name}. It's valid to feel drained by that.", "That sounds really frustrating. Dealing with pressure at your job is incredibly difficult."],
        'advice': ["To combat work stress, it's crucial to create a boundary. Can you set a specific time tonight to turn off all work-related notifications? Your mind needs a dedicated break to truly recover."]
    },
    'study_stress': {
        'keywords': ['study', 'studying', 'exam', 'exams', 'homework', 'grades', 'assignment', 'focus'],
        'empathy': ["Study stress is so real. The pressure to perform can be immense. I hear you, {name}.", "That sounds like a lot to handle. It's easy to feel overwhelmed with academic pressure."],
        'advice': ["Try the Pomodoro Technique. Set a timer for 25 minutes of focused study, then take a 5-minute break to do something completely different. It can make studying feel much less like a marathon."]
    },
    'loneliness': {
        'keywords': ['lonely', 'alone', 'isolated'],
        'empathy': ["Feeling lonely is one of the toughest human emotions. Thank you for being brave enough to share that with me, {name}.", "That sense of isolation can be crushing. I want you to know that in this moment, you're not alone. I'm here with you."],
        'advice': ["Sometimes a small act of connection can make a difference. Could you think of one person you could send a simple message to, like 'Hey, just thinking of you!'? There's no pressure for a long chat."]
    },
    'happiness': {
        'keywords': ['happy', 'great', 'awesome', 'wonderful', 'joyful', 'good', 'amazing', 'marks'],
        'empathy': ["That's wonderful to hear, {name}! I'm so glad you're feeling good. Let's celebrate that win!", "Yes! I love that for you, {name}. Hold on to that feeling, you deserve it!"]
    }
}
SELF_HARM_RESPONSE = "I am deeply concerned by what you've shared. Your safety and wellbeing are the most important things right now. Please reach out to someone who can help immediately:\n\n🆘 National Suicide Prevention Lifeline: 988 (US)\n🆘 Crisis Text Line: Text HOME to 741741"
DEFAULT_RESPONSE = "I hear you, {name}. Could you tell me a little more about what's on your mind?"

# --- PART 2: FastAPI Application Logic ---
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="frontend"), name="static")
class ChatRequest(BaseModel): message: str; session_id: str

@app.get("/")
async def read_root():
    with open("frontend/index.html") as f: return HTMLResponse(content=f.read(), status_code=200)

@app.post("/chat")
def handle_chat(chat_request: ChatRequest):
    session_id, user_message = chat_request.session_id, chat_request.message.lower()
    
    if session_id not in conversation_memory:
        user_name = user_message.strip().title()
        conversation_memory[session_id] = {'name': user_name}
        return {"response": f"It's so nice to meet you, {user_name}! What's on your mind today?"}
    
    user_name = conversation_memory[session_id]['name']
    
    # --- The Final, Stateless, Intent-First Engine ---

    # 1. Safety Net (Highest Priority)
    crisis_keywords = ['kill myself', 'suicide', 'wanna die', 'want to die', 'end my life']
    negation_words = ["don't", "do not", "not", "never"]
    is_negated = any(neg in user_message for neg in negation_words)
    if any(keyword in user_message for keyword in crisis_keywords) and not is_negated:
        return {"response": SELF_HARM_RESPONSE}

    # 2. Find the Most Specific Intent
    matched_intent = None
    # We iterate through our defined hierarchy to find the most specific match first
    for intent in INTENT_HIERARCHY:
        if any(keyword in user_message for keyword in INTENT_DATA[intent]['keywords']):
            # Special check to prevent "not happy" from triggering "happiness"
            if is_negated and intent == 'happiness':
                continue
            matched_intent = intent
            break
    
    # 3. Determine the User's Goal
    advice_keywords = ['how to', 'how can i', 'help me', 'what can i do', 'overcome', 'deal with', 'tips for', 'focus']
    is_asking_for_advice = any(keyword in user_message for keyword in advice_keywords)

    # 4. Execute the Correct Action based on Intent and Goal
    if matched_intent:
        flow_data = INTENT_DATA[matched_intent]
        # If the goal is advice, and advice exists for this topic, give it.
        if is_asking_for_advice and 'advice' in flow_data:
            response = random.choice(flow_data['advice'])
        # Otherwise, give a direct, one-shot empathetic response.
        else:
            response = random.choice(flow_data['empathy'])
        
        return {"response": response.format(name=user_name)}

    # 5. If no intent is found, but the user is asking a general advice question, handle it.
    if is_asking_for_advice:
         return {"response": "I'd love to help with that, {name}. Could you tell me a bit more about what topic you need advice on, like sadness, stress, or something else?".format(name=user_name)}

    # 6. If nothing else matches, return the default response.
    return {"response": DEFAULT_RESPONSE.format(name=user_name)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)