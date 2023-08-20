class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"I am {self.name}.")

class Dog(Animal):
    def speak(self):
        print(f"Woof! I am {self.name}.")

class Cat(Animal):
    def speak(self):
        print(f"Meow! I am {self.name}.")

def main():
    dog = Dog("Max")
    dog.speak()

    cat = Cat("Kitty")
    cat.speak()

if __name__ == "__main__":
    main()
