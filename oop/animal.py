class Animal:
    alive = True

    def eat(self):
        print("The animal is eating!")

    def sleep(self):
        print("The animal is sleeping!")

class Rabbit(Animal):

    def run(self):
        print("The rabbit is running!")

class Fish(Animal):

    def swim(self):
        print("The fish is swimming!")

rabbit = Rabbit()
fish = Fish()

rabbit.eat()
fish.eat()
rabbit.run()
fish.swim()