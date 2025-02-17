# task 1 
def counting_words(sentence):
    word_count = len(sentence.split())
    print(f"in this sentence there are {word_count} words")

counting_words("this is a testing text for my words counter")

# task 2
price = 0.01
def getting_price(message):
    word_count = len(message.split())
    print(f"this message costs ${word_count * price}")

getting_price("this is a testing text for pricing message")



# task 3
def get_total_price(*messages):
    price = 0
    price_per_word = 0.01
    for message_list in messages:
        for message in message_list:
            price += len(message.split()) * price_per_word
    print(f"this is a price: {price}")

get_total_price(["Hello, World!", "Hello, Python!", "hello everyone"])

# task 4
def format_message(message, sender):
    if message == " " or sender == " ":
        print("Invalid Message")
    else:
        print(f"From {sender}:\n{message}")
        
format_message("hello world", "Nodo")

# task 5
def format_messages(messages, sender):
    for message in messages:
        print(f"From {sender}:\n{message}")

format_messages(["Hello, World!", "Hello, Python!"], "Nodo")
    