menuitems = ['Burger', 'Cheeseburger', 'Fries', 'Drink']

print("Welcome to the shop, we have all sorts of items")
for menuitem in menuitems:
    print(menuitem)

print()
userchoice = input("What would you like? ")

if userchoice in menuitems:
    print("Sure thing, we can get you: " + userchoice)
else:
    print("I'm sorry, I we don't have any: " + userchoice)


