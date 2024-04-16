import gradio as gr

from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

model = AzureChatOpenAI(
    openai_api_version="2024-02-15-preview",
    azure_deployment="gpt-35-turbo",
)

def open_ai_prompt(prompt_text):
    return model([HumanMessage(content=prompt_text)]).content

demo = gr.Interface(
    fn=open_ai_prompt, 
    inputs="text", 
    outputs="text",
    title="Hello Azure Red Hat OpenShift and Azure OpenAI",
    description="Demo application for a small chat-agent. Enter your questions below.",
    allow_flagging=False)
    
demo.launch( server_name="0.0.0.0", server_port=8080 )
