class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


dog = Dog('Willie', 6)
# dog2 = Dog('Lucy', 3)

# print(f"My dog's name is {dog.name}.")
# print(f"My dog is {dog.age} years old.")
dog.sit()
dog.roll_over()

# print(f"\nYour dog's name is {dog2.name}.")
# print(f"Your dog is {dog2.age} years old.")
# dog2.sit()