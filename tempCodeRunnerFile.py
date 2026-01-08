from modules.calculator import Calculator
from modules.notes_manager import NotesManager
from modules.timer_tool import TimerTool
from modules.file_organizer import FileOrganizer
from modules.unit_converter import UnitConverter
from modules.utils import press_enter

def main():
    calc = Calculator()
    notes = NotesManager()
    timer = TimerTool()
    organizer = FileOrganizer()
    converter = UnitConverter()

    while True:
        print("""
==============================
 PERSONAL PRODUCTIVITY SUITE
==============================
1. Calculator
2. Notes Manager
3. Timer
4. File Organizer
5. Unit Converter
6. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            calc.run()
        elif choice == "2":
            notes.run()
        elif choice == "3":
            timer.run()
        elif choice == "4":
            organizer.run()
        elif choice == "5":
            converter.run()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

        press_enter()

if __name__ == "__main__":
    main()
