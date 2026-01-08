class UnitConverter:
    def run(self):
        print("1.KM to Miles  2.Celsius to Fahrenheit")
        choice = input("Choose: ")

        try:
            if choice == "1":
                km = float(input("Enter KM: "))
                print("Miles:", km * 0.621371)
            elif choice == "2":
                c = float(input("Enter Celsius: "))
                print("Fahrenheit:", (c * 9/5) + 32)
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")
