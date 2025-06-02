# python_assignment_4

This repository contains two Python programs focused on file handling operations, including reading from files, handling errors, writing to files, and appending data.

## Files Included

- `task1.py` - Read a file and handle errors.
- `task2.py` - Write and append data to a file, and display the final content.

---

## Task 1: Read a File and Handle Errors

**Problem Statement:**  
Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

**Code Summary:**
- Uses `try-except` to catch `FileNotFoundError`.
- Reads each line from the file and prints with line numbers.

**Example Output:**
Reading file content:
Lines 1 : This is a sample text file.
Lines 2 : it contains multiple Lines.

---

## Task 2: Write and Append Data to a File

**Problem Statement:**  
Write a Python program that:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

**Code Summary:**
- Takes initial input and writes to `output.txt`.
- Takes another input and appends it to the file.
- Displays the final content of the file.

**Example Output:**
Enter text to write to the file: Rushikesh Phatak
Data successfully written to output.txt.
Enter additional text to append: I Like to Learn python language And Explore.  
Data successfully appended.

Final content of output.txt:
Rushikesh Phatak
I Like to Learn python language And Explore. 

---

## 📌 How to Run

Open terminal or command prompt and run:
```bash
python task1.py
python task2.py

