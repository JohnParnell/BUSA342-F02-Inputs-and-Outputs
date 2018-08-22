'''
Simple program that combines two strings and two integers and displays them to the user.

firstName and lastName are concatenated and displayed to the user

firstNumber and secondNumber are added together and displayed to the user.

Created by John Parnell for Dr. Eric Wen
'''

# Creates two variables, firstName and lastName and asks the user for Input, their input is saved to the variables.

firstName = input("Aloha! What's your first name? ")
lastName = input("Great! What's your last name? ")

# Those two inputs and then concatenated to create the whole name/
print("Well, that would make your whole name " + firstName + " " + lastName + "!")

# Same idea as the first, however we have to convert the user input to an Int, otherwise it's still a string and will
# simply concatenate the two numbers together. This way, they ADD together, instead of stick together.

firstNumber = int(input("Okay, now let's do something else, give me a number! "))
secondNumber = int(input("Great, now give me a SECOND number! "))


# Finally, the two integers are added together and displayed to the user.
print("The sum of those two numbers is: ", firstNumber + secondNumber, "!")
