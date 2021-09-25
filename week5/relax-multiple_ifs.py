# This is a simple program that will tell the user to relax if it is currently the weekend or the evening
WEEKEND_DAYS = ['sunday', 'saturday']


# First, gather the input about the day and time
weekday = input("What day of the week is it? (Example: Sunday): ")
hour = int(input("What hour is it? (Example: 2): "))
morning_or_afternoon = input("Was that am or pm? ")

# Test to see if they should relax
if (weekday.lower() in WEEKEND_DAYS) or ((hour >= 5) and morning_or_afternoon == 'pm'):
    print("You should get some rest and relax")
else:
    print("Why are you messing around with this program - you should get to work!")
