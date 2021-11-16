def changeOrder(myList):
    temp = myList[0]
    myList[0] = myList[1]
    myList[1] = temp


testList = [1, 2, 3, 4, 5]
print("Before calling the function, the list is: {}".format(testList))
changeOrder(testList)
print("After calling the function, the list is: {}".format(testList))
print("Test list was modified in-place")
input("Press enter to do this again, but with a copy")

testList = [1, 2, 3, 4, 5]
print("Before calling the function, the list is: {}".format(testList))
changeOrder(testList[:])
print("After calling the function, the list is: {}".format(testList))
input("Press enter to do this again, but with a tuple")

testTuple = (1, 2, 3, 4, 5)
print("Before calling the function, the tuple is: {}".format(testList))
changeOrder(testTuple)
print("After calling the function, the tuple is: {}".format(testList))
