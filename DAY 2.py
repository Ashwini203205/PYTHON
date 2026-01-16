# TYPES OF OPERATOR

a=50
b=20

# 1.ARTHIMETIC OPERATOR
print(a+b)           #ADDITION
print(a-b)           #SUBTRACTION
print(a*b)           #MULTIPICATION
print(a/b)           #DIVISION
print(a%b)           #MODULE
print(a**b)          #POWER

# 2.RELATIONAL OPERATOR
print(a==b)           #EQUAL TO
print(a!=b)           #NOT EQUAL TO
print(a>=b)           #GREATER THAN EQUAL TO
print(a<=b)           #LESS THAN EQUAL TO
print(a<b)            #LESS THAN
print(a>b)            #GREATER THAN

# 3.ASSIGNMENT OPERATOR
num=20
NUM=num+10
print(NUM)
#OR
num=+20          #OR num+=20
num*=20
num-=20
num/=20
num*=20
num%=20
num**=20

# 4.LOGICAL OPERATOR
print(not True)     #False
print(not False)    #True
print(a>b)          #True
print(a<b)          #False
print(a>b and a>b)  #True
print(a>b and a<b)  #False
print(a>b or a>b)   #True
print(a<b or a<b)   #False


""" TYPES OF CONVERSION 
- COVERSION (automatically) 
- CASTING   (forcefully manually)
"""
a=2          #int
b=4.5        #float
sum=a+b      #python covert int to float becz float is superior
print(sum)   #this is automatic covertion

a="2"         #string
b=4.5         #float
              #python can not covert string to float or can not add 
a=int("2")    #but we can do it forcefully i.e castibg
sum=a+b
print(sum)   
print(type(a)) 

a=3.14
a=str(a)
print(type(a))

# TAKING INPUT
Name=input("enter your name: ")
print("welcome",Name)
print(type(Name))

Age=input("enter your age: ")
       
Phone=input("enter your phone no.: ")













