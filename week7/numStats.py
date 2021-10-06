# This program demonstrates using a sentinal value with numbers

mylist = []

print("Give me some numbers. I will give you some statistics on them. Enter a zero when you're done")

curr_value = int(input("Give a number: "))
while curr_value != 0:
    mylist.append(curr_value)
    curr_value = int(input("Ok, give me another number: "))

print("The sum of the numbers is {}, their max value is {}, and the min value is {}".format(sum(mylist), max(mylist), min(mylist)))

