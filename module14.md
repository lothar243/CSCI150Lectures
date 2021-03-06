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

Python has sorting built in. Lists have a sort() method that sorts them in-place, and there is also a sorted function that creates and returns a new list

```python
from random import shuffle
numbers = list(range(10))
id(numbers)
numbers2 = sorted(numbers)
id(numbers2)
numbers.sort()
id(numbers)
```

By default, these sort numbers numerically, and strings alphabetically (by their Ansi values). What if we want to sort by some other criteria? We can use the optional **key** argument

```python
myLists = [[1, 2, 4], [3], [5, 6]]
print(sorted(myLists))
print(sorted(myLists, key=len))
print(sorted(myLists, key=max, reverse=True))
```

## Example

Putting a bunch of this together, we can do quite a bit. Suppose we want to analyze the words in this paragraph

```
mystring = "There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, `Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge."

wordlist = mystring.split()
non_alpha_chars = {character for word in wordlist for character in word if not character.isalpha()}
tr_table = {ord(chr):None for chr in non_alpha_chars}
wordlist = [val.translate(tr_table) for val in wordlist]

# Let's check that this worked
lettersonly = [word.isalpha() for word in wordlist]
all(lettersonly)

# Ok, now lets sort the words
wordlist.sort()

# If I want to ignore capitalization, use lower as a key
wordlist.sort(key=str.lower)

# In fact, let's just get rid of capital letters altogether
wordlist = [word.lower() for word in wordlist]

# What about word frequency? Start by getting each word exactly once
wordset = set(wordlist)
# Now I want their frequency
words_to_frequencies = {word:wordlist.count(word) for word in wordset}

# I can even sort by these frequencies. Dictionaries don't have order, but I can convert it to a list of tuples
word_frequencies = list(words_to_frequencies.items())
word_frequencies.sort(key = lambda x:x[1], reverse=True)

# If you're uncomfortable with lambda functions, you can use the operator.itemgetter function
from operator import itemgetter
word_frequencies.sort(key=itemgetter(1), reverse=True)
```
