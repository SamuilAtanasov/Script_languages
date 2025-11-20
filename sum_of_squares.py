N = int(input("Enter the count of the numbers:"))
numbers = []

for i in range(N):
    s = int(input(f"Number {i + 1}:"))
    numbers.append(s)
sum_of_squares = 0
for num in numbers:
    sum_of_squares += num ** 2
print("The sum of squares is:", sum_of_squares)