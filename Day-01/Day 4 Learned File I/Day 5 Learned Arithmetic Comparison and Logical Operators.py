# Day 5: Operators Mastery (Safe Version)
# Topics: Arithmetic, Comparison, Logic, and Error Handling

print("--- 🧮 THE NUMBER ANALYZER 🧮 ---")

# 1. Get Inputs (Using float so decimals work)
# We use a try/except here too, just in case they type "abc" instead of a number!
try:
    x = float(input("Enter first number (x): "))
    y = float(input("Enter second number (y): "))
except ValueError:
    print("❌ Error: You must enter a number!")
    # We set default numbers so the program doesn't crash later
    x = 1.0
    y = 1.0

print(f"\nAnalyzing numbers: {x} and {y}...")

# 2. Arithmetic Operators (Math)
print("\n--- 🔢 MATH RESULTS ---")
print(f"Plus (x + y):      {x + y}")
print(f"Minus (x - y):     {x - y}")
print(f"Times (x * y):     {x * y}")

# SAFETY SHIELD 1: Division by Zero protection
if y != 0:
    print(f"Divide (x / y):    {x / y}")
    print(f"Remainder (x % y): {x % y}")
    print(f"Floor Div (x // y):{x // y}")
else:
    print("Divide:            Cannot divide by Zero! 🚫")

# SAFETY SHIELD 2: Overflow protection (The fix for your crash!)
try:
    power = x ** y
    print(f"Power (x ** y):    {power}")
except OverflowError:
    print("Power:             Result too large to calculate! 💥")


# 3. Comparison Operators (True/False)
print("\n--- ⚖️ COMPARISONS ---")
print(f"Is x greater than y? {x > y}")
print(f"Is x equal to y?     {x == y}")
print(f"Is x NOT equal to y? {x != y}")


# 4. Logical Operators (The 'Brain')
print("\n--- 🧠 LOGIC CHECKS ---")

# Check if both are positive numbers
is_both_positive = (x > 0) and (y > 0)
print(f"Are both positive?   {is_both_positive}")

# Check if x is Even (using Modulus)
# We convert to int() temporarily because even/odd is for whole numbers
if int(x) % 2 == 0:
    print(f"Is x an Even number? True")
else:
    print(f"Is x an Even number? False")

print("\n---------------------------------")
print("Analysis Complete.")