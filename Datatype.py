#datatype
'''a=100
A=150
B=200

print(type(a))

a=A=100
print(id(a))
print(id(A))
print(id(B))
print(a)

#list
fruits=["apple","banana","cherry"] # add_item_append
print("before:",fruits)
print("before id:",id(fruits))

fruits.append("grapes")
print("after:",fruits)
print("after id:",id(fruits))

fruits=["apple","banana","cherry"]  #insert at particular position
print("before:",fruits)
print("before id:",id(fruits))

fruits.insert(2,"grapes")
print("after:",fruits)
print("after id:",id(fruits))

fruits=["apple","banana","cherry"]  #insert multiple items
print("before:",fruits)
print("before id:",id(fruits))

fruits.extend(["mango","pineapple"])
print("after:",fruits)
print("after id:",id(fruits))

fruits=["apple","banana","cherry"]  #update the values
print("before:",fruits)
print("before id:",id(fruits))

fruits[0]= "jackfruit"
print("after:",fruits)
print("after id:",id(fruits))

fruits=["apple","banana","cherry","jackfruit"]  #remove the item
print("before:",fruits)
print("before id:",id(fruits))

fruits.pop(2)
print("after:",fruits)
print("after id:",id(fruits))

fruits=["apple","banana","cherry","jackfruit"]  #remove the last item
print("before:",fruits)
print("before id:",id(fruits))

fruits.pop()
print("after:",fruits)
print("after id:",id(fruits))

fruits=["apple","banana","cherry","jackfruit"]  #remove all the item
print("before:",fruits)
print("before id:",id(fruits))

fruits.clear()
print("after:",fruits)
print("after id:",id(fruits))

vegetables=("tomato","raddish","brinjal","garlic") #tuple(cant change the values)
print(vegetables)

num={10,20,30,40,20,10,50}       #set
print(num)
print(type(num))
print(id(num))

fruits={"apple","banana","cherry","jackfruit"}  #
print("before:",fruits)
print("before id:",id(fruits))

fruits.add("pineapple")
print("after:",fruits)
print("after id:",id(fruits))

student= {                   #dictionary
    "name":"shruthi",
    "age": 30
}
print(student)
print(type(student))

student= {
    "name":"shruthi",
    "age": 30
}
print("before:",student)
print("before id:", id(student))

student["course"]="PYTHON"                  # add new item
print("after:",student)
print("after id:",id(student))

student= {
    "name":"shruthi",
    "age": 30,
    "course":"PYTHON" 
}
print("before:",student)
print("before id:", id(student))

student["course"]="Data analyst"             #update the exisiting item
print("after:",student)
print("after id:",id(student))

student= {
    "name":"shruthi",
    "age": 30,
    "course":"PYTHON" 
}
print("before:",student)
print("before id:", id(student))

student.update({
    "course":"Data analyst" ,
    "age":27 
})                                           #update the multiple item
print("after:",student)
print("after id:",id(student))

student= {
    "name":"shruthi",
    "age": 30,
    "course":"PYTHON" 
}
print("before:",student)
print("before id:", id(student))

student.pop("age")                                           #remove item
print("after:",student)
print("after id:",id(student))

student= {
    "name":"shruthi",
    "age": 30,
    "course":"PYTHON" 
}
print("before:",student)
print("before id:", id(student))

student.popitem()                                           #remove last item
print("after:",student)
print("after id:",id(student))
'''
student= {
    "name":"shruthi",
    "age": 30,
    "course":"PYTHON" 
}
print("before:",student)
print("before id:", id(student))

student.clear()                                           #remove all item
print("after:",student)
print("after id:",id(student))


