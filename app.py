import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="BuddyBot 🤖", page_icon="💬")

st.title("💬 BuddyBot — Simple Chatbot")
st.write("Talk to BuddyBot below! Ask about time, jokes, greetings, etc.")

# Chat history storage
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("BuddyBot", response))

# Display chat history
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"**🧍 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
