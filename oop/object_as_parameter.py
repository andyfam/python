class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle, color):
    vehicle.color = color

car = Car()
motorcycle = Motorcycle

change_color(car, "white")
change_color(motorcycle, "black")

print(car.color)
print(motorcycle.color)
