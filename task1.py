#1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
#create an instance for each of the animal and call the unique method for it.
#Determine if each of the animal is an instance of the Animals class

class Animal:
    """
    Parent class, should have eat, sleep
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print("Meowing")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("Barking")

class Bat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print("Flying")

class Fish(Animal):

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print("Swimming")

class Fox(Animal):

    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print("Running")

cat = Cat('Tom')
cat.meow()
print(isinstance(cat, Animal))

dog = Dog('Tom')
dog.bark()
print(isinstance(dog, Animal))

bat = Bat('Grimmy')
bat.fly()
print(isinstance(bat, Animal))

fish = Fish('Garry')
fish.swim()
print(isinstance(fish, Animal))

fox = Fox('Larry')
fox.run()
print(isinstance(fox, Animal))

#1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    """
    Human class, should have eat, sleep, study, work
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Human is eating")

    def sleep(self):
        print("Human is sleeping")

    def study(self):
        print("Human is studying")

    def work(self):
        print("Human is working")


class Centaur(Human , Animal):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
    def __init__(self, name):
        super().__init__(name)

centaur = Centaur('someName')
centaur.sleep()
centaur.eat()