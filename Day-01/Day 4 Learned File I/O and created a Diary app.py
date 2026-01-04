# Day 4: File Input/Output (I/O)
# Project: The Persistent Diary

import datetime

# 1. Get the current date and time
current_time = datetime.datetime.now()
# Format it nicely (e.g., "2026-01-04 14:30")
date_str = current_time.strftime("%Y-%m-%d %H:%M")

print(f"--- Diary Entry for {date_str} ---")

# 2. Get Input from the user (Console I/O)
entry = input("Dear Diary, what happened today? ")

# 3. Write Output to a file (File I/O)
# We use "a" (Append) so we don't delete old entries!
with open("my_diary.txt", "a") as file:
    file.write(f"\n[{date_str}]\n")
    file.write(f"{entry}\n")
    file.write("-" * 20) # Adds a separator line

print("\nSaved to 'my_diary.txt' successfully!")

# 4. Read it back to verify (Input from File)
print("\n--- Your Full Journal So Far ---")
with open("my_diary.txt", "r") as file:
    print(file.read())