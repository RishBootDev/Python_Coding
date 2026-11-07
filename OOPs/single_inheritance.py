class Animal:
	def __init__(self, name):
		self.name = name

	def eat(self):
		print(f"{self.name} is eating.")


# Dog inherits the eat() method from Animal.
class Dog(Animal):
	def __init__(self, name, breed):
		super().__init__(name)
		self.breed = breed

	def bark(self):
		print(f"{self.name} the {self.breed} is barking.")


my_dog = Dog("Buddy", "Golden Retriever")
my_dog.eat()   # Inherited from Animal
my_dog.bark()  # Defined in Dog
