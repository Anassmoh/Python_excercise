class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

dog1 = Dog("snap", 1999)
dog2 = Dog("Lucky", 2000, "how how")

print(dog1.name)
print(dog2.sound)
print(dog2.birth_year)

dog2.bark(2)

hotel  = Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)

for i in range(len(hotel.dogs)):
    print(hotel.dogs[i].name)