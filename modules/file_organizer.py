import os
import shutil

class FileOrganizer:
    def run(self):
        path = input("Enter directory path: ")

        if not os.path.isdir(path):
            print("Invalid directory")
            return

        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                ext = file.split(".")[-1]
                folder = os.path.join(path, ext.upper() + "_FILES")
                os.makedirs(folder, exist_ok=True)
                shutil.move(full_path, folder)

        print("Files organized successfully")
