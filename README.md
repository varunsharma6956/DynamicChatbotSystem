Dynamic Chatbot System
This is a Dynamic Chatbot system built using Gradio, which allows users to select a model from a list of GroqModels and interact with the chatbot by providing system context and user input. The system also provides options for flagging responses if needed.

Table of Contents
Features
Setup
Running the Project
Deployment
Flagging System
Technologies Used



Features -
Dynamic selection of different chatbot models.
User can interact with the chatbot using custom system context and queries.
Responses can be flagged with different reasons like "Inappropriate Response", "Incorrect Information", or "Other".
Simple and intuitive UI using Gradio.



Setup -

Clone the repository:
git clone https://github.com/your-username/DynamicChatbotSystem.git

Navigate into the directory:
cd DynamicChatbotSystem

Install the required packages:

Make sure to install the following required Python packages:
pip install -r requirements.txt

Setup environment variables:

Create a .env file in the root directory and add your API key:

GROQ_API_KEY="your_api_key_here"


Running the Project:
python src/chatbot.py

The Gradio interface will start, and you can access it at the local URL provided (e.g., http://128.0.0.1:7190).





Flagging System
You can flag a response using three options: "Inappropriate Response", "Incorrect Information", or "Other".
Flagged responses are saved in the flagged_responses directory with a log in log.csv.


Technologies Used
Gradio: For creating the user interface.
dotenv: For managing environment variables securely.
Python 3.12 for scripting.
Swarmauri package: Used for GroqModels, conversation handling, and chatbot system context.
