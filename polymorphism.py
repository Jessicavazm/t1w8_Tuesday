class Animal:
    def speak(self):
        print("Bark bark")

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function to make any animal speak, this function is defined OUTSIDE the class, this function in particular fetches the speak function from above.
def animal_sound(animal):
    print(animal.speak())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Using polymorphism to call the speak method
# Function of polymorphism, if you have a function you can pass different objects and it will behave in accord to the object passed, different methods are called depending on the object.
animal_sound(dog)
animal_sound(cat)

