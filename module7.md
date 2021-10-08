# Module 7.1 - While Loops

Input verification - how can we ensure that a user gives us acceptable input?

An if statement will execute a particular block at most once

A while loop - keep executing as long as an expression keeps evaluating to True

```bash
vim weekdayQuestion.py
vim giveNumber.py
```

Be careful not to get stuck in an infinite loop

```bash
vim infinite.py
```

This can also be used to repeat something as many times as a user would like

```bash
vim guessingGame.py
vim numStats.py
```

Reminder: Compound arithmetic operators +=, -=, *=, /=: Perform both the arithmetic and assignment

```bash
vim increment.py
```

While loops work well when we want to repeat something but we're not sure how many times

```bash
vim powerOfTwo.py
```

When it is known how many times we want to iterate, for instance if we know we want to loop through the numbers 1-20, we tend to use `for` loops (next class)

# Module 7.2 - For loops

For loops are a good way to loop through every object in a container

```python3
for element in container:
    statement to do for each element
```

Examples:

```bash
loopList.py
loopDict.py
loopSet.py
```

You can instruct Python to loop through the container in a particular order by using `.sorted()` or `.reversed()`

```bash
vim loopSortedSet.py
```

This is in addition to the ability to sort lists, but it doesn't change the order of the original item

You can generate a sequence of numbers using the `range()` function

```python3
for element in range(start, end, step):
    statements to be repeated
```

Examples:

```bash
vim rangeExample.py
```

When to use while loops, vs when to use for loops

Iterating through something a predictable number of times, or through every element in a container -> for loops

Iterating an unknown number of times, or until the user gives a particular input -> while loops

In reality, either of these could work for either situation, but tends to be the easiest and most clear
