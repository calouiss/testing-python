#Conditions in python
'''num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if num1==num2:
    print("They are equal")
elif(num1>num2):
    print("Number 1 is greater")
else:
    print("Number 2 is greater")
print("Something")
#Nested if
if(num1>10):
    print("num1is greater than 10")
    if(num1>20):
      print("num1is greater than 20")  
      if(num1>50):
          print("num1is greater than 50")
elif(num1>5):
    print("Num1 is greater than 5") 
elif(num1==5):
    pass #Do not do anything come out of the if block
else:
    print("num1is less than 5")'''
'''day=int(input("What is the day:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
        print("Yey !!Weekend!!")
    case 7:
        print("Sunday")
        print("Yey !!Weekend!!")
    case _:
        print("Invalid Input")
match day:
    case 6|7:
        print("Yey !!Weekend!!")'''
#Loops in python
i=1
while (i<10):
    print(i)
    i=i+1
    if(i==5):
        break #To break the loop
print("Loop Ended!")
studentList=["cynthia","Gurpreet","Aditya"]
#membership operators in and not in
print("cynthia" in studentList) #returns true if item belongs to the list
print("sweta" not in studentList)#returns true if 
#item does not belong to the list
#For loop
for x in studentList:
    print(x)
str="PYTHON"
for x in str:
    print(x)
for i in range(2,10,2):
    #if(i==5):
      #  break
    print (i)
print("Loop Ended")
student={
"studentDict":{"id":100,
             "name":"sweta",
             "Campus":"Davis"

},
"studentDict1":{"id":100,
             "name":"Ahmed",
             "Campus":"Davis"

}
}
studentDict1= {"id":100,
             "name":"Ahmed",
             "Campus":"Davis"

}
for x in studentDict1.values():
    print (x)
for x in studentDict1.items():
    print (x)