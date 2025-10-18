import random
import gradio as gr

# -------------------------------
#  Chatbot Logic
# -------------------------------
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "hello": ["Hi!", "Hello! 😊", "Hey, nice to see you!"],
    "how are you": ["I'm just a bot, but I'm doing great!", "All good here. How about you?", "Feeling chatty today!"],
    "what's your name": ["I'm ChatBuddy 🤖", "You can call me ChatBuddy!", "ChatBuddy at your service!"],
    "tell me a joke": [
        "Why don’t skeletons fight each other? They don’t have the guts. 😄",
        "Why was the math book sad? It had too many problems. 📘",
        "I tried to catch fog yesterday… Mist! ☁️"
    ],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day! 👋"]
}

fallbacks = [
    "Hmm, I didn’t get that. Could you try again?",
    "Interesting... tell me more!",
    "I'm not sure I understand yet, but I'm learning 😊",
]

def chatbot_reply(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(fallbacks)

# -------------------------------
#  Gradio UI
# -------------------------------
def chat(user_input, history):
    bot_response = chatbot_reply(user_input)
    history.append((user_input, bot_response))
    return history, history

with gr.Blocks(title="ChatBuddy") as demo:
    gr.Markdown("## 🤖 Welcome to **ChatBuddy** — Your Friendly Chatbot!")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(placeholder="Type your message here...")
    clear = gr.Button("Clear Chat")

    msg.submit(chat, [msg, chatbot], [chatbot, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
