#OPERATORS
'''
#arithmetic operator

a= 10
b= 30
print(a+b)
a="shruthi"
b="palmari"
name =a+" "+b
print(name)

print(a-b)
c= a*b
print(c)
print(200/3) #division- quotient
print(200//3) #division- without decimal quotient
print(200%3) #modules 
print(20**4) #exponential (20*20*20*20)


#addition with float
m= 20
n= 37.54
print(m+n) 

# addition with string
m= 20
n= "30.22"
print(str(m)+n) #concatination by type_casting

m= 'raj'
n= 'shekhar'
print(m,n) 

age= 35
print("Age=",age)

#subtraction

a,b,c= 1000,20,48
c= a-b-c
print(c)

#multiplication with string
a= 'john'
b= 4
print(a*b)

#multiplication with multiple values
a= 4
b= 4
c= 4
d=a*b*c

print(d)

#assignment operator
#add and assign
a= 10
print(a)
a+= 5
print(a)
a-= 5             #subtract and assign
print(a)
a *= 5
print(a)          #multiply and assign
a /=5
print(a)          #division and assign
a //=5 
print(a)          #floor division and assign
a %= 5
print(a)          #mod and assign
c= 20/5*2
print(c)
d=10
d**=3
print(d)               #expo and assign

name,age,salary = "shruthi",30, 49000                        #Different Data Types with Multiple Assignment
print(name)
print(age)
print(salary) 

a=b=c= 5000                                  #Assigning the Same Value to Multiple Variables
print(a,b,c)   

#Swapping Variables
a= 10
b= 20
print("before swapping")
print("a=", a)
print("b=", b)
a,b = b,a
print("after swapping")
print("a=", a)
print("b=", b)  

#comparioson operators
a =10
b = 20
print(a>b)

a==b # equal to
print(a==b)
print(a!=b)
print(a>b)
print(b>a)
print(a>=b)
print(b>=a)
print("Shruthi"=="shruthi") 

#LOGICAL OPERators
#AND
age= 13
salary =50000
result = age>18 and salary >30000
print(result)

age=20
salary =50000
experience = 6
result = age>18 and salary >30000 and experience >4         #Multiple Conditions with and
print(result) 

#OR
age= 13
salary =50000
result = age>18 or salary >30000
print(result)

age=20
salary =50000
experience = 6
result = age>18 or salary >30000 or experience >4         #Multiple Conditions with or
print(result)  

#NOT
a = True
print(not a) 

age=20
salary =50000
experience = 6
result = age>18 and salary >30000 or experience >4         #Combining and and or
print(result)    

# IDENTITY OPERATOR
a =[10,20]
b= a
print(a is b)              # IS

a=[10,20]
b=[10,20]
print( a is not b)     #IS NOT

# MEMBERSHIP OPERATOR 
text ="shruthi"
print("h" in text)         #in with String

course =["python","Data Analyst","Data Science"]
print("Data Analyst" in course)                #in with List
print("java"not in course)

#Membership with Tuple
num = (10, 20, 30)
print(20 in num)

#Membership with Set
numbers = {10, 20, 30}
print(40 in numbers)

#Membership with Dictionary
student = {
"name": "Shruthi",
"age": 25
}
print("name" in student)
print("Shruthi"in student)
'''
#Bitwise Operators
#AND
a= 5
b= 3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a>>1)
print(a<<1)