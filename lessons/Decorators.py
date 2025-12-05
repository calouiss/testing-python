def myDecorator(func):  # accepts function
    def wrapper():  # Wrap
        print("Wrapper")
        func()  # Call the original function
        print("After calling sayHello")
    return wrapper  # return wrapper

def sayHello():  # Gift
    print("Hello")

sayHello = myDecorator(sayHello)  # wrap the gift
sayHello()

from curses import wrapper
import logging #imports module logging
logging.basicConfig(level=logging.INFO)
def logDecorator(func):
    def wrapper(*args,**kwargs):
        logging.info(f"Running{func.__name__} with={args},{kwargs}")
    return wrapper

@logDecorator
def processOrder(orderId):
    print(f"Processing order: {orderId}")
processOrder(100)

#For checking authentication
def authDecorator(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("logged_in"):
            return func(user,*args,**kwargs)
            print("Access Denied")
            return
         return (user,*args)
    return wrapper  

@logDecorator
def viewProfile(user):
    print(f"Welcome: {user}")
viewProfile({"name"}"sweta", logged_in=False)
viewProfile("sweta", logged_in=True)