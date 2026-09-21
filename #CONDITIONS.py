#conditions
#IF statement
'''
age = int(input("enter the age: "))

if age>18:
    print("eligible")

    print("end")

# IF-ELSE statement
marks = int(input("enter the marks:"))
if marks>35:
 print("pass")
else:
 print("fail")

#IF-ELIF-ELSE STATEMENT 
marks = int(input("enter the marks:"))
if marks>85: 
    print("distinction")
elif marks>75:
    print("first class")
elif marks>55:
    print("second class")
elif marks>35:
    print("third class")
else:
    print("fail")    

#NESTED-IF statement
age = int(input("enter the age: "))
marks = int(input("enter the marks:"))

if age>18:
    if marks >60:
        print("eligable for admission")

    print("done")    '''

#MATCH-CASE STATEMENT
choice = int(input("enter the choice: "))

match choice:
    case 1:
        print("check balance")
    case 2:
        print("withdraw")
    case 3:
        print("deposit")
    case 4:
        print("change PIN")
    case 5:
        print("exit")
    case _:
        print("entered invalid choice")
                        