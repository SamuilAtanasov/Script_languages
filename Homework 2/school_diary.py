class Student:
    def __init__(self, name, gender, points):
        self.name = name
        self.gender = gender
        self.points = points
    def get_grade(self):
        grade = 0.034 *  self.points + 2.54
        return round(grade, 2)
    
students = []
N = int(input("Enter count of students:"))
print("Name, Gender, Points: ")

for i in range(N):
    line = input(f"\nStudent {i + 1}: ")
    name, gender, points = line.split()
    points = float(points)

    students.append(Student(name, gender, points))

total = 0
boys_total = 0
girls_total = 0

girls_count = 0
boys_count = 0

for s in students:
    grade = s.get_grade()
    total += grade

    if s.gender.upper() == "M":
        boys_total += grade
        boys_count += 1
    elif s.gender.upper() == "W":
        girls_total += grade
        girls_count += 1

print(f"Average success on everyone: {round(total / N, 2)}")

if boys_count > 0:
    print(f"Average success on the boys: {round(boys_total / boys_count, 2)}")
else:
    print("There is no entered boys.")

if girls_count > 0:
    print(f"Average success on the girls: {round(girls_total / girls_count, 2)}")
else:
    print("There is no entered girls.")