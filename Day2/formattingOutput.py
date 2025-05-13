# name='John'
# age=30
# sal=5000.50
name,age,sal='John',30,5000.50

##### Approach1 #####
# print(name)
# print(age)
# print(sal)
# print(name,age,sal)


##### Approach2 #####
# print('Name is :',name)
# print('Age is :',age)
# print('Salary is :',sal)


##### Approach3 #####
# print("Name is:%s  Age is:%d  Salary is:%g" %(name, age, sal))


##### Approach4 #####   {}
print("Name is:{}  Age is:{}  Salary is:{}" .format(name,age,sal))
print("Age is:{}  Name is:{}  Salary is:{}" .format(age,name,sal))
