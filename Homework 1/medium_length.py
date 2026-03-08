n = int(input("Enter the count of the strings:"))
strings = ['apple', 'orange', 'watermelon', 'banana', 'apple']
for i in range(n):
    strings.append
total_length = 0
for s in strings:
    total_length += len(s)
average_length = total_length / n
print("The medium length of the strings is:", average_length)