from time import sleep
import math
def delay(fn,ms,*args):
  sleep (ms / 1000)
  return fn (*args)
print("Square root 25100 after 2123 specific miliseconds:")
print(delay(lambda x: math.sqrt(x),2123,25100))