# Finally keyword

# Python provides a keyword finally, which is **always executed** after 
# try and except blocks. The finally block always executes after normal 
# termination of try block or after try block terminates due to some exception.

# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        # this block is always executed  
        # regardless of exception generation. 
        print('This is always executed')  
 
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

# Output:
# Yeah ! Your answer is : 1
# This is always executed
# Sorry ! You are dividing by zero 
# This is always executed
