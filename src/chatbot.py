from dotenv import load_dotenv
import os
import gradio as gr
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
llm = GroqModel(api_key=API_KEY)
allowed_models = llm.allowed_models
conversation = MaxSystemContextConversation()

def load_model(selected_model):
    return GroqModel(api_key=API_KEY, name=selected_model)

def chatbot(system_context, input_text, model_name):
    llm = load_model(model_name)
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)
    agent.conversation.system_context = SystemMessage(content=system_context)
    result = agent.exec(str(input_text))
    return str(result)

flagging_dir = "flagged_responses"
if not os.path.exists(flagging_dir):
    os.makedirs(flagging_dir)

iface = gr.Interface(
    fn=chatbot,
    inputs=[gr.Textbox(label="System Context"), gr.Textbox(label="User Input"), gr.Dropdown(choices=allowed_models, label="Model")],
    outputs="text",
    title="Dynamic Chatbot with System Context",
    description="Interact with the chatbot using a system context and user query.",
    flagging_dir=flagging_dir,
    flagging_options=["Inappropriate Response", "Incorrect Information", "Other"]
)

if __name__ == "__main__":
    iface.launch()
