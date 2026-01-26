""" LOOPS   
for loop, while loop, nested loop
Lops are use to repeat a instruction or block of code multiple times 
"""

# WHILE LOOP

#infinte loop
while True:
    print("Hello World","\n")     #TILL HERE IT WILL PRINT INFINITE TIME
    break                         #break is use to stop infinite loop
                                  #HERE PRINT HELLO WORLD ONLY ONCE
print("\n")
#finite loop
count=1
while count<=5:                    #WHILE CONDITION, PRINT HELLO ASHWINI 5 TIMES
    print("Hello Ashwini")
    count=count+1                  #INCREMENT
   
#or
count=5
while count>=1:
    print("Hello Yash")
    count=count-1

#REVERSE PRINTING
k = 10
while k >= 1:
    print(k)
    k = k - 1

#EXAMPLES

#print 1 to 50 order
i = 1
while i<=50:
    print(i)
    i = i + 1   

#print 50 to 1 order
j = 50
while j>=1:
    print(j)
    j = j - 1

#print multiplication of 2
n = 2
m = 1
while m<=10:
    print(n*m)
    m = m + 1

#print elements of follow [1,4,9,16,25,36,49,64,81,100]
a = [1,4,9,16,25,36,49,64,81,100]
index = 0                                    #this is called initialization
while index < len(a):
    print(a[index])
    index = index + 1


#search no X in tuple using loop
num = (10,20,30,40,50)                      #index starts from 0
x = 30  
i = 0
while i < len(num):
    if(num[i] == x):
       print("Element found at index:",i)
       break
    i = i + 1
