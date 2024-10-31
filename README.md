Instructions
Objective: To learn how to take user input in Python
Write a program that asks the user for their name, age, and location and then prints out a 
personalized message.
Instructions:
1. Create a new Python file and name it "user_input.py"
2. Use the input() function to ask the user for their name and store it in a variable called 
"name".
3. Use the input() function to ask the user for their age and store it in a variable called 
"age".
4. Use the input() function to ask the user for their location and store it in a variable called 
"location".
5. Print out a personalized message using the user's name, age, and location. For example: 
"Hello [name], you are [age] years old and live in [location]."
6. Save and run the program to see the output

# (link unavailable)

# Ask user for their name
name = input("What's your name? ")

# Ask user for their age
age = input("How old are you? ")

# Ask user for their location
location = input("Where do you live? ")

# Print personalized message
print(f"Hello {name}, you are {age} years old and live in {location}.")
``]

### Running the Program

To run the program:

1. Save the file as "(link unavailable)".
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Type `python (link unavailable)` and press Enter.

### Example Output


What's your name? John
How old are you? 30
Where do you live? New York
Hello John, you are 30 years old and live in New York.


### Notes

* The `input()` function returns a string, so the `age` variable will be a string. If you want to perform arithmetic operations on the age, consider converting it to an integer using `int(age)`.
* The `f-string` formatting (f"Hello {name}...") is used to insert variables into the printed message.
* You can enhance the program by adding error handling, validating user input, or asking additional questions.


Note: Upload the code to github and submit the github link