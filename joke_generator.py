import random

# Step 1: Create a list of jokes
jokes = [
    "Why do Python programmers prefer dark mode? Because light attracts bugs!",
    "Why do programmers hate nature? It has too many bugs.",
    "How do you tell HTML from HTML5? By the doctype!",
    "Why do Java developers wear glasses? Because they don’t see sharp.",
    "What is a programmer's favorite hangout place? Foo Bar!",
    "Why do programmers prefer iOS development? Because they can’t handle Android's Java runtime!",
    "What do you call a programmer from Finland? Nerdic!",
    "Why was the developer unhappy at their job? They wanted arrays but got stuck with a string!",
    "How many programmers does it take to change a light bulb? None; it’s a hardware problem!",
    "Why did the programmer quit their job? Because they didn’t get arrays!",
    "What’s a programmer’s favorite snack? Microchips!",
    "Why was the JavaScript developer sad? Because they didn’t know how to 'null' their feelings!",
    "What do you get when you cross a computer and a lifeguard? A screensaver!",
    "Why did the developer go broke? Because they used up all their cache!",
    "How do you comfort a JavaScript bug? You console it!",
    "Why don’t programmers like nature? It has too many bugs.",
    "How does a computer get drunk? It takes screenshots.",
    "Why do robots never get angry? They always keep their cool circuits!",
    "Why was the computer cold? It left its Windows open!",
    "How do you fix a broken pizza? With tomato paste!",
    "Why did the computer go to art school? To improve its pixels!",
    "Why did the developer bring a ladder to work? To reach the high-level programming!",
    "Why don't computers play soccer? They might get a byte out of it!",
    "Why did the computer visit the doctor? Because it had a virus!",
    "What do you get when you cross a computer and a lifeguard? A screensaver!",
    "Why did the developer go broke? He used up all his cache!",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
    "Why did the computer keep sneezing? It had a virus!",
    "How do computers get drunk? They take screenshots!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "Why do Java developers wear glasses? Because they can't C#!",
    "Why was the developer unhappy at their job? They wanted arrays but got stuck with a string!",
    "Why don't programmers like nature? It has too many bugs.",
    "How many programmers does it take to change a light bulb? None, it's a hardware problem!",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings!",
    "How do you comfort a JavaScript bug? You console it!",
    "Why did the programmer go broke? Because he used up all his cache!",
    "Why don’t programmers like nature? It has too many bugs.",
    "How does a computer get drunk? It takes screenshots.",
    "Why did the developer go broke? Because he used up all his cache!",
    "Why do programmers prefer iOS development? Because they can't handle Android's Java runtime!",
    "What’s a programmer’s favorite hangout place? Foo Bar!",
    "Why do Java developers wear glasses? Because they don’t see sharp.",
    "How do you comfort a JavaScript bug? You console it!",
    "What do you get when you cross a computer and a lifeguard? A screensaver!",
    "Why did the programmer quit his job? Because he didn’t get arrays!",
    "What’s a programmer’s favorite snack? Microchips!",
    "Why do programmers hate nature? It has too many bugs.",
    "What do you call a programmer from Finland? Nerdic!",
    "How do programmers stay cool in the summer? They have lots of fans!",
    "Why was the developer unhappy? They couldn't debug their emotions!",
    "Why do robots never get angry? They always keep their cool circuits!",
]

# Step 2: Function to print jokes without repeating until all jokes are used
def print_random_joke(jokes_list):
    random.shuffle(jokes_list)
    used_jokes = set()
    
    for joke in jokes_list:
        if joke not in used_jokes:
            print(joke)
            used_jokes.add(joke)

            if len(used_jokes) == len(jokes_list):
                used_jokes.clear()
                random.shuffle(jokes_list)
            break

# Step 3: Test the function
for _ in range(1):  # Print more than the number of jokes to test the cycle
    print_random_joke(jokes)
