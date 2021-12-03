# Module 14 ~ Lists

## Lists

Lists can be defined by using brackets. They act as a container and can hold other objects. You use brackets with indices to reference objects in the list

```python
mylist = [5, 1, 2]
mylist2 = ['a', "Test", 3.15]
type(mylist)
type(mylist[0])
type(mylist2[2])
```

They are mutable

```python
mylist[0] = 'asdf'
print(mylist)
mylist3 = mylist
mylist3.append('a change')
# what will happen to mylist?
```

You can even have lists of lists

```python
mylist.append(mylist2)
print(mylist)
type(mylist[4])
```

You can create lists from any iterable object

```python
numbers = list(range(10))
```

## List Methods

Adding two lists combines them, note that this doesn't change either of the original lists.

If you want to add a list to another, either assign this sum, or use extend

```python
print(mylist + numbers)
print(mylist)
print(numbers)
mylist.extend(numbers)
print(mylist)
```

You can remove elements from a list by using pop or remove

```python
poppedItem = mylist.pop() # by default this remove and returns the last item of the list
poppedItem = mylist.pop(1) # but you can specify which index to pop
mylist.remove(4) # alternatively, you can remove an item with a specific value
```

You can sort the list in place, or reverse the list in place

```python
import random
random.shuffle(numbers)
numbers.reverse()
numbers.numbers() # note that you can't sort mylist because there is no way to compare some of the object types
```

You can also use index() or count() to find out about the list

```python
random.shuffle(numbers)
numbers.index(4)
numbers.count(1)
```

## Iterating over a list

There are several ways to iterate over a list, if you are just interested in the values just use for... in

```python
for value in numbers:
    print(value)
```

If you want the index in addition to the value, use enumerate

```python
for i, val in enumerate(mylist):
    print("{}: {}".format(i, val))
```

It is also common for you to want to iterate with just the index

```python
for i in range(len(mylist)):
    print(i)
```



## List Slicing

Just like strings, you can slice lists

```python
numbers[2:5]
numbers[:-1] # gives a copy of the list without the last item
numbers[::2] # specifies the stride to be every other item
numbers[::-1] # gives a copy of the list in reverse order
numbers[:] # gives a copy of the list
```

# Module 14 Section 2 ~ More Lists

## Loops modifying lists

Common errors:

```python
numbers = [5, 8, 4, 6, 0, 7, 2, 3, 9, 1]

## Why doesn't the following work? ##
print(numbers)

# Subtract one from each value in the list
for val in numbers:
    val = val - 1

print(numbers)
```

How could you fix this?

```python
numbers = [5, 8, 4, 6, 0, 7, 2, 3, 9, 1]

## Why doesn't the following work? ##
print(numbers)

# Remove all items from the list that are less than 5
for val in numbers:
    if val < 5:
        numbers.remove(val)

print(numbers)
```

How would you fix it?

## List Comprehension

Suppose you want to create a list of 10 random numbers, how could we go about this?

```python
import random

numbers = []
for _ in range(10):
    numbers.append(random.randrange(20))
```

List comprehension allows us to create some lists on a single line

```python
import random

numbers = [random.randrange(20) for _ in range(10)]
```



[YouTube - Socratica - List Comprehension (7:42)](https://www.youtube.com/watch?v=AhSvKGTh28Q)



## Sorting lists

