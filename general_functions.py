# functions

# D R Y
# dont repeat yourself

# create a function

#define
# def print_something():
#     print("something has been printed ") #hard coded not re-useable
#
#
# print_something()

## Functions and arguments

# def print_something(print_string): #make sure argument gives context
#     print(print_string)
#
# print_something("this is my variable")
#
# print_something("this is my second time calling tis funvtion")
#
# # in java:
# public void print_string(string_text)


# def greetings(name):
#     print("Hello, my name is" + name)
#
# greetings(" luke")
# greetings(" waleed")


##THE RETURN STATEMENT

# def addition(int1, int2):
#   return int1 + int2
#
# print(addition(2, 2))

#Default arguments
  #set your defult in your argument
# def addition(int1=2, int2=2):
#     return int1 + int2
# print(addition())
# print(addition(10, 10))

##Multiple agruments

# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Type Hints

# def greeting(name): str):
#     print("hello my name is" + name)
# greeting()


# def division(num1: int = 2, num2: int = 2) -> float:
#     return num1 / num2
# print(division())

# Functions best practices

##Name your functions clearly using lowercase and underscores
## ALL argumentss should be cclear in their needs and where possible include their expected type
## remebember the return statement or your function will return none
# keep functions small to preserve readability and simplicity
## use comments in your functions/methods to give instructions on how to use them
##Consider using type hints to avoid type errors when ypu run your code.