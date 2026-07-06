total = 0  
count = 0

print("===== EXPENSE TRACKER =====")
print("Enter an expense amount to add it to your total")
print("Type 'done' when you want to stop and see your total")

while True:
    raw_value = input("Enter expense amount (or 'done' to finish): ")

    if raw_value.lower() == "done":
        break

    try:
        expense = float(raw_value)
    except ValueError:
        print("Invalid input. Please enter a number (e.g., 100 or 50.5).")
        continue

    total += expense
    count += 1
    print(f"Added ${expense:.2f}. Running total: ${total:.2f}\n")

print("===== SUMMARY =====")
print(f"Total expenses entered: {count}")
print(f"Total Spent: ${total:.2f}")
