car1 = {
    "Brand" : input("Car 1 brand:"),
    "Model" : input("Car 1 model:"),
    "Horsepower" : int(input("Car 1 how much horsepower:"))
}
car2 = {
    "Brand" : input("Car 2 brand:"),
    "Model" : input("Car 2 model:"),
    "Horsepower" : int(input("Car 2 how much horsepower:"))
}
if car1["Horsepower"] > car2["Horsepower"]:
    print(car1["Brand"])
    print(car1["Model"])
    print(car1["Horsepower"])
elif car2["Horsepower"] > car1["Horsepower"]:
    print(car2["Brand"])
    print(car2["Model"])
    print(car2["Horsepower"])
else:
    print("Both cars have the same horsepower!")