def add():
    print("\n--- Addition ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

def subtract():
    print("\n--- Subtraction ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

def multiply():
    print("Multiplication function coming soon.")

def divide():
    print("Division function coming soon.")

def main():
    while True:
        print("\n--- Calculator Master ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Select an operation (1-5): ")
        
        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
