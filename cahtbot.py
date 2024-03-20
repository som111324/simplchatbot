import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you ?', ['I am doing well, thank you.', 'I am fine, thanks for asking.']),
    (r'what is your name ?', ['You can call me ChatBot.', 'I am a chatbot.']),
    (r'what programming languages do you know\?', ['I know Python, Java, C++, and many more.']),
    (r'(.*) programming language\?', ['Yes, programming languages are used to write code and create software.']),
    (r'quit', ['Bye, take care!', 'Goodbye!']),
]

# Create a chatbot with the defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Start chatting with the user
print("Hello, I'm a simple chatbot. You can ask me about programming languages or just say hi!")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
    if user_input.lower() == 'quit':
        break
