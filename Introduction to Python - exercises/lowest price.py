n = int(input("input number of kilometers: "))

if n < 20:
    print("Taxi is the only way!")

    daytime = input("period of day: ")
    #validate period of day
    while daytime != 'day' and daytime != 'night':
        daytime = input("period of day: ")

    
    if daytime == 'day':
        price = (0.79 * n) + 0.7
    elif daytime == 'night':
        price = (0.9 *n) + 0.7
elif n > 20 and n <= 100:
    print("The bus is the better option!")
    price = 0.09 * n
elif n >= 100:
    print("The train is the cheapest option!")
    price = 0.06 * n
print ("Total price:", price, " BGN")