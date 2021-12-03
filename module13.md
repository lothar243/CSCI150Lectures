[YouTube - Socratica - Pomodoro Technique (6:03)](https://www.youtube.com/watch?v=TxdLBxNMbtw)

# Module 13 Section 1 ~ Modular Programming

Modular programming

* Not just dividing programs up into functions, but also modules
* Reusable modules
  * Creating documents that always have the same template
  * Working with specific file types
  * Setting up an environment for working with electronics

# Module 13 Section 2 ~ Strings

## String Slicing

Using a colon with indices give a start and end, called slice notation. note that it stops just before we get to the second listed index

```python
my_str = "Hello, world!"
print(my_str[2])
"l"

my_str[0:3]
"Hel"

my_str[3:7]
"lo, "


```

You can make use of negative indices with slices

```python
my_str[8:-1]
"orld"

my_str[-6:-2]
"worl"
```

If you don't specify one or the other part of the slice, it goes the beginning or end, respectively

```python
my_str[:5]
'Hello'

my_str[3:]
'lo, world!'j

my_str[:]
'Hello, world!'
```

String are immutable, so my_str[0:2] is a new object, and my_str[:] creates a copy

Slice stride, how much to increment the index after reading. it has the default value of 1

```python
my_str[::2]
'Hlo ol!'
```

## Advanced string formatting

"{}".format

In general, the name goes before a colon and formatting instructions go after the colon.

To expand a string to a specified width, you can specify:

* Field width {:10}
* Alignment {:>10}, {<10}, {^10} (right, left, center)
* Fill character {:a<10} would fill with a

You can also format floating point decimals {:.2f}

Combine field size and rounding: {:10.2f}

## String methods

You can `replace` a substring with another string

```python
help(str.replace)
my_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
my_str.replace('l','L',2)
```

Note: this doesn't change the original string (it's immutable)

You can `find` the index of the first occurrence of a substring, possibly specifying the start and the ending positions of where to look (interpreted as slice notation). -1 means the substring doesn't exist

```python
my_str.find('it')
my_str.find('it',20)
```

You can also use `in` to check for the existence of a substring (If you don't care about the index)

You can `count` the number of times a substring occurs. It has optional start and end arguments as well.

```python
my_str.count('it')
```

Comparing strings

Use the `==` operator to check if two strings have the same value.

Inequalities use the ascii values: `"Third" > "Fourth"`

There are additional methods for use with strings. Check the documentation to see a full list

## Splitting and joining strings

`split` creates a list of tokens, separated by a specified substring (default to whitespace - spaces, tabs, newlines, etc)

```python
my_str.split()
my_str.split('it')
```

`join` creates a string from a list, using the specified substring between each of the elements

```python
myList = my_str.split()
outputString = ", ".join(myList)
print(outputString)
# perhaps we don't want the doubled commas
no_commas_string = my_str.replace(",", "")
myList = no_commas_string.split()
outputString = ", ".join(myList)
print(outputString)
```

A common use - parsing numerical input:

```python
input_string = "12, 4, 1, 6, 1, 6, 2345,  2, 4,6"
print("\nParsing the string: '{}'\n".format(input_string))

# We can't just split on ", ", because the spaces aren't generally going to be consistent, so just split on the comma
value_list = input_string.split(",")

print(str(value_list)) # Notice that the spaces are part of the new strings, we could use strip

for i, val in enumerate(value_list):
    value_list[i] = val.strip()
print(str(value_list))

# And of course, we would want to end up with integers. We'll see a nicer way of doing this next week
for i, val in enumerate(value_list):
    value_list[i] = int(val)
print(str(value_list))

# Allright, that looks good
```

