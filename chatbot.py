import random
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey", "hola"]
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "Why was the computer cold? It forgot to close its Windows."
    ]

    if any(word in user_input for word in greetings):
        return random.choice(["Hello there! 👋", "Hey! How can I help you?", "Hi buddy! 😊"])

    elif "your name" in user_input:
        return "I'm BuddyBot, your friendly chatbot 🤖"

    elif "how are you" in user_input:
        return random.choice(["I'm just a bot, but feeling great!", "Doing awesome, thanks for asking!"])

    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%I:%M %p')} ⏰"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Hmm... I didn’t quite get that. Try asking me something else 😊"
