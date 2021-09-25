[YouTube - Computer Science - ASCII and Unicode Character Sets - 12:48](https://www.youtube.com/watch?v=I-pQH_krD0M)

# Module 4 Section 1

## 3.7 Type conversions

* implicit conversions – done automatically, 1 + 2.1, 2 * 0.5

  print(2)

  print(mylist)

* explicit conversions – written in code

  `int(2)`		does nothing

  `float(2)`	2.0

  `float(5.6)`	does nothing

  `int(5.6)`	will truncate the part after the decimal

  `str(2.1)`		convert to string

  convert between tuple, list, set

  ```python
  mylist = ['first', 'second', 'third'], tuple(mylist)
  ```

## 3.8 Binary numbers

[YouTube - Computer Science - Binary 1](https://www.youtube.com/watch?v=cJNm938Xwao)

counting in decimal, digits used, place value $10^0$, $10^1$, etc

counting in binary, bits used, place value $2^0$, $2^1$, etc

powers of 2

convert 0b00001111 to a decimal number (by hand, by the calculator, and in python)

convert 0d51 to a binary number (by hand, by calculator, and in python `bin(51)` )

1 byte = 8 bits

why do we use binary? These indicate on or off values

counting in hexadecimal

convert 0x3a to decimal (by hand, calculator, and in python)

convert 632 to hex (by hand, calculator, and in python `hex(632)`)

why do we use hex?

* easier to write
* two characters represent one byte
  * example: `xxd /bin/sh | head`, or other file

## 3.9 String formatting

placeholder surrounded by curly braces is called a replacement field

values inside format() are inserted into the replacement field

```python
number = 6
cost = 32
print('{} burritos cost ${}'.format(number, cost))
```


inferred positional replacement

```python
'The {} in the {} is {}.'.format('cat', 'hat', 'fat')
```

positional replacement

```python
'The {1} in the {0} is {2}.'.format('hat', 'cat', 'fat')
```

named replacement

```python
'The {animal} in the {headwear} is {shape}.'.format(animal='cat', headwear='hat', shape='fat')
```

you cannot combine positional with inferred positional replacement, but named replacement can be combined with either of the other two

```python
'{first} + {} is {sum}'.format(2, first = 3, sum = 5)
```

double braces can be used to place an actual curly brace in a string

```python
'{0} {{Bezos}}'.format('Amazon')  produces “Amazon {Bezos}”
```


Common formatting specifications

* s – string (default)
* d – decimal			‘{:d}’.format(4)
* b – binary
* x, X – Hexadecimal in lowercase or uppercase
* e – exponential notation
* f – fixed-point notation (6 places of precision)
	* .2f – fixed-point notation (programmer-defined)
	* 10.4f – fixed-point notation (4 places of precision, 10 spaces total)

# Module 4 Section 2 - Branching

## 4.1 – If-else branches
[YouTube - Computer Science - If Statements - 6:31](https://www.youtube.com/watch?v=CF38ghVEywQ)

Do one thing under these conditions, otherwise do this other thing

If x  < 10, print “it was smaller than 10”, x = 11, else print “it was at least 10”

## 4.2 – if-else statements

if …: (python style calls for an indent of 4 spaces)else:

```python
price = float(input("How expensive is this meal?"))
if price < 10:
    print("I will buy it")
```

else:

```python
else:
    print("No, it's too expensive")
```

difference between < <= > >=

equality operator ==

```shell
pudb3 branchingExample.py
```

elif:

```shell
pudb3 computeLatePenalty-elifExample.py
```

what happens if the value changes midway through?

```shell
pudb3 changeMidway.py
```

## 4.3 - More if-else

Multiple if statements can each evaluate independently

```shell
pudb3 carAge.py
```

## 4.4 - Equality and Relational Operators

[YouTube - Computer Science - Relational Operators - 5:21](https://www.youtube.com/watch?v=A9GbS1ZL_OE)

boolean - two values: True and False

==, <, <= etc all return boolean values

!= is used for 'not equal to'

* and

* or

We'll see more of 'and' and 'or' next time
