"""
DICTONARY 
={"Key" : "value"} pairs  (unorder, mutable, don't allow duplicate keys.)
"""

dic={
    "key":"value",                  #we can store str,int,boolean,float,list.set..
    "name":"ashwini",
    "age":20,
    "is adult":True,
    "marks":98.9,
    "subject":["python","java"],
    "hobby":("yoga","karate"),
    1:100,                          #we can make int as key
    2:150
}
print(dic)
print(type(dic),"\n")

# Accessing dictionary

print(dic["name"])
print(dic[1],"\n")

# Adding in dictonary

dic["surname"]="Giri"
print(dic,"\n")

# Replace or change

dic["name"]="Yash"
print(dic,"\n")

dic[1]=200
print(dic,"\n")

# Null dictonary
null_dic={}
print(null_dic)
null_dic["name"]="mohan"
print(null_dic)

# Nested dictonary

stu={
    "name":"rupali",
    "age":40,
    "marks":{
        "python":99,
        "html":90
    }
}
print(stu,"\n")

# Dictonary Methons

print(stu.keys())                    #keys= methods=returns all keys
print(len(stu))                             #length of keys 

print(stu.values())                  #values= values retuns

print(stu.items())                   #items= returns all key values in form of list

print(stu.get("name"))               #get=   access or return value acc to key

stu.update({"city":"hi"})            #update= add new or update also
print(stu)
stu.update({"name":"as"})
print(stu,"\n")