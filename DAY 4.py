# CONDITIONAL STATEMENT
# SYNTAX:SET OF RULES 

# if-else

age=int(input("age = "))              # input only for string but here age is integer we can convert.

if age>=18:
    print(" can vote \n can drive")   # space before print called indentation it is very imp in python.
else:
    print(" can't vote \n can't drive")

# if-elif-else                        #can use more than 1 elif

colour = input("Enter colour: ")

if colour == "red":
    print("STOP")
elif colour == "yellow":
    print("GO SLOW")
elif colour == "green":
    print("GO")
else:
    print("Invalid colour")

# if-if-if...                        at a time check two or more conditions

a=10
if a>=2:
    print("greater than 2")
if a<=15:
    print("less than 15")


# EXAMPLE

marks=int(input("enter marks: "))
if marks>=80 and marks<=90:
    print("A")
elif marks>=70 and marks<=80:
    print("B")
else:
    print("D")


# NESTING if 

age=int(input("enter age: "))
if age>=18:
    if age>=80:                       #if inside if
        print("cannot drive")
    else:
        print("drive")
else:
    print("cannot drive")


# EXAMPLES
# 1.EVEN ODD
n=int(input("enetr no: "))
if n%2==0:
    print("EVEN")
else:
    print("ODD")

# 2. GREATER NO. IN THREE
A=int(input("enetr 1 no: "))
B=int(input("enetr 2 no: "))
C=int(input("enetr 3 no: "))
if A>=B and A>=C:
    print("A is grater",A)
elif B>=C:
    print("B is grater",B)
else:
    print("C is greater",C)