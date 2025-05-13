# Conditional Staements
#     if    if..else     elif

#Example 1: Print a person is eligible for vote or not
# age>=18

# age=20
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


#Example 2:
# if False:
#     print("True condition")
# else:
#     print("False condition")


#Example 3:
# if 1:
#     print("True condition")
# else:
#     print("False condition")


#Example 4: Find the number is even/odd
# num=15
# if num%2==0:
#     print("Given number is Even")
# else:
#     print("Given number is Odd")


#Example 5: if else - In single line (ternary operator)
# num=10
# print("Even Number") if num%2==0 else print("Odd Number")


#Example 6: if else - Multiple statements in single line (ternary operator)
# a=5
# {print("Hello"),print("Python")} if a>=10 else {print("Hi"),print("Java")}


#Example 7: Multiple conditions using elif
weekno=10

if weekno == 1:
    print("Sunday")
elif weekno == 2:
    print("Monday")
elif weekno == 3:
    print("Tuesday")
elif weekno == 4:
    print("Wednesday")
elif weekno == 5:
    print("Thursday")
elif weekno == 6:
    print("Friday")
elif weekno == 7:
    print("Saturday")
else:
    print("Invalid week number")

