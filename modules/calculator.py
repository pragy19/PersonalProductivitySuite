class Calculator:
    def run(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("1.Add  2.Subtract  3.Multiply  4.Divide")
            choice = input("Choose operation: ")

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                if b == 0:
                    print("Cannot divide by zero")
                else:
                    print("Result:", a / b)
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid number input")
