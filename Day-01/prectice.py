# --- LEVEL 1: The ID Card ---
username = "Your Name"  # Replace with your actual name
age = 25                # Replace with your actual age
is_student = True

print("--- ID Details ---")
print(username)
print(age)
print(is_student)


# --- LEVEL 2: The Swap Logic ---
print("\n--- Swapping Logic ---")
glass1 = "Milk"
glass2 = "Juice"

print(f"Before Swap: glass1={glass1}, glass2={glass2}")

# Your Solution (The Temporary Variable Logic)
glass3 = glass1
glass1 = glass2
glass2 = glass3

print(f"After Swap:  glass1={glass1}, glass2={glass2}")


# --- LEVEL 3: Correct Variable Naming ---
print("\n--- Corrected Names ---")
# Fixed from: 1st_Place, My Name, class
First_Place = "Gold"
My_Name = "John"
class_ = "Science" 

print(First_Place)
print(My_Name)
print(class_)


# --- LEVEL 4: Data Types ---
print("\n--- Data Types Check ---")
mystery_1 = 5
mystery_2 = "5"

# mystery_1 is an Integer (number)
print(f"Type of mystery_1: {type(mystery_1)}")

# mystery_2 is a String (text)
print(f"Type of mystery_2: {type(mystery_2)}")