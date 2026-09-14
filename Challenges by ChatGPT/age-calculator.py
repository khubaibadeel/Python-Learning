# Data Types + Type Conversion
# Age Calculator: Input birth year and calculate approximate age. Then print the data type of the input before and after conversion.
# ⭐

birthyear = input("Enter your Birthyear: ")
print(type(birthyear))
birthyear = int(birthyear)
print(type(birthyear))
print("Your Estimated age is", 2026 - birthyear)