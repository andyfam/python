class Prey:
    def flee(self):
        print("The animal is fleeing!")

class Predator:
    def hunt(self):
        print("The animal is hunting!")

class Fish(Prey, Predator):
    pass

fish = Fish()

fish.flee()
fish.hunt()