# Module 5 Section 1

## 4.5 Detecting ranges using logical operators

### Logical AND, OR, and NOT

[YouTube - Socratica - Python Booleans (4:39)](https://www.youtube.com/watch?v=9OK32jb_TdI)

Truth tables

Order of operations

0 < x < 40 vs 0 < x and x < 40

How to test if x is outside of this range?

* not (0<x<40)
* not(0 < x) or not(x < 40)

boolean can take on two values, True or False (note the capitalization)

Examine the following

```python3
5 < 5
5 <= 5
not 5 < 5
5 != 5
```

```shell
python3 logic_operators.py
```

## 4.6 Detecting ranges with gaps

If it's the weekend or after 5, we can relax

```python3
python3 relax-multiple_ifs.py
```

## 4.7 Detecting multiple features with branches

[Youtube - Computer Science - Nested If Statements - 10:30](https://www.youtube.com/watch?v=VGsuGhBPD4s)

```shell
pudb3 priceIsRight-nestedIfs_and_elifs.py
```

# Module 5 Section 2

min, max, sum functions

## Section 2 Branching

### 4.8 - Comparing data types and common errors

Floating point rounding error

```python3
3 * 1.2
```

Don't compare floating point numbers with ==, instead use a small range

What does it mean to compare 'a' < 'd'? How about `'abc' < 'ABC' `?

`ord('a')` and `ord('A')`

### 4.9 - Membership and identity operators

The `in` and `not in` operators

```python3
mylist = [1, 2, 'a', 'qwer']
1 in mylist
3 in mylist
'a' not in mylist
'q' in mylist
'qwer' in mylist
'w' in 'qwer'
'w' in mylist
```

```python3
class_to_roomnum = {
"csci150":"mc227",
"m090":"mc235", 
"csci240":"mc025"
}
print(class_to_roomnum["csci150"])
'm090' in class_to_roomnum
'm090' in class_to_roomnum.keys()
'mc235' in class_to_roomnum
'mc235' in class_to_roomnum.values()
class_to_roomnum.keys()	  # also view .values(), and .items()
```

Pre-made example:

```shell
python3 menuitems.py
python3 menuitemsprices.py
```

The `is` and `is not` operators - checks to see if two things are the same object

```python3
mylist1 = [1, 2]
mylist2 = [1, 2]
mylist3 = mylist1
mylist1 == mylist2
mylist1 is mylist2
mylist1 is mylist3
mylist1.append(3)
mylist1
mylist2
mylist3
```

### 4.10 - Order of evaluation

[YouTube - Appficial - Python Order of Operations - (2:52)](https://www.youtube.com/watch?v=fmD0ZAi8SFk)

### 4.11 - Code blocks and indentation

## Section 2 Labs

### 4.15 Golf Scores

### 4.16 - Leap year

Reminder: `year_num % 4 == 0` is true when `year_num` is divisible by 4

### Additional content

Show image manipulation with the PIL module

```shell
vim imageEditing.py
```

