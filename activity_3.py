# Functional Programming
def flat_and_sorted(array):
    arr = []
    for each in array:
        for i in each:
            arr.append(i)
    return sorted(arr)


# Make sure to answer the following questions about your coding process:
    
# How does this solution ensure data immutability?
    # this solution does not modify the array's data 
# Is this solution a pure function? Why or why not?
    # Yes this is a pure function. It does not have any side affects and it does not affect the array's data
# Is this solution a higher order function? Why or why not?
    # It is a higher order function. It accepts an array and uses the sorted function to sort the data. The function flat_and_sorted is higher order because it uses sorted.
# Would it have been easier to solve this problem using a different programming style?
    # Potentially, there are several valid ways to solve this problem using OOP. Through research I found ways to do this with list comprehension, recursively, as well as using other built in functions. 
# Why in particular is functional programming a helpful paradigm when solving this problem?
    # Making sure that the data is not changed is the most helpful. We do not want our data effected

#OOP
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

def repair(self):
    self.condition = "repaired"

# class inheritance  
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2
    
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self,other):
        other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism
    # This solution demonstrates encapsulation through organization and readability. The classes contain information about the podracers that can be used later on. It demonstrates Inheritance with the class inheritance used to create the different pod racers with classes. Finally it uses Polymorphism to use the original podracer class to add the other racers as well as their special power ups
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    # I believe using the classes to organize this data to preform the necessary operations worked best for this problem. This would be a lot to hard code without using classes. 
# How in particular did Object Oriented Programming assist in the solving of this problem?
    # OOP helped to pass the data to the different podracers so hard coding the properties of the racers was not done over and over. Just once in a class that can be reused over and over. 


# Reflections
    # neither one of these programming paradigms is necessarily better than the other. they both have valuable properties and can be used for different instances. 
    # so far I have enjoyed working with OOP but I could also use functional programming more often. I do not think one sounds better than the other, more so different
    # functional programming is really great for working with databases to protect the data from changes. 
    # functional programming takes more to understand, partially because i have not worked with it as much and partially because it involves hardcoding more in order to work around using oop