#Conditional Statements – Scenario-Based Coding Tasks
#Task 1: Student Result Checker
'''
marks= int(input("enter the student marks:"))
if marks >=40:
    print("PASSED")
else:
    print("FAIL")'''

#Task 2: Student Grade Calculator
'''

marks= int(input("enter the student marks:"))
if marks>=90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >60:
    print("grade C")
elif marks >49:
    print("grade D")
elif marks >=39:
    print("grade E")
else:
    print("Grade F")    

    '''
#Task 3: Driving License Eligibility
'''
age = int(input("enter the person age:"))
if age>=18:
    print("Eligible to apply for driving license")
else:
    print("Not eligible to apply for driving license")
    '''
#Task 4: Premium Customer Discount
'''
preminum_member = input("enter the person is preminum member:")
amount = int(input("enter the purchased amount:"))

if preminum_member =="true":
    if amount>=5000:
        print("20% discount applied")
    else:
        print("customer is not eligible,because amount is lessthan 5000")
else:

    print("customer is not eligible,because not premium member")
    '''

#Task 5: ETL Pipeline Status Processor

status = input("enter the status: ")

match status:
    case "success":
        print(" ETL pipeline completed successfully")
    case "RUNNIMG":    
        print("ETL pipeline is currently running")
    case "FAILED":
        print("ETL pipeline failed")    
    case "PENDING":
        print("ETL pipeline is waiting")    
    case _:
        print("Unknown pipeline status")    
       