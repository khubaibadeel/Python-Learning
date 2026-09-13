# 1. Conditionals + Loops
# Number Analyzer — Ask the user for 10 numbers. At the end, display how many were positive, negative, zero, even, and odd. Also display the largest and smallest number. Do not use max() or min().
# ⭐⭐


numbers = []

for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

print(numbers)

posnum = 0
negnum = 0
zernum = 0

for number in numbers:
    if number > 0:
        posnum += 1
    elif number < 0:
        negnum += 1
    else:
        zernum += 1

print(
    "There are", posnum,
    "positive numbers,", negnum,
    "negative numbers, and", zernum,
    "zero numbers in the list."
)

evenum = 0
oddnum = 0

for number in numbers:
    if number % 2 == 0:
        evenum += 1
    else:
        oddnum += 1

print("Moreover, there are",evenum,"even numbers and",oddnum,"odd numbers in the list.")

largest = numbers[0]
for number in numbers[1:]:
    if number > largest:
        largest = number

print(largest, "is Largest")

smallest = numbers[0]
for number in numbers[1:]:
    if number < smallest:
        smallest = number

print(smallest, "is Smallest")