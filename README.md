# The Uplifting AI Companion 🤖

A sophisticated, dual-path AI chatbot providing empathetic conversation and intelligent advice.  
![Demo GIF](![My_uplifiting_Chatbot](https://github.com/user-attachments/assets/7178fc7b-e6db-4ea8-853b-5cf6b2b916db))

---

## 📚 Table of Contents

- [About The Project](#about-the-project)  
- [Core Architecture: The Dual-Path Logic Engine](#core-architecture-the-dual-path-logic-engine)  
- [Key Features](#key-features)  
- [Technology Stack](#technology-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation & Setup](#installation--setup)  
  - [Live Demo & Testing](#live-demo--testing)  
- [Project Limitations](#project-limitations)

---

## 📖 About The Project

The Uplifting AI Companion is a web-based conversational AI designed to provide a safe, empathetic, and supportive space for users. It addresses the need for immediate, accessible first-line emotional support for individuals experiencing stress, sadness, loneliness, or burnout.

Unlike typical chatbots, this project leverages a hybrid logic architecture that can intelligently choose between dynamic advice and heartfelt empathy — all tailored to the user's intent.

---

## 🧠 Core Architecture: The Dual-Path Logic Engine

'''text
+----------------+
|  User Message  |
+----------------+
       |
       v
+----------------+   YES   +-----------------------+
|  Safety Check  |-------->| Immediate Help Response |
|   (Crisis?)    |         +-----------------------+
+----------------+
       | NO
       v
+----------------+   YES   +-----------------------------+
| Advice Seeking?|-------->| Path 1: RAG / LLM System    |
| ("how to...")  |         | (For Intelligent Advice)    |
+--zzzzz

### 🔹 Path 1: The Advice Seeker (RAG / LLM System)

- Triggered when a user asks a question (e.g., "how to stop overthinking?")
- Combines a Retrieval-Augmented Generation (RAG) pipeline using:
  - A curated knowledge base in .txt files
  - ChromaDB vector search
  - Hugging Face sentence-transformers
  - Groq’s Llama 3 for detailed, intelligent replies

---

### 🔸 Path 2: The Feeling Expresser (Guided Conversation Engine)

- Triggered when a user expresses a feeling (e.g., "I feel so sad.")
- Follows a 2-step empathy flow:
  1. A probing question to understand emotional context
  2. A validating response that reflects the user’s input

---

## 🚀 Key Features

✅ Dual-Path Routing: RAG for advice / Guided flow for emotion  
✅ Empathetic Two-Step Dialogues  
✅ Retrieval-Augmented Generation with Llama 3  
✅ Safety Net for Crisis Detection  
✅ Memory for Personalized Greetings  
✅ Modern, Animated Frontend UI  

---

## 🧰 Technology Stack

| Layer        | Tech Used                                   |
|--------------|----------------------------------------------|
| Backend      | Python, FastAPI, Uvicorn                     |
| AI Framework | LangChain, Hugging Face Transformers         |
| LLM          | Groq (Llama 3 70B)                           |
| Vector DB    | ChromaDB                                     |
| Embeddings   | sentence-transformers from Hugging Face      |
| Frontend     | HTML5, CSS3, Vanilla JavaScript              |

---

### Getting Started

Follow these steps to get a local copy up and running on your machine.

#### Prerequisites

*   Python 3.9+ installed.
*   An active Python virtual environment (recommended).
*   A free API key from [Groq](https://console.groq.com/keys).

#### Installation & Setup

1.  Clone the Repository
    bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    

2.  Install Dependencies
    bash
    pip install -r requirements.txt
    

3.  Set Up Environment Variables
    Create a file named .env in the root of the project and add your Groq API key:
    
    GROQ_API_KEY="gsk_YourActualGroqApiKeyHere"
    

4.  Create Your Knowledge Base
    Create a folder named knowledge_base/ in the root directory. Inside it, add your advice as .txt files. The filenames are important and should correspond to the chatbot's conversational flows (e.g., anxiety_advice.txt, work_stress_advice.txt).

    
    knowledge_base/
    ├── anxiety_advice.txt
    ├── study_stress_advice.txt
    └── loneliness_advice.txt
    

5.  Build the Vector Database
    Run this script once to process your knowledge base files. It only needs to be re-run if you add or change the .txt files.
    bash
    python prepare_vector_db.py
    

6.  Start the Chatbot Application
    bash
    python app.py
    

7.  Visit the Application
    Open your browser and navigate to http://localhost:8000.

---

### Live Demo & Testing

Below are examples of the chatbot's core functionalities, demonstrating its dual-path logic engine.

#### Test 1: Guided Empathetic Conversation
This tests the bot's ability to engage in a stateful, two-step empathetic flow when a user expresses a feeling.

*   User Input: i feel so tired today
*   Bot's Probe Question: That feeling of being completely drained is so hard to push through. Is this more of a physical tiredness or a mental exhaustion, Alexa?
*   User's Reply: i just didn't get enough sleep
*   Bot's Final Response: I hear you. Your body and mind are telling you they need rest. Please listen to them and be gentle with yourself today. Rest is productive.

![Demo of Guided Conversation](https://github.com/user-attachments/assets/70a71de4-23e4-4a72-9154-73b8145a642a)


#### Test 2: Intelligent Advice (RAG System)
This tests the bot's ability to answer a direct question for help using its Retrieval-Augmented Generation (RAG) pipeline.

*   User Input: how can I overcome stress from my job?
*   Expected Bot Behavior: The bot will provide a detailed, conversational answer generated by the LLM, based on the content of your work_stress_advice.txt file.

![Demo of RAG Advice System](https://github.com/user-attachments/assets/57445813-bf17-49c6-b5f6-035af329b224)


#### Test 3: The Unbreakable Safety Net
This verifies the highest-priority safety feature, which overrides all other logic.

*   User Input: i want to die
*   Expected Bot Response: I am deeply concerned by what you've shared. Your safety and wellbeing are the most important things right now. Please reach out to someone who can help immediately: 🆘 National Suicide Prevention Lifeline: 988 (US) 🆘 Crisis Text Line: Text HOME to 741741

![Demo of Safety Net Feature](https://github.com/user-attachments/assets/09138e28-8f12-410f-98fe-b02bdbe59732)

---

### Project Limitations

While robust, the chatbot has some defined limitations that offer clear opportunities for future development:

*   Session-Based Memory: The bot only remembers the user's name within a single browser session. It does not have long-term memory to recall past conversations.
*   Keyword-Based Initial Triage: The initial routing to the "Advice" or "Empathy" path is based on a list of keywords. This is reliable but less nuanced than a machine learning classifier could be.
*   No Proactive Engagement: The bot is purely reactive and will not initiate a conversation or send follow-up notifications.
*   Not a Medical Device: The chatbot is explicitly a supportive companion and not a substitute for professional medical or therapeutic help. It is designed to de-escalate and point users toward professional resources in a crisis.
