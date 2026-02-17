# Inheritance

"""
Child class derives properties and methods of parent class

Types: Single Inheritance      (one child one parent)
       Multiple Inheritance    (One Base, Multiple Derived)
       Multi Level Inheritance (Multiple parent, One child)
"""


"""decorators

1. @Static Method : argument:no class no property   Uses decorator: @staticmethod
                    Takes no self and no cls
                    Cannot access class or instance variables directly
                    Used for utility/helper functions)
2. @classmethod   : argument:class   Uses decorator: @classmethod
                    Takes cls (class) as first parameter
                    Can access and modify class variables)
3. instance method: __init__ argument:self   
                    Takes self as first parameter
                    Works with object data (instance variables)
                    Can access and modify object properties)
4. @property     :  Uses decorator: @property
                    Allows a method to be accessed like a variable
                    Used for data hiding and encapsulation
                    Helps control access to private variables

* Super Method

______________________________________________________________________________________
| Method Type     | Decorator       | First Argument | Access Instance | Access Class |
| --------------- | --------------- | -------------- | --------------- | ------------ |
| Instance Method | No decorator    | `self`         | ✅ Yes          | ✅ Yes      |
| Class Method    | `@classmethod`  | `cls`          | ❌ No           | ✅ Yes      |
| Static Method   | `@staticmethod` | None           | ❌ No           | ❌ No       |
| Property Method | `@property`     | `self`         | ✅ Yes          | ✅ Yes      |
_______________________________________________________________________________________
"""

# 1.Single level Inhertance

class Car:                      # Parent / Base class: gives property to another class
    @staticmethod
    def start():
        print("Car started...")

class Toyota(Car):              # Child / Derived class: takes property from another class
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")       # Creating object of child class
car1.start()                    # Creating object of child class


# OR if you want to print car name
class Car:
    def start(self):
        print("Car started...")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Car name:", self.name)

car1 = Toyota("Fortuner")
car1.start()
car1.show()
print("\n")



# 2.Multilevel

class Car:                           # Parent / Base class
    @staticmethod
    def start():
        print("Car started...")

class Toyota(Car):                   # Child / Derived class
    def __init__(self, brand):
        self.name = brand

class fortuner(Toyota):              # Child / Derived class
    def __init__(self, type):
        self.name = type

car1 = fortuner("disel")            # Creating object of child class
car1.start()  
print("\n")                     



# 3.Multiple 

class A:
    varA="class A"

class B:
    varB="class B" 

class C(A,B):
    varC="class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
print("\n")


#Super Method

"""
 we can call it parent class in inheritance.
 it is used to accress methods of the parent class from the child class.
When a child class wants to use something from its parent class, it uses super().

To reuse parent class code.
To avoid rewriting same code.
To extend parent class functionality.
Useful in inheritance.
"""

# Parent Class 
class Animal:                          # Animal is the parent class.
    def sound(self):
        print("Animals make sound")

# Child Class
class Dog(Animal):                     # Dog is the child class.
    def sound(self):
        super().sound()                # calling parent class method. "Call the parent class method first."
        print("Dog barks")             # Both classes have a method called sound().

# Object creation
d = Dog()
d.sound()
print("\n")

# super also use with constructor 

# Parent Class
class Person:
    def __init__(self, name):
        self.name = name                   # Parent constructor called

# Child Class
class Student(Person):
    def __init__(self, name,course):
        super().__init__(name)             # calling parent constructor
        self.course = course               # Child constructor called

# Object creation
s1 = Student("Rahul","IT")

print("Name:", s1.name)
print("Course:", s1.course)


# Class Method

"""
Class Method is bound to the class & receives the class as an implicit first argument
note: static mathod cant access or modify class state & generally for utility
We use @classmethod decorator to create a class method.
"""

#without class method 

class person:
    name="ashwini"
    def changename(self,name):
        self.name=name

p1=person()
p1.changename("yash")
print(p1.name)
print(person.name)
print("\n")


#with class method
class person:
    name="rupali"

    @classmethod
    def changename(cls,name):
        cls.name=name

p1=person()
p1.changename("mohan")
print(p1.name)
print(person.name)
print("\n")


#@property 
"""
we use @property dector on any method in class to use method as a property
"""
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

p = Person(20)
print(p.age)                   # No parentheses needed





