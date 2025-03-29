import math

print("Calculator")
print()


def show_menu(options):
    print("Select an option: ")
    for key in sorted(options):
        print(f' {key}) {options[key][0]}')

def read_option(options):
    while (a := input('Option: ')) not in options:
        print("Incorrect option, try again with another option.")
    return a

def execute_option(option, options):
    options[option][1]()

def generate_menu(options, output_option):
    opcion = None
    while option != output_option:
        show_menu(options)
        opcion = read_option(options)
        execute_option(option, options)
        print()

def main_menu():
    operations = {
        '1': ("Addition", addition()),
        '2': ("Sustraction", sustraction()),
        '3': ("Multiplication", multiplication()),
        '4': ("Division", division()),
        '5': ("Exit", exit())
    }

    generate_menu(options, '5')

def addition():
    print("Addition selected")

def sustraction():
    print("Sustraction selected")

def multiplication():
    print("Multiplication selected")

def division():
    print("Division selected")

main_menu()