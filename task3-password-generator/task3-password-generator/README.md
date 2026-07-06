# Task 3: Random Password Generator

A command-line tool that generates a secure, random password based on user-defined length.

## Features
- Prompts the user for a desired password length
- Validates input to ensure it's a number and at least 8 characters
- Uses the `secrets` module for cryptographically secure randomness
- Combines letters (upper + lower), digits, and symbols for complexity
- Warns the user if the password is shorter than the NIST-recommended 15 characters

## How to Run
python password_generator.py

## How it Works
1. Enter the desired password length when prompted
2. The program validates that the input is a whole number and at least 8 characters
3. A character pool is built using the `string` module (letters, digits, punctuation)
4. `secrets.choice()` randomly and securely selects characters from the pool
5. The password is assembled using `.join()` for efficiency and displayed

## Example
===== RANDOM PASSWORD GENERATOR =====
This tool generates a secure random password using letters, numbers, and symbols
Enter password length (minimum 8, recommended 15+): 16
===== YOUR SECURE PASSWORD =====
xT9$mQ2!zR7&pL4@
Length: 16 characters

## Industry Standard Reference
This project follows NIST 2024 guidelines, which prioritize password length over forced complexity, recommending at least 15 characters for high-security contexts.

## Tech Used
- Python 3 (`string` module, `secrets` module, list comprehension, `.join()`)
