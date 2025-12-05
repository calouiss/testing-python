#Functions
def sayHello(): #Defining a function
    print("Hello")

'''def sayHelloWithName(fname):
    print(f"Hello {fname}")
    print("How are you?")
    

fname=input("Enter your first name:")
lname=input("Enter your last name:")
sayHello() #Calling a function
sayHelloWithName("Gurpreet")#Calling function with an argument(Hard coded argument)
sayHelloWithName(fname)#Calling function with an argument'''
#Arbitory argument function
def friendsInfo(*friends):
    print("My school friend is:"+friends[0])
    print("My best friend is" +friends[-1] )

friendsInfo("friend1","friend2","friend3") #arguments treated like a tuple
#keyword arguments
def friendsInfo1(friend1="Swetha",friend2="Ahmed"):
    print(friend1)
    print(friend2)
friendsInfo1("Cythia","Gurpreet")
#With the arguments, it takes the values that are paased through the argument
friendsInfo1()#Without arguments, 
#it takes the values that are assigned in the function definition
def friendsInfo2(**friend):
    print("My friend's last name is:" +friend["lname"])
    print("My friend is in :" +friend["campus"])
friendsInfo2(fname="Sweta",lname="R",campus="Davis")
def friendFood (food):
    for x in food:
        print(x)
    print(food)
fav=["Pizza","Pasta","Burger"]
friendFood(fav)
def mathFunction(x):
    return 2+x #functions return the value
print(mathFunction(11))
print(mathFunction(22)+10)
result=mathFunction(11)
result=result+10

'''def mathFunction1(x):
    while(x!=1):
        x=x+mathFunction1(x) #Recursion calling a function within itself
    print("out of while loop")

mathFunction1(4)'''
def listDemo():
    list1=["item1","item2"]
    return list1
print(listDemo())
def dictionaryDemo():
    myDict={"name":"sweta",
            "Campus":"Davis"

    }
    print(myDict)
dictionaryDemo()
