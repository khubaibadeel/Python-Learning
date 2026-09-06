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

evenum=0
oddnum=0
nothing=0
for i in range(5):
    if (numbers[i]%2==0 and numbers[i]!=0):
        evenum+=1
    elif(numbers[i]%2!=0 and numbers[i]!=0):
        oddnum+=1
    else:
        nothing+=nothing
        
print("Moreover, there are",evenum,"Even Numbers and",oddnum,"Odd Numbers in the list.")

others=numbers[1]
for i in range(10):
    if numbers[0]>others:
        print(numbers[0],"is Largest")