# Create a decorator calledlogger that print a message before and after a function runs.
#Use it on a function greed that prints message Hello Python
def logger(func):
    def inner():
        print("Starting a function...")
        func()
        print("Ending of Message...")
        return func
    return inner


@logger
def greed():
    print ("Hello Python!")

greed()