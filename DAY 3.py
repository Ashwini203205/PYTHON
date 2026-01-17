# STRING'S

print('Ashwini')
print( "Mohan")
print("""Giri""")
print('This is string"s tutorial') 
print(" ")

# NEXT LINE


print(" This is \n Next line")   #not this (/)
print("\n")

# CONCATINATION (JOIN CHAR)

str1="sun" 
str2="light"
print(str1 +" "+ str2)               #we can add more than two
print("sun"+"shine")

# LENGTH

a="Ashwini "                       #space also consider
print(len(a))

# INDEXTING (start with zero. use for access char , cannot modify)

print(a[0])
print(a[1])

#SLICING (access part of string) (start with 0)
 
#forward
str="Doing Slicing"
print(str[6:13])
print(str[:])                      #print all
print(str[0:])                     #print all without end
print(str[:13])                    #print all without start

#backward (negative indexing)   
print(str[-7:-1])                  #start with -1 (i.e -5 -4 -3 -2 -1)


# STRING FUNCTION (There are too many functions of string but follow are main)

x="i am a coder"

print(x.endswith("er"))               # True or False
print(x.capitalize())                 #capitalize 1st char
print(x.replace("coder","Ashwini"))   #replace single letter or whole word
print(x.find("i"))                    #start with 0, fing single letter, shows 1st occurance
print(x.count("a"))                   #count single letter or whole word how many times occurs in str

