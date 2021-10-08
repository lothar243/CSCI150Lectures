
print("Note that for loops always stop as they reach the stop number")

print("\nYou can count up to 5 (5 lines total)")
print("for index in range(5) gives")
for index in range(5):
    print(index)

print("\nYou can count from 2 to 5 (3 lines total)")
print("for index in range(2, 5) gives")
for index in range(2, 5):
    print(index)

print("\nYou can count from 3 to 15 with step size 4")
print("for index in range(3, 15, 4) gives")
for index in range(3, 15, 4):
    print(index)

print("\nIf the index doesn't hit exactly, this isn't a problem")
print("Counting from 3 to 16 with step size 4")
print("for index in range(3, 16, 4) gives")
for index in range(3, 16, 4):
    print(index)

print("\nYou can even count backwards")
print("for index in range(6, 2, -1) gives")
for index in range(6, 2, -1):
    print(index)
