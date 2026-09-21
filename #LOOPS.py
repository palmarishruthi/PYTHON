#LOOPS
#WHILE LOOP
'''
ex-1
count = 1
while count< 5:
    print(count)
    count+= 1
#ex-2
num =1
total = 0
while num <=5:
    total= total+num
    num+=1

print (total) 
print(num)   

#ex-3(rightangled triangle)
row =1
while row <=5:
    star= 1
    while star <=row:
        print("*",end=" ")
        star += 1
    print()
    row += 1 

#ex-4(left angled triangle)
row =1
while row <=5:
    space =5- row
    while space> 0:
        print(" ", end=" ")
        space -=1
    star =1
    while star<=row: 
        print("*",end=" ")
        star +=1  
    print()
    row+=1     

#ex-4(left angled triangle in descresing pattern)
row =5
while row >=1:
    space =1
    while space<= row:
        print("*", end=" ")
        space +=1
      
    print()
    row-=1     

#ex-5 Reverse the number
num = 12345
reverse =0
while num>0:
    digit=num%10
    reverse = reverse*10+digit
    num = num//10
print("reverse=", reverse)   


#FOR LOOP
#LIST
courses =["java","sql","python"]
for course in courses:
    print(course)

#STRING
word ="DATA"
for charecter in word:
    print(charecter)

#TUPLE
num =[10,20,30,40]
for number in num:
    print(number)

#range(stop)
for num in range(5):
    print(num)

#range(start,stop)
for num in range(2,8):
    print(num)   

#range(start, stop,step)
for num in range(2, 11, 2):
    print(num)

#NESTED LOOP
for i in range(2):
    for j in range(3):
        print(i,j)

    #multiplication 
for i in range(1,4):
    for j in range(1,4):
        print(i*j)        

     # PATTERN
for i in range(1,5):
    for j in range(i):
        print("*", end =" ")   
    print() 

#PATTERNS
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()   

#BREAK

for i in range(1,10):
 if i == 8:
  break
 print(i)

numbers = [10,20,30,40,50,60,70]
for num in  numbers:
 if num ==60:
  print("number found")
  break
 print(num)  

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
for prod in products:
    if prod == "Keyboard":
        print("product found")
        break
    print("checking product:", prod) 

#CONTINUE
for i in range(1,9):         #ex1
    if i == 7:
        continue
    print(i) 
for i in range(1,10):        #ex2
    if i%2!=0:
        continue
    print(i) 

transactions=[1000,-5000,3000,-200,150,0]
for amount in transactions:
    if amount<0:
        continue
    print(amount)'''

#PASS
age = 9
if age>18:
    pass
print("pgm completed ")

for i in range(1,8):
    if i ==6:
        pass
    else:
        print(i)

