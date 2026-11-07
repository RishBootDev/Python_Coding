class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def display_address(self):
        print("Street:", self.street, ", City:", self.city, ", Postal Code:", self.postal_code)


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print("Name:", self.name, ", Age:", self.age)
        print("Address:", end=" ")
        self.address.display_address()


person_address = Address("123 Main St", "Cityville", "12345")
person = Person("John Doe", 30, person_address)

person.display_info()

