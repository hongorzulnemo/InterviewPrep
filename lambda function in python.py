# The power of lambda is better shown when you use them as an 
# anonymous function inside another function as a helper instead of declaring new func.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(10)) # 20
