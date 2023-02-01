# tech201_functions
# functions


### create a function


```# def print_something():
#     print("something has been printed ") #hard coded not re-useable
#
#
# print_something()
```
## Functions and arguments
```` python
# def print_something(print_string): #make sure argument gives context
#     print(print_string)
#
# print_something("this is my variable")
#
# print_something("this is my second time calling tis funvtion")
``````
#### in java:
##### public void print_string(string_text)

```` python
# def greetings(name):
#     print("Hello, my name is" + name)
#
# greetings(" luke")
# greetings(" waleed")
````

## THE RETURN STATEMENT
```` python
# def addition(int1, int2):
#   return int1 + int2
#
# print(addition(2, 2))
````
```` python
#Default arguments
  #set your defult in your argument
```# def addition(int1=2, int2=2):
#     return int1 + int2
# print(addition())
# print(addition(10, 10))
````
## Multiple arguments
```` python
# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
````
# Type Hints
```` python
# def greeting(name): str):
#     print("hello my name is" + name)
# greeting()
````
```` python
# def division(num1: int = 2, num2: int = 2) -> float:
#     return num1 / num2
# print(division())
````

# Calculator Task 
```` python
def add(a=5, b=10):
    return a + b
print(add())
````
The first function, add, is defined to take two arguments a and b, both with default values of 5 and 10, respectively. The function returns the sum of a and b.
```` python
def subtract(a, b):
    return a - b

print(subtract(5, 10))
````
The second function, subtract, is defined to take two arguments a and b. The function returns the difference of a and b.

In the second print statement, the subtract function is called with arguments 5 and 10. The function returns the difference of these values, which is -5, and this value is printed.
```` python
def multiply(a=5, b=10):
    return a * b

print(multiply())
````
The third function, multiply, is defined to take two arguments a and b, both with default values of 5 and 10, respectively. The function returns the product of a and b.

In the third print statement, the multiply function is called without any arguments. Since a and b both have default values, their product, 50, is returned and printed.

```` python
def divide (a=5, b=10):
    return a / b

print(multiply())
````
The fourth function, divide, is defined to take two arguments a and b, both with default values of 5 and 10, respectively. The function returns the division of a by b.

In the fourth print statement, the multiply function is called by mistake instead of the divide function. As a result, the product of a and b is returned and printed, which is 50.
    















# Functions best practices 

- Name your functions clearly using lowercase and underscores 
- ALL argumentss should be cclear in their needs and where possible include their expected type
- remebember the return statement or your function will return none
- keep functions small to preserve readability and simplicity 
- use comments in your functions/methods to give instructions on how to use them
- Consider using type hints to avoid type errors when ypu run your code.