import json
import os
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "notes.json")

class NotesManager:
    def __init__(self):
        self.notes = []
        self.ensure_data_file()
        self.load_notes()

    def ensure_data_file(self):
        # Create data directory if it doesn't exist
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        # Create notes.json if it doesn't exist
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def load_notes(self):
        with open(DATA_FILE, "r") as f:
            self.notes = json.load(f)

    def save_notes(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.notes, f, indent=4)

    def add_note(self):
        title = input("Title: ")
        content = input("Content: ")

        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.notes.append(note)
        self.save_notes()
        print("Note added successfully")

    def view_notes(self):
        if not self.notes:
            print("No notes available")
            return

        for note in self.notes:
            print("\n----------------------")
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print(f"Created: {note['created']}")

    def run(self):
        while True:
            print("\n1. View Notes  2. Add Note  3. Back")
            choice = input("Choose: ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                break
            else:
                print("Invalid choice")
