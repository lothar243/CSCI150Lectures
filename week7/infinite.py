# This program demonstrates that a program can stay in a while loop
# to validate a user's input

weekdays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

user_day = input("What is the current day of the week? ")

while user_day.lower() not in weekdays:
    print("No really, what day of the week is it? ")

print("{} is a nice day, wouldn't you say?".format(user_day.capitalize()))
