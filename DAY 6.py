# Tuple
"""
- build in data type  (stores int,str,float etc)
- Imutable seq of values, can NOT be change.
- tuple can not access as well as not change.
- index start from Zero.
"""
tup=(1,2,3,4,5)
print(tup)
print(type(tup))        #type 
print(len(tup))         #length 
print(tup[0])           #print 1st 
print("\n")

tuple=()                #zero value tuple
print(tuple)
print(type(tuple))
print(len(tuple))
print("\n")

tuple=(20,)              #right way of writting single value tuplr 
print(tuple)
print(len(tuple))

tuple=(20)               #if we write single tuple without (,) then it is str type
print(type(tuple))
print("\n")

# Tuple Slicing :
"""- similar to list slicing
   - slicing is subset of tuple
"""
print(tup[:2])           
print(tup[1:])            
print(tup[1:3])          
print(tup[-3:-1]) 
print("\n")

# Tuple Methods

tup=(1,2,3,4,5,2)
print(tup.index(1))
print(tup.index(5))
print(tup.count(2))


#EXAMPLES

Movies=[]
a=input("enter 1 movies names: ")
b=input("enter 2 movies names: ")
c=input("enter 3 movies names: ")
Movies.append(a)
Movies.append(b)
Movies.append(c)
print(Movies)

 

a=[1,2,3]
b=[3,2,1]
a.reverse()  
print(a)
if (a==b):
    print("Palindrome")
else:
    print("No")



b=["c","d","a","a","b","b","b"]
print(b.count("a"))

b.sort()
print(b)