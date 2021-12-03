numbers = [5, 8, 4, 6, 0, 7, 2, 3, 9, 1]

## Why doesn't the following work? ##
print(numbers)

print("Remove all items from the list that are less than 5")
for val in numbers:
    if val < 5:
        numbers.remove(val)

print(numbers)
