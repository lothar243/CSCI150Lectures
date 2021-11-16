Why do we use functions?

* Improving program readability
* Modular program development
* Avoid writing redundant code

Mathematical functions

* In math, functions have a specific meaning
* Use inputs, return output

Calling functions in expressions

* When a function has a return value, you can chain functions together

```python
def areaOfCircle(radius):
    return 3.141592 * r ** 2

print("The area of a circle with radius 3 is {}".format(areaOfCircle(3)))
```

Function stubs

* Incremental development

* `pass` keyword

Functions with branches/loops

Debuggers

# Module 12 Section 2

## Scope

Global variables can be used from anywhere inside the .py file. When a variable is defined outside of any function, it is global

Local variables can be seen/used inside that execution of the function

It is good practice to use the narrowest scope necessary for a variable. This usually means you should be utilizing local variables

Walk through examples of `scopeDemo.py`  

The `global` keyword can be used to make a variable global, as in `explicitGlobal.py`

The `locals()` and `globals()` functions can be used to display all the variables within the local and global namespace, respectively

Scope resolution - first the local namespace is checked, then global, than the built-in namespace`impliedGlobal.py`. If the variable is not found, then the interpreter generates a NameError. Also,  `scopeError.py`

## Function Arguments

Arguments are passed by assignment in Python. If an argument is mutable, it can be changed

This can be overcome by creating a copy and passing that instead, or by using an immutable object

`mutableExample.py`

## Keyword arguments and default parameters

Keyword arguments allow the user to specify a value without keeping to a specific order

```python
 print("hi", "there", "how", "are", "you", sep="_", end="\n\n")
```

Default values for arguments allow the user to not specify a value at all

```python
print("hi", "there", "how", "are", "you")
```

You can create functions with a mix of required and default parameters

```python
def createRow(CRN, title, room="Unassigned", time="TBA"):
    return "{:>6} | {:>20} | {:>7} | {:>7}".format(CRN, title, room, time)

print(createRow(123456, "Intro to CS"))
```

## Docstrings

A docstring is a string literal placed at the first line of a function and the first line of a module. We use triple-quotes to create a multi-line string. This docstring is a good place to put documentation that is necessary for using the functions you create.

The `help()` function will show the relevant docstring, and the function signature, so that a programmer can see what arguments are necessary and review the documentation
