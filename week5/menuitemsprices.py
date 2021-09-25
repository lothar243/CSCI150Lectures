menuitems = {'Burger':4.99, 'Cheeseburger':5.99, 'Fries':2.99, 'Drink':1.49}

print("Welcome to the shop, we have all sorts of items")
for menuitem, price in menuitems.items():
    print("{:10} ${:.2f}".format(menuitem, price))

print()
userchoice = input("What would you like? ")

if userchoice in menuitems.keys():
    print("Sure thing, we can get you: {}".format(userchoice))
    print("It costs ${:.2f}".format(menuitems[userchoice]))
else:
    print("I'm sorry, I we don't have any: " + userchoice)


