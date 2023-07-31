#print("Day 1 printing function")
#print("The function is declared like this: ")
#print("print('What to print')")

#print("\nPrinting in different lines!")
#print("Hello")
#print("Hello")
#print("Hello")
#print("-------------------------------------")
#print("Hello\nHello\nHello")
#print("-------------------------------------")
#print("\nHello" "Alan")

#Fix the code below 👇

#print("Day 1 - String Manipulation")
#print('String Concatenation is done with the' ' "+" ' 'sign.')
#print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslash and n."))

#print("Hello, " + input("What is your name? ") + "!")

#string = input("What is your name? ")
#print(len(string))

#print( len( input("What is your name? ")))

#name = input("What is your name? ")
#length = len(name)
#print(length)

#################### PROJECT DAY 1 ####################
#1. Create a greeting for your program.
print("Yo. This is your Band Name GENERATOR!")
print("Answer the following questions so we can generate your BAND NAME!")
#2. Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of one pet of yours?\n")
#4. Combine the name of their city and pet and show them their band name.
a = city
city = pet
pet = a
print("Here's your band name: \n" + pet + " " + city)
#5. Make sure the input cursor shows on a new line: