class Car:
    # name = "Maruti"
    def __init__(self, fullname):
        self.name = fullname
    print("Hello World 123!@#")

list = []

car1 = Car("BMW")
print(car1.name)
carN1 = car1
list.append(carN1)

car2 = Car("Mercedes")
print(car2.name)
carN2 = car2
list.append(carN2)

car3 = Car(input())
print(car3.name)
carN3 = car3
list.append(carN3)

print(list)