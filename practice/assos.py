class Dog:
    def __init__(self, name, year_of_birth, bark = "woof"):
        self.name = name
        self.year_of_birth = year_of_birth
        self.bark = bark
    def bark(self, times):
        for i in range(times):
            print(f"{self.name} barks {self.bark}")

class Hotel:
    def _init_(self):
        self.dogs = []
    def dog_checking(self, dog):
        self.dogs.append(dog)
    def dog_checkout(self, dog):
        self.fogs.remove(dog)
    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

dog1 = Dog("Max", 2020)
dog2 = Dog("Boi", 2022, "Yip Yip")
hotel = Hotel()

hotel.dog_checking(dog1)
hotel.dog_checking(dog2)
hotel.greet_dog(dog1)
hotel.dog_checkout(dog1)
