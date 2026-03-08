list = ('apple','orange', 'watermelon', 'banana', 'apple')

dublicates = False

for i in range (len(list)):
        if list.count(list[i]) > 1:
            dublicates = True
if dublicates:
    print("There are equal items in the list!")
else:
    print("There are NO equal items in the list!")