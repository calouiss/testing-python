class Person:  # Parent / base class
    def __init__(self, age, address):
        self.age = age
        self.__address = address

    def getAdderss(self):  # keep professor's spelling
        return self.__address

    def setAddress(self, new_address):
        if new_address is None or str(new_address).strip() == "":
            raise ValueError("Address cannot be empty.")
        self.__address = new_address

    def display(self):
        print(self.getAdderss())


class Student(Person):  # child class of Person
    def __init__(self, id, name, marks):
        # professor style: no call to Person.__init__ here
        self.id = id
        self.name = name
        self.__marks = marks  # private

    def display(self):
        print(f"Student id: {self.id}")
        print(f"Student name: {self.name}")
        print(f"Student marks: {self.__marks}")

    def getMarks(self):
        return self.__marks

    def setMarks(self, new_marks):
        if isinstance(new_marks, (int, float)) and 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            raise ValueError("Marks must be between 0 and 100.")


class Faculty(Person):
    def __init__(self, coursesTaught):
        self.coursesTaught = coursesTaught

    def display(self):
        print(f"Courses Taught: {self.coursesTaught}")


class ITStudent(Student):  # multilevel inheritance (prof style)
    def __init__(self, programmingLangugeLearnt):
        # no super call (prof style)
        self.programmingLangugeLearnt = programmingLangugeLearnt

    def display(self):
        print(f"programmingLangugeLearnt: {self.programmingLangugeLearnt}")


class GraduateITStudent(ITStudent):
    def __init__(self, programmingLangugeLearnt, thesisTitle):
        super().__init__(programmingLangugeLearnt)
        self.thesisTitle = thesisTitle

    # Prints exactly per requirement
    def checkEligibility(self):
        # rules: marks >= 70, language non-empty, thesis non-empty
        try:
            marks_ok = self.getMarks() >= 70
        except Exception:
            marks_ok = False
        lang_ok = bool(str(getattr(self, "programmingLangugeLearnt", "")).strip())
        thesis_ok = bool(str(str(getattr(self, "thesisTitle", "")).strip()))

        if marks_ok and lang_ok and thesis_ok:
            print("Eligible for internship")
        else:
            print("Not eligible for internship")

# ITStudent Alex: id=101, name="Alex", age=22, address="Toronto", marks=85, language="Python"
print("Creating ITStudent Alex...")
alex = ITStudent("Python")
alex.id = 101
alex.name = "Alex"
alex.age = 22

try:
    alex.setAddress("Toronto")
except ValueError as e:
    print("Error Address for Alex:", e)
try:
    alex.setMarks(85)
except ValueError as e:
    print("Error Marks for Alex:", e)

print(f"Alex -  id:{alex.id}, name:{alex.name}, age:{alex.age}, "
      f"address:{alex.getAdderss()}, lang:{alex.programmingLangugeLearnt}, marks:{alex.getMarks()}")

print("\nTrying invalid updates for Alex (to show exceptions):")
try:
    alex.setMarks(105)
except ValueError as e:
    print("Error Marks for Alex:", e)
try:
    alex.setAddress("")
except ValueError as e:
    print("Error Address for Alex:", e)

# GraduateITStudent Maya: marks=92, language="Java", thesisTitle="AI in Education"
print("\nCreating GraduateITStudent Maya...")
maya = GraduateITStudent("Java", "AI in Education")
maya.id = 102
maya.name = "Maya"
maya.age = 24
try:
    maya.setAddress("Toronto")
except ValueError as e:
    print("Error Address for Maya:", e)
try:
    maya.setMarks(92)
except ValueError as e:
    print("Error Marks for Maya:", e)

print(f"Maya -> id:{maya.id}, name:{maya.name}, age:{maya.age}, "
      f"address:{maya.getAdderss()}, lang:{maya.programmingLangugeLearnt}, "
      f"thesis:{maya.thesisTitle}, marks:{maya.getMarks()}")

# Check eligibility (should print "Eligible for internship")
print("\nMaya eligibility check:")
maya.checkEligibility()