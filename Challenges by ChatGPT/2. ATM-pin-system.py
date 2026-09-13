# While Loop + Validation
# ATM PIN System — Store a PIN such as 4321. Give the user only 3 attempts. Correct PIN → "Access Granted". Wrong PIN → show attempts remaining. After 3 failures → "Card Blocked".

pin=4321
attempt=3

print("Note: You have only 3 attempts to Enter the Correct pin!")
print("")

pin_of_user=0

while attempt>0 and pin_of_user!=pin:
    pin_of_user=int(input("Enter the PIN: "))
    if pin_of_user!=pin:
        attempt-=1
        print("Oops! You have",attempt,"left.")
        if attempt==0:
            print("Your Account has been blocked.")
        else:
            print("Try Again!")
