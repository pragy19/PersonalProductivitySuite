📘 Personal Productivity Suite (Python)

A command-line based productivity application built with Python that brings together multiple everyday tools into a single, cohesive system. This project demonstrates strong Python fundamentals, clean architecture, and real-world problem solving.

🏆 Developed as part of Month 1 – Python Programming Mastery

📌 Project Overview

The Personal Productivity Suite is a modular Python application designed to improve daily productivity through commonly used utilities such as a calculator, notes manager, timer, file organizer, and more.

The project emphasizes:

Object-Oriented Programming (OOP)

Modular and reusable code

Persistent data storage

Robust error handling

Clean project structure and documentation

🎯 Project Objectives

✅ Apply Python concepts in a real-world application

✅ Design a modular and scalable codebase

✅ Implement persistent storage using multiple file formats

✅ Build a user-friendly, menu-driven CLI interface

✅ Follow industry-standard project structure and documentation practices

🛠 Tools Included
Tool	Description
🧮 Calculator	Perform basic arithmetic operations
📝 Notes Manager	Create, view, update, and delete notes (JSON-based)
⏱ Timer / Stopwatch	Measure elapsed time and countdowns
📂 File Organizer	Automatically organize files by type
🔁 Unit Converter	Convert between common units
💾 Backup & Restore	Backup and restore important data
⚙️ Technology Stack

Language: Python 3.x

Libraries Used (Standard Library Only):

os

json

csv

time

datetime

shutil

🚫 No third-party libraries required

📂 Project Structure
PersonalProductivitySuite/
│
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
│
├── modules/
│   ├── calculator.py      # Calculator logic
│   ├── notes_manager.py   # Notes CRUD & JSON persistence
│   ├── timer_tool.py      # Timer & stopwatch
│   ├── file_organizer.py  # File organization utility
│   ├── unit_converter.py  # Unit conversion functions
│   └── utils.py           # Shared helper utilities
│
├── data/
│   ├── notes.json         # Persistent notes storage
│   └── backups/           # Backup files

🧱 Key Features

🔹 Modular architecture with clearly separated concerns

🔹 Menu-driven command-line interface

🔹 Persistent data storage across sessions

🔹 Comprehensive error handling for invalid user inputs

🔹 File handling using JSON, CSV, and TXT formats

🔹 Clean, readable, and well-documented code

📥 Setup & Installation
Prerequisites

Python 3.x installed

Any code editor (VS Code recommended)

Installation Steps
git clone https://github.com/pragy19/PersonalProductivitySuite
cd PersonalProductivitySuite
pip install -r requirements.txt
python main.py

🧠 How Technical Requirements Are Met
Requirement	Implementation
Modular architecture	Separate modules for each tool
File handling	JSON, CSV, TXT
Error handling	try-except blocks
CLI Interface	Menu-driven system
Data persistence	Files saved across sessions
Code quality	Clean, structured, documented
🧪 Testing

✔ Manual testing for all tools

✔ Input validation testing

✔ File path and permission checks

✔ Verified data persistence after restart

🖼 Screenshots

The documentation includes screenshots of:

📋 Main menu

🧮 Calculator usage

📝 Notes manager (Add / View)

⏱ Timer execution

📂 File organizer output

⚠️ Troubleshooting

Issue: FileNotFoundError for data files

Solution: Required directories and files are automatically created at runtime.

Issue: Invalid user input

Solution: User-friendly error messages guide correct input.

🚀 Future Enhancements

🖥 Graphical User Interface (Tkinter)

☁️ Cloud data synchronization

🔐 User authentication

📊 Analytics and productivity reports

📌 Project Option

Option 2 – Standard Version

🔗 Repository & Documentation

GitHub Repository:
👉 https://github.com/pragy19/PersonalProductivitySuite

Project Documentation:
👉 https://drive.google.com/drive/folders/1jTXn22B5IwjVzutEwr_wiDCv2_Um5lDH

📝 Remarks

This project strengthened my understanding of Python programming, modular software design, and real-world application development.
The architecture allows easy scalability, maintainability, and future enhancements.

✅ Ready for Submission

This repository fully satisfies all requirements for Month 1 – Python Programming Mastery 🎉
