""" SET
collection of unorder items
items are unique ,sets are mutable but values/elements are immutable
dublicate values  allow but set ignores(i.e consider as one)
"""

set={1,2,3,4,"ashwini","giri","giri",5}
print(set)
print(len(set))

# empty set
null_set=()                 # wrong. this is tuple 
null=set;{}                 #correct way to create empty set
print(type(null_set))
print(type(null))
print("\n")

#methods in set
sett={10,20,50}
sett.add(30)                 # add() : to add element in set
print(sett)
print(len(sett))

sett.remove(20)              # remove() : to remove element from set
print(sett)

sett.pop()                   # pop()    : remove random element from set
print(sett)

sett.clear()                 # clear()  : to clear all element from set
print(sett,"\n")

#Union and Intersection of sets

set1={1,2,3}
set2={3,4,5}
set3=set1.union(set2)         # union()  : to join two sets
print(set3)

set4=set1.intersection(set2)  # intersection() : common element in both sets
print(set4)
print("\n")


# Examples(list ,set,tuple,dictonary)
# List
"""- ordered collection of items
   - mutable (can change)
   - allow duplicate values
""" 
# SET
"""collection of unorder items
items are unique ,sets are mutable but values/elements are immutable
dublicate values  allow but set ignores(i.e consider as one)"""

# TUPLE
"""- ordered collection of items
   - immutable (can NOT change)
   - allow duplicate values
"""
# DICTIONARY
"""- collection of key:value pairs  (unorder, mutable, don't allow duplicate keys.)
""" 


"""EX 1: Two stu are follow diff subject are there find how much classes required to complete all subject
A=java c++ python js
B=java python java c++ c"""

sub={
    "java","c++","python","js",
    "java","python","java","c++","c"
    }
print(sub)
print(len(sub))


"""EX 2 : enter marks of 3 sub from user and store in dic.
start with empty dic and add one by one .
use sub name as key and marks as value."""

marks={}
sub1=input("enter 1 subject name: ")
mark1=int(input("enter marks: "))

sub2=input("enter 2 subject name: ")
mark2=int(input("enter marks: "))   

sub3=input("enter 3 subject name: ")
mark3=int(input("enter marks: "))

marks[sub1]=mark1
marks[sub2]=mark2
marks[sub3]=mark3
print(marks)
print("\n")



