# This program displays all powers of 2 up to the user supplied value

print("This program displays all powers of 2 up to a number you specify")
cutoff = int(input("What number would you like to keep going until? "))


powerOfTwo = 1 # Start at 2^0 = 1

while powerOfTwo <= cutoff:
    print(powerOfTwo, end=" ")
    powerOfTwo *= 2

print()
