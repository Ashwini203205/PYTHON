#LIST :
"""
- build in data type  (stores int,str,float etc)
- Mutable can be change.
- list can access as well as change.
- index start from Zero.
"""

marks1=11
marks2=22
marks3=33
marks4=44
marks5=55

#instead of this we can writen list at a time as follow-->

marks=[11,22,33,44,55]
print(marks)
print(type(marks))        #type of list
print(len(marks))         #length of list
print(marks[0])           #print 1st letter

#Replace in list

stu=["Ashwini",20,"IT"]
print(stu)
stu[0]="Yash"
print(stu)
#or
stu.insert(1,"Yash")      #this is list method index() we see next
print(stu)

#List Slicing :
"""- similar to string slicing
   - slicing is subset of list
"""
print(marks[:2])            #it will print start to one no before to 2 not print 2
print(marks[1:])            #it will print from 1 (one also)to end
print(marks[1:3])           #print one and 2 not 3
print(marks[-3:-1]) 

#i.e before : is print but after : not print.
 
# List Method :

list=[2,1,3,5,4]

print(list.append(6))       # append() : adding in list
print(list)

list.sort()                 # sort()  : by default ascending
print(list)

list.sort(reverse=True)     # sort() : by decending
print(list)

list=[2,1,3,5,4]
list.reverse()              # reverse() : reverse of whole list
print(list)

list.insert(1,9)            # insert() : insert or replace 
print(list)
list.insert(5,9)           
print(list)

list.remove(5)              # remove() : remove letter '9'list.insert(5,9)           
print(list)

list.pop(1)                 # pop() : remove/pop 1st position in list

print(list)
