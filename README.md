# The Uplifting AI Companion 🤖

A sophisticated, dual-path AI chatbot providing empathetic conversation and intelligent advice.  
<<<<<<< Updated upstream
DEMO
![Screen Recording 2025-07-10 084018](https://github.com/user-attachments/assets/df5f147a-a2f6-4f89-a1d4-692df75a6683)

=======
![Demo GIF](https://www.canva.com/design/DAGsvEdGK_A/i0dyYov4_oC4h5HrPHHrtw/edit?utm_content=DAGsvEdGK_A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
The Uplifting AI Companion is a web-based conversational AI designed to provide a safe, empathetic, and supportive space for users. It addresses the need for immediate, accessible first-line emotional support for individuals experiencing stress, sadness, loneliness, or burnout.

Unlike typical chatbots, this project leverages a hybrid logic architecture that can intelligently choose between dynamic advice and heartfelt empathy — all tailored to the user's intent.
=======
The **Uplifting AI Companion** is a web-based conversational AI designed to provide a safe, empathetic, and supportive space for users. It addresses the need for immediate, accessible first-line emotional support for individuals experiencing stress, sadness, loneliness, or burnout.

Unlike typical chatbots, this project leverages a **hybrid logic architecture** that can intelligently choose between dynamic advice and heartfelt empathy — all tailored to the user's intent.
>>>>>>> Stashed changes

---

## 🧠 Core Architecture: The Dual-Path Logic Engine

<<<<<<< Updated upstream
```
=======
'''text
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
```

### 🔹 Path 1: The Advice Seeker (RAG / LLM System)

- Triggered when a user asks a question (e.g., "how to stop overthinking?")
- Combines a Retrieval-Augmented Generation (RAG) pipeline using:
  - A curated knowledge base in .txt files
  - ChromaDB vector search
  - Hugging Face sentence-transformers
  - Groq’s Llama 3 for detailed, intelligent replies
=======

### 🔹 Path 1: The Advice Seeker (RAG / LLM System)

- Triggered when a user asks a question (e.g., _"how to stop overthinking?"_)
- Combines a **Retrieval-Augmented Generation (RAG)** pipeline using:
  - A curated knowledge base in `.txt` files
  - ChromaDB vector search
  - Hugging Face sentence-transformers
  - Groq’s **Llama 3** for detailed, intelligent replies
>>>>>>> Stashed changes

---

### 🔸 Path 2: The Feeling Expresser (Guided Conversation Engine)

<<<<<<< Updated upstream
- Triggered when a user expresses a feeling (e.g., "I feel so sad.")
- Follows a 2-step empathy flow:
  1. A probing question to understand emotional context
  2. A validating response that reflects the user’s input
=======
- Triggered when a user expresses a feeling (e.g., _"I feel so sad."_)
- Follows a **2-step empathy flow**:
  1. A **probing question** to understand emotional context
  2. A **validating response** that reflects the user’s input
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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
=======
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up Environment Variables**
    Create a file named `.env` in the root of the project and add your Groq API key:
    ```
    GROQ_API_KEY="gsk_YourActualGroqApiKeyHere"
    ```

4.  **Create Your Knowledge Base**
    Create a folder named `knowledge_base/` in the root directory. Inside it, add your advice as `.txt` files. The filenames are important and should correspond to the chatbot's conversational flows (e.g., `anxiety_advice.txt`, `work_stress_advice.txt`).
>>>>>>> Stashed changes

    
    knowledge_base/
    ├── anxiety_advice.txt
    ├── study_stress_advice.txt
    └── loneliness_advice.txt
    

<<<<<<< Updated upstream
5.  Build the Vector Database
    Run this script once to process your knowledge base files. It only needs to be re-run if you add or change the .txt files.
=======
5.  **Build the Vector Database**
    Run this script once to process your knowledge base files. It only needs to be re-run if you add or change the `.txt` files.
>>>>>>> Stashed changes
    bash
    python prepare_vector_db.py
    

<<<<<<< Updated upstream
6.  Start the Chatbot Application
=======
6.  **Start the Chatbot Application**
>>>>>>> Stashed changes
    bash
    python app.py
    

<<<<<<< Updated upstream
7.  Visit the Application
    Open your browser and navigate to http://localhost:8000.
=======
7.  **Visit the Application**
    Open your browser and navigate to `http://localhost:8000`.
>>>>>>> Stashed changes

---

### Live Demo & Testing

Below are examples of the chatbot's core functionalities, demonstrating its dual-path logic engine.

#### Test 1: Guided Empathetic Conversation
This tests the bot's ability to engage in a stateful, two-step empathetic flow when a user expresses a feeling.

<<<<<<< Updated upstream
*   User Input: i feel so tired today
*   Bot's Probe Question: That feeling of being completely drained is so hard to push through. Is this more of a physical tiredness or a mental exhaustion, Alexa?
*   User's Reply: i just didn't get enough sleep
*   Bot's Final Response: I hear you. Your body and mind are telling you they need rest. Please listen to them and be gentle with yourself today. Rest is productive.
=======
*   **User Input:** `i feel so tired today`
*   **Bot's Probe Question:** `That feeling of being completely drained is so hard to push through. Is this more of a physical tiredness or a mental exhaustion, Alexa?`
*   **User's Reply:** `i just didn't get enough sleep`
*   **Bot's Final Response:** `I hear you. Your body and mind are telling you they need rest. Please listen to them and be gentle with yourself today. Rest is productive.`
>>>>>>> Stashed changes

![Demo of Guided Conversation](https://github.com/user-attachments/assets/70a71de4-23e4-4a72-9154-73b8145a642a)


#### Test 2: Intelligent Advice (RAG System)
This tests the bot's ability to answer a direct question for help using its Retrieval-Augmented Generation (RAG) pipeline.

<<<<<<< Updated upstream
*   User Input: how can I overcome stress from my job?
*   Expected Bot Behavior: The bot will provide a detailed, conversational answer generated by the LLM, based on the content of your work_stress_advice.txt file.
=======
*   **User Input:** `how can I overcome stress from my job?`
*   **Expected Bot Behavior:** The bot will provide a detailed, conversational answer generated by the LLM, based on the content of your `work_stress_advice.txt` file.
>>>>>>> Stashed changes

![Demo of RAG Advice System](https://github.com/user-attachments/assets/57445813-bf17-49c6-b5f6-035af329b224)


#### Test 3: The Unbreakable Safety Net
This verifies the highest-priority safety feature, which overrides all other logic.

<<<<<<< Updated upstream
*   User Input: i want to die
*   Expected Bot Response: I am deeply concerned by what you've shared. Your safety and wellbeing are the most important things right now. Please reach out to someone who can help immediately: 🆘 National Suicide Prevention Lifeline: 988 (US) 🆘 Crisis Text Line: Text HOME to 741741
=======
*   **User Input:** `i want to die`
*   **Expected Bot Response:** `I am deeply concerned by what you've shared. Your safety and wellbeing are the most important things right now. Please reach out to someone who can help immediately: 🆘 National Suicide Prevention Lifeline: 988 (US) 🆘 Crisis Text Line: Text HOME to 741741`
>>>>>>> Stashed changes

![Demo of Safety Net Feature](https://github.com/user-attachments/assets/09138e28-8f12-410f-98fe-b02bdbe59732)

---

### Project Limitations

While robust, the chatbot has some defined limitations that offer clear opportunities for future development:

<<<<<<< Updated upstream
*   Session-Based Memory: The bot only remembers the user's name within a single browser session. It does not have long-term memory to recall past conversations.
*   Keyword-Based Initial Triage: The initial routing to the "Advice" or "Empathy" path is based on a list of keywords. This is reliable but less nuanced than a machine learning classifier could be.
*   No Proactive Engagement: The bot is purely reactive and will not initiate a conversation or send follow-up notifications.
*   Not a Medical Device: The chatbot is explicitly a supportive companion and not a substitute for professional medical or therapeutic help. It is designed to de-escalate and point users toward professional resources in a crisis.
=======
*   **Session-Based Memory:** The bot only remembers the user's name within a single browser session. It does not have long-term memory to recall past conversations.
*   **Keyword-Based Initial Triage:** The initial routing to the "Advice" or "Empathy" path is based on a list of keywords. This is reliable but less nuanced than a machine learning classifier could be.
*   **No Proactive Engagement:** The bot is purely reactive and will not initiate a conversation or send follow-up notifications.
*   **Not a Medical Device:** The chatbot is explicitly a supportive companion and **not** a substitute for professional medical or therapeutic help. It is designed to de-escalate and point users toward professional resources in a crisis.

>>>>>>> Stashed changes
