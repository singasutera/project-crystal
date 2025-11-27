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

# [my_math.py]
def bestnumber():
    return "it's not 69"
def may_contain_other_functions():
    x = "and variables"
    return x

# >>importing the whole module>>

# [your_math.py file]
# import my_math
# result = my_math.bestnumber() !!!when accessing the function, need to mention the module
# print(result)

# >>importing just the function>>

# [your_math.py file]
# from my_math import bestnumber
# result = bestnumber() !!!access the function directly
# print(result)

# >>both will print "it's not 69", because it isn't the best number xd. but anyway...<<<




