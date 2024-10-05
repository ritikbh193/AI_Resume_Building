
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

## Key Libraries and Dependencies
- Flask: Micro web framework for handling HTTP requests and serving web pages.
- Langchain: Used for interacting with large language models, specifically the Google Gemini API.
- Google Generative AI (Gemini): Powered by Google's LLM (large language model) for dynamic resume generation.
- ConversationBufferMemory: Maintains the chat context for interaction with the LLM to produce coherent and relevant responses based on prior user inputs.


## Usage
1. Open the app in your browser.
2. Fill out the form with your personal details, skills, work experience, education, and contact details.
3. Submit the form. The AI model processes the data and generates a resume based on the inputs.
4. The generated resume is displayed as an HTML response, which can be saved locally for further use.

   
## Form Fields
The form takes the following inputs:

- Name: The user's full name.
- Skills: A list of the user's skills (e.g., programming languages, technical skills).
- Experience: Work experience details, including job titles and responsibilities.
- Education: Degree, university, graduation year, and CGPA.
- Certifications: Optional certifications or achievements.
- Contact Information: Address, phone number, email, and LinkedIn profile.
- Example
* User Input:

Name: John Doe

Skills: Python, Flask, React

Experience: Software Developer at ABC Corp

Education: B.Sc. in Computer Science from XYZ University (Graduation Year: 2022)
CGPA: 3.8
Certifications: AWS Certified Solutions Architect
Contact: Phone Number, Address, Email, LinkedIn
Output:
A clean and modern resume in HTML format with structured sections for name, skills, experience, education, contact information, and certifications, styled dynamically with CSS.

## Future Enhancements
- PDF Export: Add functionality to export the generated resume to PDF format.
- Custom Templates: Allow users to choose from a variety of design templates.
- Login System: Introduce a user authentication system to save and manage multiple resumes.
