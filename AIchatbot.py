print("=========================")
print("     DecodeLbas")
print("=========================")
print("type 'bye' anytime to exit.\n")
while True:
    user_input = input("You:").lower()
    # Greetings
    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif user_input == "how are you":
        print("Bot: I am doing good, Thank you for asking.")
    elif user_input == "what is your name":
        print("Bot: I am AIVA, your personal AI assistant.")
    elif user_input == "how old are you":
        print("Bot: I was created last week!")
    elif user_input == "who made you":
        print("Bot: I was made by Aaishah")
    elif user_input == "favourite colour":
        print("Bot: I like black, what's yours?")
    elif user_input == "what is 2 plus 2":
        print("Bot: the answer is 4")
    elif user_input == "help":
        print("Bot: try typing greetings, questions or bye to exit.")
    # Exit commands
    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! nice meeting you, have a great day.")
        break
    # unknown inputs
    else:
        print("Bot: Sorry, i cannot seem to understand that yet, is there anything else i could help with?")
