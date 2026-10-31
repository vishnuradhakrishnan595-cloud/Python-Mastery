"""Polymorphism: different objects provide a common method interface."""


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Cow:
    def speak(self) -> str:
        return "Moo"


def make_animal_speak(animal) -> None:
    """Accept any object that provides a speak() method."""
    print(animal.speak())


def main():
    animals = [Dog(), Cat(), Cow()]
    for animal in animals:
        make_animal_speak(animal)


if __name__ == "__main__":
    main()
