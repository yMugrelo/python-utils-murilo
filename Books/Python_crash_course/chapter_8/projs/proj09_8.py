messages = [
    "Hi!",
    "How are you?",
    "Let's meet tomorrow.",
    "Don't forget the appointment.",
    "See you soon!"
]
sent_messages = []

def show_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

show_messages(messages, sent_messages)


print("\nOriginal list:", messages)
print("Sent messages:", sent_messages)
