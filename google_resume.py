




from flask import Flask, request, render_template_string, jsonify
import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__)

# Initialize Google Generative API
# google_api_key = 'API KEY'
google_api_key = 'API KEY'
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0.7, google_api_key=google_api_key)

memory = ConversationBufferMemory()
conversation_chain = ConversationChain(llm=llm, memory=memory)

# HTML form embedded within Flask route
form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Builder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: grey;
        }
        label {
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: teal;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #005f5f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Resume Builder</h1>
        <form method="POST" action="/submit_resume">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="skills">Skills:</label>
            <textarea id="skills" name="skills" rows="3" required></textarea>

            <label for="experience">Experience 1:</label>
            <textarea id="experience" name="experience" rows="3" required></textarea>

            <label for="experience2">Experience 2 (Details):</label>
            <textarea id="experience2" name="experience2" rows="3" required></textarea>

            <label for="education">Education:</label>
            <input type="text" id="education" name="education" required>

            <label for="university">University:</label>
            <input type="text" id="university" name="university" required>

            <label for="graduation_year">Graduation Year:</label>
            <input type="number" id="graduation_year" name="graduation_year" required>

            <label for="degree">Degree:</label>
            <input type="text" id="degree" name="degree" required>

            <label for="cgpa">CGPA:</label>
            <input type="number" step="0.01" id="cgpa" name="cgpa" required>

            <label for="certifications">Certifications:</label>
            <textarea id="certifications" name="certifications" rows="3"></textarea>

            <label for="linkedin_url">LinkedIn URL:</label>
            <input type="url" id="linkedin_url" name="linkedin_url" required>

            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required>

            <label for="phone_number">Phone Number:</label>
            <input type="tel" id="phone_number" name="phone_number" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/submit_resume', methods=['POST'])
def submit_resume():
    # Get the form data from the POST request
    data = request.form

    # Construct the resume prompt
    resume_prompt = f'''
    Prompt: "Generate an HTML and CSS code for a clean, modern, and stylish resume template. The template should include the following sections:

    A header with the candidate's name and position (e.g., Software Engineer).
    A Personal Summary section with a brief introduction.
    A Skills section displayed as a list of programming languages and other relevant skills.
    An Experience section with job titles, companies, and descriptions of responsibilities.
    An Education section listing degrees and academic achievements.
    A Contact Information section including address, phone number, email, and website.
    A Personal References section with names and contact details of professional references.
    Use dynamic colors and dynamic design for each generation to apply vibrant but professional tones (e.g., teal, light blue, white, and other variations). Ensure you have to provide the combined code for a single template.
    use grey color for header and bold for fonts

    use these details:
    Name - {data['name']}
    Skills - {data['skills']}
    Experience - 
    {data['experience']}

    {data['experience2']}

    Education - {data['education']}
    {data['university']} | Graduation Year: {data['graduation_year']}
    Specialized in {data['degree']} with {data['cgpa']} CGPA.

    Certifications - {data['certifications']}
    
    Contact - {data['phone_number']}
    Address - {data['address']}
    Email - {data['email']}
    LinkedIn - {data['linkedin_url']}
    '''
    
    # Call the LLM model to generate the resume
    response = conversation_chain.run(input=resume_prompt)
    filename = "resume_output.html"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response)
        
    # Return the generated HTML response
    return response  # Return the raw HTML for the generated resume


if __name__ == '__main__':
    app.run(debug=True)




    # def save_resume_as_html(resume_html):
    #     # Specify the filename
    #     filename = "resume_output.html"
        
    #     # Write the HTML content to a file
    #     with open(filename, 'w', encoding='utf-8') as file:
    #         file.write(resume_html)
        
    #     print(f"Resume saved as {filename}. You can download it now.")

    # save_resume_as_html(resume_html=res)
