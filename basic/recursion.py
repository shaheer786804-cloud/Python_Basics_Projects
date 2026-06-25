import sys
from time import sleep
sys.setrecursionlimit(1000)


count = 1
def greed():
    sleep (0.5)
    global count
    print("Hello" , count)
    count += 1
    greed()

greed()
