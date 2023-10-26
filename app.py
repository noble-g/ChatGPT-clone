## import libraries
import streamlit as st
import openai

## web app configurations
st.set_page_config(page_title= "Chat GPT clone")
## App title
st.title("Chat GPT clone")

# Set OpenAI API key from Streamlit secrets
#openai.api_key = st.secrets["OPENAI_API_KEY"]
# Replicate Credentials
with st.sidebar:
    st.title('chat GPT clone')
    if "OPENAI_API_KEY" in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai_api = st.secrets["OPENAI_API_KEY"]
        #openai_api = "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"
    else:
        openai_api = st.text_input('Enter your open AI API key:', type='password')
        if not (openai_api.startswith('sk-')):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('not yet perfected, still trying things out')


# Set a default model
## session state is like the memory, holding previous chats
if "openai_model" not in st.session_state:
    st.session_state.openai_model = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]): #what is role
        st.markdown(message["content"]) # what is content?

# Accept user input
if prompt := st.chat_input("Shoot me your questions"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    #st.session_state.messages.append("New message")

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty() #
        full_response = "" #
