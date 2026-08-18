from datetime import datetime

print("==============================================")
print("          RULE-BASED CHATBOT")
print("==============================================")
print("Hello! I am your chatbot.")
print("You can ask me about my name, time, date,")
print("jokes, programming, or general greetings.")
print("Type 'bye' to exit.")
print("==============================================\n")

while True:
    user_input = input("You: ").lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "hii", "good morning", "good evening"]:
        print("Bot: Hello! Nice to meet you. How can I help you?")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a Rule-Based Chatbot created using Python.")

    # User's name
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        if name:
            print(f"Bot: Nice to meet you, {name.title()}!")
        else:
            print("Bot: Nice to meet you!")

    # Help
    elif "help" in user_input:
        print("Bot: You can ask me about my name, time, date, programming, or ask for a joke.")

    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")

    # Date
    elif "date" in user_input or "today" in user_input:
        current_date = datetime.now().strftime("%d %B %Y")
        print(f"Bot: Today's date is {current_date}.")

    # Programming
    elif "python" in user_input or "programming" in user_input:
        print("Bot: Python is a popular programming language known for its simplicity and versatility.")

    # Joke
    elif "joke" in user_input:
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs! 😄")

    # Thanks
    elif "thank" in user_input:
        print("Bot: You're welcome! 😊")

    # Goodbye
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Try asking about my name, time, date, Python, or say 'help'.")