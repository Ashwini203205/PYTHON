# Polymorphism

"""
poly:many & morphism:form
operator overloading
when the same operator is allowed to have diff meaning acc to context

There are mainly 2 types: Compile-time Polymorphism (Method Overloading)
                          Run-time Polymorphism (Method Overriding)
"""

# Operation polym.    (+ overload , diff form diff meaning) 

print(1+2)          #add:3
print("ash"+"wini") #concatination:ashwini
print([1,2]+[3,4])  #merger:[1,2,3,4]


# Function Polymorphism

print(len("Hello"))
print(len([1, 2, 3, 4]))

print(type("hello"))


# Compile-time Polymorphism (Method Overloading)

class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))      # 5
print(m.add(2, 3, 4))   # 9


# Run-Time Polymorphism(Method Overriding)

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class")

c = Child()
c.show()
