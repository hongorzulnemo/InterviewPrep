# a function is called higher order function if it contains other functions as a 
# parameter or returns a function as an output.
# property of a hof.
# 1. A function is an instance of the Object type.
def shout(text): 
    return text.upper() 
    
print(shout('Hello')) 
    
# Assigning function to a variable
yell = shout 
    
print(yell('Hello'))

# Output: 
# HELLO
# HELLO

# 2. You can pass the function as a parameter to another function.
def shout(text): 
    return text.upper() 
    
def whisper(text): 
    return text.lower() 
    
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function \
    passed as an argument.") 
    print(greeting)  
    
greet(shout) 
greet(whisper)

# Output
# HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
# hi, i am created by a function passed as an argument.

# 3.You can return the function from a function.
def create_adder(x): 
    def adder(y): 
        return x + y 
    
    return adder 
    
add_15 = create_adder(15) 
    
print(add_15(10))
