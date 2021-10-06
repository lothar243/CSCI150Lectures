# This is an example of using a while loop to validate user input

usernum = int(input("Give me a number between 1 and 10: "))

while not 1 <= usernum <= 10:
    usernum = int(input("That isn't between 1 and 10, try again: "))

print("All right, you chose {}".format(usernum))
