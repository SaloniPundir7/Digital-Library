# 📚 Digital Library Project

## Overview
Digital Library is a Python program to manage, search, and open digital content like books, audiobooks, and articles. The program stores all library data in `library.json` and allows users to view, search, and open files based on their access type (`user` or `admin`).

## Features
- View all files (metadata only or full details)  
- Search files by **title**  
- Search files by **genre**  
- Open files:
  - `.txt` → read in terminal  
  - `.docx` → read in terminal or open in Word  
  - `.pdf` → open in default PDF viewer  
  - `.mp3` / `.wav` → open in default media player  
  - Web URLs → open in browser  
- User/Admin access control  
- Persistent library storage in `library.json`  

## Setup
1. Install Python 3.x  
2. Install required package:
   pip install python-docx

## Usage

1. Navigate to the Digital Library folder

2. Run the program:

   python main.py


3. Enter your access type: user or admin

Use the menu options displayed in the program:

1. View all files (metadata only)
2. Search by title
3. Search by genre
4. Open a file
5. Exit


4. Follow prompts:

a. If you select View all files, you can see full metadata and choose to open a file.

b. If you select Search by title or Search by genre, matching files will be displayed, and you will be prompted to open them.

Open a file allows you to directly open a file by its number from the library list.

## Adding New Files Example
from main import files, save_library, load_library

library = load_library([])

new_book = files(
    name="Python for Everyone",
    category="Book",
    genre=["Education", "Programming"],
    price=25,
    rating=4.7,
    access_type="user",
    writer="John Doe",
    file_path="PythonForEveryone.docx"
)

library.append(new_book)
save_library(library)

## Notes

a. Files must exist or have a valid path

b. Unsupported files are handled gracefully

c. The program ensures that even a new user can run, search, and open files without guidance
