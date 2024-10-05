
# AI_Resume_Building_Web_Application
Project Overview
This project is a Flask-based web application that allows users to input their personal details, skills, experience, education, and other relevant information to generate a modern, stylish resume in HTML and CSS format. The app leverages Google Generative AI (Gemini) via Langchain to dynamically generate personalized resume templates. Users fill out a form with their details, and the AI constructs a professional resume with vibrant yet professional design aesthetics.

## Features
- User Input Form: A simple, user-friendly HTML form for collecting essential information such as name, skills, work experience, education, certifications, contact details, etc.
- AI-Powered Resume Generation: Using the Google Generative AI (Gemini) model, the app generates a custom, formatted HTML and CSS resume based on the user's input.
- Dynamic and Modern Resume Design: The generated resume includes dynamic colors, professional tones (teal, light blue, grey, etc.), and a clean layout to ensure a professional presentation.
- Personalized Output: Each resume template is created with personalized details and structured sections for easy readability.
- Downloadable Resume: The output is generated as an HTML file, which the user can save and use.

## Tech Stack
- Backend Framework: Flask (Python)
- Language Model: Google Gemini 1.5 via Langchain
- Front-end: HTML, CSS (generated dynamically)
- AI Integration: Langchain’s Conversational Chain with ConversationBufferMemory
- Deployment: The application runs locally using Flask’s built-in development server
