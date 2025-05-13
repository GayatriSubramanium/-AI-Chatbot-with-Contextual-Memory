import streamlit as st
from chatbot import generate_reply
from database import log_message


st.title("🧠 AI Chatbot with Memory")

# Session-level chat history
if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if st.button("Send"):
    reply, history = generate_reply(user_input, st.session_state.chat_history_ids)
    st.session_state.chat_history_ids = history
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", reply))

# Display chat
for sender, msg in st.session_state.messages:
    st.markdown(f"**{sender}:** {msg}")

if st.button("Send", key="send_button"):
    reply, history = generate_reply(user_input, st.session_state.chat_history_ids)
    st.session_state.chat_history_ids = history


    # Save user and bot messages
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", reply))

    # 🔥 Log messages to DB
    log_message("User1", "user", user_input)
    log_message("User1", "bot", reply)

