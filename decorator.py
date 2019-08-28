import time 
import math 
  
def asterisk_decorator(func): 
      
    def inner1(*args, **kwargs):

        for i in range(args[0] + args[1]):
            print('*', end=""),
        result = func(*args, **kwargs)
        print(result, end="") 

        count = 0 
        while result !=0:
            result = result//10
            count += 1
        print(count + args[0] + args[1], end="")
  
    return inner1 
  
  
  
@asterisk_decorator
def sum(a, b): 
    return (a+b) 
  
# sum(10, 100) 