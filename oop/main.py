from car import Car

car1 = Car("Ford", "Escape", 2013, "white")
car2 = Car("BMW", "X6", 2020, "black")

car1.drive()
car2.stop()

print("car1's wheels: " + str(car1.wheels))
print("car2's wheels: " + str(car2.wheels))

# we can modify class variables through instance, which will not infect other instances
car1.wheels = 2
print("car1's wheels: " + str(car1.wheels))
print("car2's wheels: " + str(car2.wheels))

# but if we modify a class variable through instance, then we can't modify it again for this instance through the class variables
Car.wheels = 3
print("car1's wheels: " + str(car1.wheels))
print("car2's wheels: " + str(car2.wheels))