n = int(input("How many items in the list?"))
numbers = []
for x in range (n):
    num = int(input("Insert a number:"))
    numbers.append(num)
print(numbers)
numbers.sort()
print(numbers)