import random  # Step 1: Import random module
# Step 2: Define the quiz questions and answers
questions = [
    {
        "question": "What’s the best way to declare a variable in Python?",
        "options": ["A) var name = \"Python\"", "B) let name = 'Python' 💻", "C) name = \"Python\" 🐍", "D) int name = Python"],
        "answer": "C"
    },
    {
        "question": "Which of these is a valid Python data type?",
        "options": ["A) Pizza 🍕", "B) List 📜", "C) Taco 🌮", "D) String 🧵"],
        "answer": "B"
    },
    {
        "question": "How would you collect a user's name in Python?",
        "options": ["A) input(name \"What's your name?\")", "B) name.collect(\"What's your name?\")", "C) ask name \"What's your name?\"", "D) name = input(\"What's your name?\") 💬"],
        "answer": "D"
    },
    {
        "question": "What’s the result of this Python operation: 5 + 3 * 2?",
        "options": ["A) 11 🔢", "B) 16", "C) 10 🤔", "D) 13"],
        "answer": "A"
    },
    {
        "question": "Which of the following is the correct way to check a variable’s data type?",
        "options": ["A) typeof(variable) 🔍", "B) type(variable) 🧪", "C) datatype(variable)", "D) checktype(variable)"],
        "answer": "B"
    }
]

def play_quiz():
    score = 0  # Initialize the score
    
    random.shuffle(questions) # Shuffle the questions

    # Step 3: Loop through each question
    for q in questions:
        print(q["question"])  # Print the question
        for option in q["options"]:
            print(option)  # Print the options

        user_answer = input("Your answer (A/B/C/D): ").upper()  # Get user input and convert to uppercase

        # Step 4: Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 20  # Increase score
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    # Step 5: Show the final score
    print(f"Your final score is {score} out of {len(questions)}.")

# Step 6: Allow the user to play again
while True:
    play_quiz()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

