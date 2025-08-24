def calculator():
    print("Simple Calculator")
    print("=" * 20)
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")  

        choice = input("\nEnter your choice (1-4 or +, -, *, /): ")
        result = None
        if choice in ['1', '+']:
            result = num1 + num2
            operation = "+"
        elif choice in ['2', '-']:
            result = num1 - num2
            operation = "-"
        elif choice in ['3', '*']:
            result = num1 * num2
            operation = "*"
        elif choice in ['4', '/']:
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
            operation = "/"
        else:
            print("Invalid operation choice!")
            return
        print(f"\n{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    while True:
        calculator()
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("Thank you for using the calculator!")
            break
        print()
if __name__ == "__main__":
    main()