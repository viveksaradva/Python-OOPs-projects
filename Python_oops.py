# Multilevel Inheritance in OOPs

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        print("Animal constructor is called.")

    def eat(self) -> None:
        print(f"{self.name} is eating.")

class Mammal(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age
        print("Mammal constructor is called.")

    def run(self) -> None:
        print(f"{self.name} is running.")

class Dog(Mammal):
    def __init__(self, name, age, breed) -> None:
        super().__init__(name, age)
        self.breed = breed
        print("Dog constructor is called.")

    def bark(self) -> None:
        print(f"{self.name} is barking.")

if __name__ == "__main__":
    dog1 = Dog("Happy", 3, "Golden Retriever")

    dog1.eat()
    dog1.run()
    dog1.bark()
