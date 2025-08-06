# Personalized Study Assistant Chatbot
The **Personalized Study Assistant Chatbot** is an AI-powered tool designed to make studying more interactive by allowing users to upload PDF notes and ask questions directly based on their content. Built using Python, Streamlit, and the Gemini Pro API, the chatbot processes study materials, understands queries, and delivers accurate, context-aware responses in real time. This project focused on solving a real student problem—navigating static study content—and aimed to build a clean, scalable, and user-friendly solution. Key deliverables included PDF parsing, semantic search, and dynamic Q\&A functionality, while milestones involved designing architecture, integrating APIs, and testing across subjects. The project showcases my ability to apply AI to practical learning problems and lays the groundwork for future enhancements like voice input, study planning, and chat history management.


## Table of Contents

- [Project Objective](-project-objective)
- [Features](-features)
- [Tech Stack Used](-tech-stack-used)
- [Installation and Setup](-installation-and-setup)
- [How to Use](-how-to-use)
- [Constraints](-Constraints)
- [Future Scope](-future-scope)
- [Folder Structure](-Folder-Structure)
- [License](-license)



## Project Objective

To develop an AI chatbot that assists students with personalized learning, allowing them to upload study material and receive real-time responses. This bot aims to support diverse learning styles by offering contextually relevant explanations and answers from course material.


## Features

- Chatbot-like interface for seamless interaction
- Upload and read study PDFs
- Ask context-aware questions based on uploaded content
- Uses Gemini Pro API for LLM-powered answers
- Session history retention
- Clean, minimal Streamlit UI

## Tech Stack Used

- **Python** – Core programming language
- **Streamlit** – UI/UX for chatbot frontend
- **Gemini API (Google Generative AI)** – Backend LLM for generating responses
- **PDF Reader (PyMuPDF / fitz)** – For processing uploaded files

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or above
- `pip` package manager
- Google Gemini API Key *(see [API Key Notice](#️-api-key-notice))*

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/your-username/personalized-study-assistant-chatbot.git
cd personalized-study-assistant-chatbot
```
2. Install the dependencies
```
pip install -r requirements.txt
```
3. Add your Gemini API key
```
GEMINI_API_KEY = "your_actual_gemini_api_key"
```
Do not expose your API key in public

4. Run the application
```
streamlit run app.py
```

## How to Use
1. Launch the app: streamlit run app.py
2. Upload your PDF study material.
3. Ask questions in the chatbot input field.
4. The assistant responds using Gemini API based on the context of your uploaded material.


## Constraints
This project is not deployed online because the Gemini API key used for generating responses is private and restricted under a free-tier quota. The API key is stored locally and is not meant for public use. This project is intended purely for personal learning, development experience, and offline demonstration.

## Future Scope
The project has the potential to be scaled and enhanced with the following planned improvements:

1. Voice input and output capabilities using speech-to-text and text-to-speech
2. Study Plan Generator: Allows users to input their time and subjects to generate personalized timetables
3. Persistent Chat History: Save conversations like ChatGPT or Gemini to allow continuity across sessions
4. User Authentication: Multiple users can maintain separate chat histories and preferences
5. Database Integration: Use Firebase or PostgreSQL for storing chat history, user data, and uploaded files
6. Caching Mechanism: Optimize API usage by storing repeated queries and avoiding redundant calls
7. Deployment: Host the application using Streamlit Cloud or other cloud services with secure key handling

## Folder Structure
```
personalized-study-assistant-chatbot/
│
├── mainapp.py
├── requirements.txt
├── README.md
└── .gitignore
```
## License
This project is licensed under the MIT License. See the ```LICENSE``` file for details.
