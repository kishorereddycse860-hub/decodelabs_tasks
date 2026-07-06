import string
import secrets

print("===== RANDOM PASSWORD GENERATOR =====")
print("This tool generates a secure random password using letters, numbers, and symbols")

while True:
    length_input = input("Enter password length (minimum 8, recommended 15+): ")
    try:
        length = int(length_input)
    except ValueError:
        print("Invalid input. Please enter a whole number (e.g., 12).")
        continue

    if length < 8:
        print("Password length should be at least 8 characters for basic security.")
        continue

    break

# Define the character pool: letters (upper + lower), digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password using secrets.choice() for cryptographically secure randomness
password = "".join(secrets.choice(characters) for _ in range(length))

print("===== YOUR SECURE PASSWORD =====")
print(password)
print(f"Length: {length} characters")

if length < 15:
    print("Tip: NIST 2024 guidelines recommend at least 15 characters for high-security accounts.")
