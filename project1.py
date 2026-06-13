print("Welcome to the AI Chatbot!")

while True:
    user = input("You: ").lower().strip()
    user = user.replace("?", "")

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who are you":
        print("Bot: I am a simple rule-based chatbot.")

    elif user == "what is the meaning of sad":
        print("Bot: Sad means feeling unhappy or sorrowful.")

    elif user in ["bye", "exit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")