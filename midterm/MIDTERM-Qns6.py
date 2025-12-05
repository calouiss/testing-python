class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        self.student_id = student_id

    def displayDetails(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Age: {self.getAge()}")

# Create an object
s1 = Student("Alice", 20, "S101")

# Change s1's age to 25.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def displayDetails(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Age: {self.getAge()}")


# Create an object
s1 = Student("Alice", 20, "S101")

# Change s1's age to 25.
s1.setAge(25)

def checkAge():
    # Check if s1's age is above 18
    if s1.getAge() > 18:
        print("s1 is above 18")
    else:
        print("s1 is 18 or younger")


# Call the function
s1.displayDetails()
checkAge()