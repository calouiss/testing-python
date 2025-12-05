#python list
studentList=["cynthia","Gurpreet","Aditya"]
print(studentList)
a=studentList.count("cynthia")
print(a)
#list index: studentList[0]="cynthia" studentList[1]="Gurpreet"
print(studentList[2])
#print(studentList[3]) Nothing at 3.
print(len(studentList))#length of the list no. of elements in the list 
print(studentList[-3])
print(studentList[-2])
studentListUpadated=["cynthia",11,33.55]
print(studentListUpadated)
#list is chagable.
studentList.append("Ahmed")
print(studentList)
'''name=input("Enter name:")
studentList.append(name)
print(studentList)'''
anotherList=studentList.copy()
print(anotherList)
studentList.insert(2,"sweta")
print(studentList)
#insert method inserts the element at the specified location 
studentList.insert(5,"sweta")
print(studentList)
studentList.insert(-1,"sweta")
print(studentList)
studentList.insert(20,"sweta")#allows duplicates
print(studentList)
studentList.pop(1) #Removes the element from the specified location
print(studentList)
studentList.pop(-3)
print(studentList)
studentList.clear() #Removes all the elements from the list
print(studentList)
studentList=["cynthia","Gurpreet","Aditya","cynthia","cynthia"]
print(studentList)
print(studentList.count("cynthia"))
#print(a)
print(studentList[1])
del studentList #Deletes the list
#print(studentList)
#list is mutable. meaning changable
#Tuple
studentTuple=("cynthia","Gurpreet","Aditya") 
print(studentTuple)
#studentTuple.append("Ahmed") 
# This is not allowed because tuples are unchangable
print(studentTuple)
flowerTuple=("Rose","Lily","Phlox")
#unpacking
red,white,pink=flowerTuple
print(f"Red:{red}")
print(f"white:{white}")
#print(f"green:{green}")
print(red)
#Tuples are ordered . Immutable. can't change the tuple.
#Set
#unchangeable,uordered,unindexed,immutable.
studentSet={"cynthia","Gurpreet","Aditya"}
print(studentSet)
studentSet.add("Ahmed")
print(studentSet)
studentSet.remove("cynthia")
print(studentSet)
#Removes the item from the list 
# but  generates key error if element is not present
#studentSet.remove("cynthia")
#print(studentSet)
studentSet.pop()
print(studentSet)
studentSet.discard("Aditya")
print(studentSet)
studentSet.discard("Aditya")
#Removes the item from the list 
# but does not generate key error if element is not present
print(studentSet)
studentSet.clear()
print(studentSet)
#Dictionary
#"key":"value"
studentDict={"id": 123,
             "name":"Ahmed",
             "Campus":"Davis",
             "marks":[100,99]
             }
print(studentDict)
studentDict["Campus"]="HMC"
print(studentDict)
studentDict.update({"Campus":"Davis"})
print(studentDict)
studentDict.update({"Grade":"A"})
print(studentDict)
studentDict.pop("Grade")
print(studentDict)
studentDict.popitem()
print(studentDict)
studentDict.clear()
print(studentDict)
del studentDict
#print(studentDict) error
#  because dictionary does not exist (it is deleted)