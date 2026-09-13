# Loops + Arithmetic
# Prime Number Detector — Ask for a number and determine whether it is prime. Then upgrade it so the user enters a range and your program prints every prime number in that range.
# ⭐⭐⭐

n = int(input("Enter a number: "))

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


if is_prime(n):
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")

num1ofrange = int(input("Enter the starting number of the range: "))
numLoftherange = int(input("Enter the ending number of the range: "))

print("Prime numbers in the range:")
for number in range(num1ofrange, numLoftherange + 1):
    if is_prime(number):
        print(number)