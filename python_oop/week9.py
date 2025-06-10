class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name


dog1 = Dog("Tommy")
dog2 = Dog("Bruno")

print(dog1.name, dog2.name)

print(dog1.species, dog2.species)