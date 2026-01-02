# 1. Create variables
my_integer = 100
my_float = 3.14
my_string = "Python"
my_boolean = True
my_list = [1, 2, 3]

# 2. Check their types
print("--- Type Checking ---")
print(type(my_integer))
print(type(my_float))
print(type(my_string))
print(type(my_boolean))
print(type(my_list))

# 3. Explicit Type Conversion (Casting)
print("\n--- Casting ---")
original_pi = 3.14
integer_pi = int(original_pi) # Converts 3.14 to 3
string_pi = str(original_pi)  # Converts 3.14 to "3.14"

print(f"Original: {original_pi}")
print(f"As Integer: {integer_pi}")
print(f"As String: {string_pi}")