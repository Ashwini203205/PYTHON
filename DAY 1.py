# SYNTAX




print("Hello !")                    #double   ("") ('') (""" """)  same working
print('ashwini')                    #single
print("""ashwini""")                #triple
print("I am Ashwini Mohan Giri")    #sentence
print(20)                           #number

# COMMENT

# THIS IS A SINGLE LINE COMMENT 
# python is case-sensitive
#  a=2 A=2 differnt both

"""
 OK
THIS 
IS 
MULTILINE
COMMENT
"""

# VARIABLES & IDENTIFIER

name="Ashwini"
age=20
price=25.2

print("My Nmae is: ",name)
print("My Age iS: ",age)
price2=print((price*2))

# DATA TYPES (inbuild/buildin & userdefine)

print(type(name))   #str
print(type(age))    #int
print(type(price))  #float
print(type(True))   #boolean
a=None              #none type
print(type(a))     
b=1j                 #complex
print(type(b))       

x=["apple","banana","cherry"]     #list mutable can change
y=("apple","banana","cherry")     #tuple
z={"apple","banana","cherry"}     #set
print(type(x))
print(type(y))
print(type(z))  

# APPEND

x.append("chicku")              
print(x)

# CASTING

a=float(2)
b=str(2)

# CONVERT

c=2
d=3.22
e=2j
f=print(float(c))      # int to float
g=print(int(d))        #float to int
h=print(complex(c))    #float to complex

# UPEER LOWER

k="Hello"
u=print(k.upper())
o=print(k.lower())

#SUM & DIFFERENCE
a=3
b=2

c=(a+b)
print(c)

d=(a-b)
print(d)
