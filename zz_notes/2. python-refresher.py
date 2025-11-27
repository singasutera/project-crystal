# module = single .py file
# package = directory containing one or more modules. contains __init__.py
# library = umbrella term for collections of modules and/or packages

# variable = instance_of_a_class(attributes)
# variable.method()

# class = definition of an object
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a {self.year} {self.make} {self.model}.")

# instance = realization of a class    
# creating instances of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2023)

# display_info(car1) will return "This is a 2020 Toyota Camry." you get the idea.

# WHAT'S THE DIFFERENCE BETWEEN import AND from .. import ..?
# say i created a module named my_math.py
# see [my_math.py] for reference!

# >>importing the whole module>>
import my_math
# when accessing the function, need to mention the module
result = my_math.bestnumber() 
print(result)

# >>importing just the function>>
from my_math import bestnumber
# when accessing the function, no need to mention the module
result = bestnumber() 
print(result)

# both will print "it's not 69", because it isn't the best number xd. but anyway...




