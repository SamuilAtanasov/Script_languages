class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Person name: {self.name}")
        print(f"Person age: {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)

        self.section = section

    def displayStudent(self):
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student section: {self.section}")

person1 = Person("Georgi Georgiev", 37)
person1.display()
print("-----------------------------------")
student1 = Student("Ivan Ivanov", 23, "Networking")
student1.displayStudent()