


import streamlit as st
from src.agents.receptionist_agent import ReceptionistAgent
from dotenv import load_dotenv

load_dotenv()

receptionist = ReceptionistAgent()

# Initialize session state for messages and context
if "messages" not in st.session_state:
    st.session_state.messages = []
if "context" not in st.session_state:
    st.session_state.context = []
if "is_processing" not in st.session_state:
    st.session_state.is_processing = False


def display_messages():
    for i, (message, is_user) in enumerate(st.session_state.messages):
        with st.chat_message("user" if is_user else "assistant"):
            st.markdown(message)


st.title("Datasmith Health Receptionist")

if st.session_state.is_processing:
    pass
else:
    user_input = st.chat_input("Ask your health-related question...")
    if user_input:
        st.session_state.messages.append((user_input, True))
        st.session_state.is_processing = True
        st.rerun()

display_messages()

if st.session_state.is_processing:
    with st.spinner("Thinking..."):
        # Get the latest user input
        user_input = st.session_state.messages[-1][0]
        # Gather conversation history for context (excluding the latest user input)
        history = [
            {"role": "user" if is_user else "assistant", "content": msg}
            for msg, is_user in st.session_state.messages[:-1]
        ]
        try:
            response = receptionist.invoke(user_input, chat_history=history)
            st.session_state.messages.append((response, False))
        except Exception as e:
            st.session_state.messages.append(
                (f"Sorry, something went wrong. Please try again.\n\nError: {e}", False)
            )
        finally:
            st.session_state.is_processing = False
            st.rerun()
