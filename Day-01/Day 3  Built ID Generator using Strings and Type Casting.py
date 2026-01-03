# Day 3 Project: The ID Card Generator
# This program demonstrates String methods and Type Conversion

# 1. CONSTANTS (Variables that don't change)
CURRENT_YEAR = 2026

print("--- Welcome to the ID Generator ---")

# 2. INPUTS (Getting raw data)
# We expect the user might be messy (e.g., "  saHIL  ")
raw_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year (YYYY): ")
height_str = input("Enter your height in cm (e.g., 175.5): ")

# 3. PROCESSING (Cleaning and Converting)

# String Chaining: We do .strip() AND .title() in one line!
# "  saHIL  " -> "saHIL" -> "Sahil"
clean_name = raw_name.strip().title()

# Type Conversion: String -> Integer (Whole number for year)
birth_year = int(birth_year_str)
age = CURRENT_YEAR - birth_year

# Type Conversion: String -> Float (Decimal number for height)
height = float(height_str)

# Creating a username (String Manipulation)
# We take the first 3 letters using slicing [0:3] and make them lowercase
username = clean_name[0:3].lower() + str(birth_year)

# 4. OUTPUT (The F-String Report)
print("\n" * 2) # Print 2 empty lines for spacing
print("=================================")
print(f"OFFICIAL ID CARD: {CURRENT_YEAR}")
print("=================================")
print(f"Name:      {clean_name}")
print(f"Username:  {username}")
print(f"Age:       {age} years old")
print(f"Height:    {height} cm")
print(f"Name Length: {len(clean_name)} characters")
print("=================================")