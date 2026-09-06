# 1. Conditionals + Loops
# Number Analyzer — Ask the user for 10 numbers. At the end, display how many were positive, negative, zero, even, and odd. Also display the largest and smallest number. Do not use max() or min().
# ⭐⭐


numbers=[]
for i in range(5):
    number=int(input("Enter a number: "))
    numbers.append(number)
print(numbers)

posnum=0
negnum=0
zernum=0

for i in range(5):
    if numbers[i] > 0:
        posnum+=1

    elif numbers[i] < 0:
        negnum+=1
    else:
        zernum+=1

print("There are",posnum,"Positive Numbers,",negnum,"Negative Numbers, and",zernum,"Zero Numbers in the list.")
