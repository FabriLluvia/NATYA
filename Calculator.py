# Importing libraries.
import math
import time
import os

# Printing title.
print("Calculator")
print()
# Declaring menu functions

def show_menu(operations): # Show menu function, used to show all operations based on the dictionary in main_menu function.
    print("Select an option: ")
    for key in sorted(operations):
        print(f' {key}) {operations[key][0]}')

def read_option(operations): # Reads input and checks if the input is in the dictionary in main_menu function.
    while (a := input('Option: ')) not in operations:
        print("Incorrect option, try again with another option.")
    return a

def execute_option(operation, operations): # Executes the input that was already checked by read_option function.
    operations[operation][1]()

def generate_menu(operations, output_option): # Generates the menu joining all above functions output.
    operation = None
    while operation != output_option:
        show_menu(operations) # Shows all of the operations based on the dictionary in main_menu function.
        operation = read_option(operations) # Reads the input with read_option function.
        execute_option(operation, operations) # Executes the input, with execute_option function.
        print()

def main_menu(): # Creates a menu, prints it on console, reads the input, checks if it is on the dictionary and executes the input.
    operations = { # Dictionary where all of the operations are found.
        '1': ("Addition", addition),
        '2': ("Sustraction", sustraction),
        '3': ("Multiplication", multiplication),
        '4': ("Division", division),
        '5': ("Read memory", readMemory),
        '6': ("Exit", exit)
    }
    generate_menu(operations, '6') # Generates the menu.

if not os.path.exists("calculatorMemory.txt"): # Checks if calculatorMemory.txt exists.
        print("Memory file not found, creating one...") # If it doesn't exist, it creates the file.
        with open(file_path, "x"):
            pass

def readMemory(): # Opens calculatorMemory.txt and reads it, so the file can be edited later.
    with open("calculatorMemory.txt", "r") as file: 
        print(file.read())
        time.sleep(2)

def addition():
    print("Addition selected")
    firstNumber = float(input("Enter first number: ")) # Asks for input.
    secondNumber = float(input("Enter second number: "))
    result = firstNumber + secondNumber # Makes the operation.
    print(f"The result of {firstNumber} plus {secondNumber} is equal to {result}.") # Prints the result.
    time.sleep(2) # Waits two seconds.
    save = input("Do you want to save result to memory? Write Y to say yes or anything else to say no: ") # Asks if the result should be saved to memory.
    if save.lower() == 'y': # Checks the input.
        with open("calculatorMemory.txt", "a") as f:
            f.write(f"The result of {firstNumber} plus {secondNumber} is equal to {result}.\n") # Writes the result to memory.
    # Deletes variables to free memory.
    del firstNumber
    del secondNumber
    del result

def sustraction():
    print("Sustraction selected")
    firstNumber = float(input("Enter first number: ")) # Asks for input.
    secondNumber = float(input("Enter second number: "))
    result = firstNumber - secondNumber # Makes the operation.
    print(f"The result of {firstNumber} minus {secondNumber} is equal to {result}.") # Prints the result.
    time.sleep(2) # Waits two seconds.
    save = input("Do you want to save result to memory? Write Y to say yes or anything else to say no: ") # Asks if the result should be saved to memory.
    if save.lower() == 'y': # Checks the input.
        with open("calculatorMemory.txt", "a") as f:
            f.write(f"The result of {firstNumber} minus {secondNumber} is equal to {result}.\n") # Writes the result to memory.
    # Deletes variables to free memory.
    del firstNumber
    del secondNumber
    del result

def multiplication():
    print("Multiplication selected")
    firstNumber = float(input("Enter first number: ")) # Asks for input.
    secondNumber = float(input("Enter second number: "))
    result = firstNumber * secondNumber # Makes the operation.
    print(f"The result of {firstNumber} times {secondNumber} is equal to {result}.") # Prints the result.
    time.sleep(2) # Waits two seconds.
    save = input("Do you want to save result to memory? Write Y to say yes or anything else to say no: ") # Asks if the result should be saved to memory.
    if save.lower() == 'y': # Checks the input.
        with open("calculatorMemory.txt", "a") as f:
            f.write(f"The result of {firstNumber} times {secondNumber} is equal to {result}.\n") # Writes the result to memory.
    # Deletes variables to free memory.
    del firstNumber
    del secondNumber
    del result

def division():
    print("Division selected")
    firstNumber = float(input("Enter first number: ")) # Asks for input.
    secondNumber = float(input("Enter second number: "))
    result = firstNumber / secondNumber # Makes the operation.
    print(f"The result of {firstNumber} divided by {secondNumber} is equal to {result}.") # Prints the result.
    time.sleep(2) # Waits two seconds.
    save = input("Do you want to save result to memory? Write Y to say yes or anything else to say no: ") # Asks if the result should be saved to memory.
    if save.lower() == 'y': # Checks the input.
        with open("calculatorMemory.txt", "a") as f:
            f.write(f"The result of {firstNumber} divided by {secondNumber} is equal to {result}.\n") # Writes the result to memory.
    # Deletes variables to free memory.
    del firstNumber
    del secondNumber
    del result

main_menu() # Creates a menu, prints it on console, reads the input, checks if it is on the dictionary and executes the input.