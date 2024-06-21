from typing import Any


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.__age = age # Private attribute
        self.__email = email # Private attribute

    
    # Getter for age
    def get_age(self):
        return self.__age
    
    # Setter for age
    def set_age(self, age):
        self.__age = age
    
    # Getter for email
    def get_email(self):
        return self.__email
    
    # Setter for email
    def set_email(self, email):
        self.__email = email

    def display_info(self):
        return f"Name: {self.name}, Age: {self.__age}, Email: {self.__email}"


# Create an object
person1 = Person("Jess", 30, "jessv@example.com")

# Accessing and modifying age using getter and setter, get and set are variable names, you can name it whatever you like but just make sure names are meaningful. defining variable such as getter and setter helps to modify the attributes values later on if needed some attributes are private. Without this, you couldn't update them. If you want the attributes to be default you won't need to have getter and setter since you could update them calling the class and passing new attributes values.

print(person1.get_age())
person1.set_age(31)
print(person1.get_age())

print(person1.get_email())
person1.set_email("jessvmartins@example.com")
print(person1.get_email())

# Displaying all info

print(person1.display_info())