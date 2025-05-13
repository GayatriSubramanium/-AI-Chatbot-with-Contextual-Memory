import streamlit as st
from chatbot import get_reply

st.title("🧠 AI Chatbot with Memory")

if "history" not in st.session_state:
    st.session_state.history = None

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    reply, history = get_reply(user_input, st.session_state.history)
    st.session_state.history = history

    st.markdown(f"**You:** {user_input}")
    st.markdown(f"**Bot:** {reply}")
