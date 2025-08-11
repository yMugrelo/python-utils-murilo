def show_messages(messages, completed_messages):
    while messages:
        current_message = messages.pop()
        print(f"message: {current_message}")
        completed_messages.append(current_message)



        
    
messages = [
    "Hi!",
    "How are you?",
    "Let's meet tomorrow.",
    "Don't forget the appointment.",
    "See you soon!"
]
show_messages(messages)