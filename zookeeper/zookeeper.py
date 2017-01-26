class Animal(object):
    population = 0

    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood
        Animal.population += 1

    def sleep(self):
        print self.name + " sleeps for 8 hours"

    def eat(self, food):
        print self.name + " eats " + food
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food

    @classmethod
    def populationCount(cls):

        return cls.population

class Tiger(Animal):
    def __init__(self, name):
        super(Tiger, self).__init__(name, "meat")

class Bear(Animal):
    def __init__(self, name):
        super(Bear, self).__init__(name, "fish")
    def sleep(self):
        print self.name + " hibernates for 4 months"

class Unicorn(Animal):
    def __init__(self, name):
        super(Unicorn, self).__init__(name, "marshmallows")

    def sleep(self):
        print self.name + " sleeps in a cloud"

class Giraffe(Animal):
    def __init__(self, name):
        super(Giraffe, self).__init__(name, "leaves")

    def eat(self, food):
        print self.name + " eats " + food
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food
        elif food != self.favoriteFood:
            print "YUCK! " + self.name + " spits out " + food

class Bee(Animal):
    def __init__(self, name):
        super(Bee, self).__init__(name, "pollen")

    def sleep(self):
        print self.name + " never sleeps"


    def eat(self, food):
        print self.name + " eats " + food
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food
        elif food != self.favoriteFood:
            print "YUCK! " + self.name + " spits out " + food

class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print self.name + " is feeding " + food + " to " + str(len(animals)) + " of " + str(Animal.populationCount()) + " total animals"
        for i in range(len(animals)):
            animals[i].eat(food)
            animals[i].sleep()
