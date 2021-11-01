# Module 10.1 ~ Functions

[YouTube - Socratica - Feynman Technique (5:44)](https://www.youtube.com/watch?v=q-16DPh_VWw)

Studying tips

* Ask the 'right questions' (Yourself, as well as others)
  * Varies by person
  * Depends on what you're having troubles understanding (Dictionaries, Lists, Loops)
  * Explain these topics to someone else. Topics that you can't explain are topics you need to spend more time on

* Don't just stop when it works
  * Your goal is not the functioning program, but rather the understanding
  * These programs are tools we're using for you to learn
* Seek additional challenges
  * The programs that are assigned are likely not enough for everyone

## Functions

A function is a named sequence of instructions. To define a function:

* Use the `def` keyword
* Give the function a name - lowercase (according to style guide, underscores or camelCase for multiple words)
* Zero or more inputs, called parameters, go inside parentheses
* End the line with a colon
* A string called a docstring typically follows the definition line, giving a description of the function. This is used to auto-generate documentation
* Any commands to be executed when the function is called are indented

```python
# An example of a function with no input and no output
def print_header():
    """Prints a header, greeting the customer"""
    print("Hello, and welcome to the system")
```

Functions are placed toward the beginning of your file, just after any import statements

Function definitions are not executed when they are encountered. Instead, the function is called by putting the name of the function with parentheses after it

```python
print_header() # This would call the print_header function
```

Suppose we want to specify an input. We declare that this function has a parameter,

```python
# An example of a function with no input and no output
def print_header(username):
    """Prints a header, greeting the customer."""
    print("Hello {}, and welcome to the system".format(username))
```

And then we pass the value of that parameter in as an argument for the function call

```python
print_header("Jeff") # Prints the header for the username Jeff
```

When we call a function, we can also return a value to where the function was called by using the `return` keyword. As soon as the return keyword is encountered, the program continues from where the function call was made. Any object can be returned

```python
def prompt_to_continue():
    """Prompts the user if they would like to continue.
    Returns either 'y' or 'n'"""
    user_input = input("Would you like to spin again? (y/n)")
    while not (user_input == 'y' or user_input == 'n'):
        user_input = input("Unrecognized input. Would you like to spin again? Please enter 'y' or 'n'")
    return user_input
```

This would be called the same way as before, but now it returns a value, so we should store that value. If we define `spin_wheel()` elsewhere, then our main loop could be reduced to

```python
continue = 'y'
while continue == 'y':
    spin_wheel()
    continue = prompt_to_continue()
```

We use functions when we have a complicated task that can be broken into smaller tasks. These smaller tasks become functions, allowing the larger task to be more readable. It is also very handy to prevent code repetition.

[YouTube - Socratica - Python Functions (9:27)](https://www.youtube.com/watch?v=NE97ylAnrz4)

The use of functions enables us to treat parts of our code as individual modules, which allows us to swap out parts for improved functionality

Example

```bash
vim MushnikMenu.py
```

[YouTube - Socratica - Python and Prime Numbers (6:01)](https://www.youtube.com/watch?v=2p3kwF04xcA)

# Module 10.2 ~ 

Walk through examples on the Moodle page

