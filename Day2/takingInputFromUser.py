# Whatever data we pass through the console window that should consider as string type
# By default input() method take the data in string format
# Convert data using either int() or float() method

# num1=input("Enter first number:")
# num2=input("Enter second number:")
#
# print(type(num1))   #str
# print(type(num2))
#
# print(num1+num2)    #100200


###### Approach1 ######
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
#
# print(type(num1))   #int
# print(type(num2))
#
# print(num1+num2)    #300


###### Approach2 ######
# num1=input("Enter first number:")
# num2=input("Enter second number:")
#
# print(int(num1)+int(num2))    #300


###### Approach3 ######
num1=input("Enter first decimal number:")
num2=input("Enter second decimal number:")

print(type(num1))   #str
print(type(num2))

print(num1+num2)    #10.520.5
print(float(num1)+float(num2))  #31.0