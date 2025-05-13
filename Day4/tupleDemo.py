#Example1: Creating tuple
# mytuple = ()          #empty tuple
# print(mytuple)        #()

# mytuple = ("apple","banana","cherry")
# print(mytuple)        #('apple', 'banana', 'cherry')


#Example2: Access tuple items
# mytuple = ("apple","banana","cherry")
# print(mytuple[1])       #banana - here index starts from 0
# print(mytuple[-1])      #cherry


#Example3: Range of indexes
# mytuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
# print(mytuple[2:5])       #('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1])     #('orange', 'kiwi', 'melon')


#Example4: changing the tuple items (through list its possible)
# By default, tuple does not allow you to change the values bcoz it is immutable
# But there is work around (i.e. indirect process) as
# Convert tuple---->list(modify items)---->convert into tuple

# mytuple = ("apple","banana","cherry")
# # mytuple = ("apple",100,200)
# mylist = list(mytuple)      #convert tuple into the list
# mylist[0] = "orange"        #modify the item of index 0
# mytuple = tuple(mylist)     #again convert list into the tuple
# print(mytuple)              #('orange', 'banana', 'cherry')


#Example5: Reading tuple items using loop
# mytuple = ("apple","banana","cherry")
# for i in mytuple:
#     print(i)


#Example6 : Check if the item exists (Searching of item in tuple)
# mytuple = ("apple","banana","cherry")
# if "banana" in mytuple:
#     print("yes, banana is present")
# else:
#     print("no, banana is not present")


#Example7 : Tuple length - counting items in a tuple
# mytuple = ("apple","banana","cherry")
# print(len(mytuple))         #3


#Example8 : Add items to tuple - not possible bcoz tuple is immutable (cannot change the values/items)
# mytuple = ("apple","banana","cherry")
# mytuple[0] = "orange"         #TypeError: 'tuple' object does not support item assignment
# print(mytuple)


#Example9 : Copy tuple
# mytuple1 = ("apple","banana","cherry")
# mytuple2 = mytuple1
# print(mytuple2)                 #('apple', 'banana', 'cherry')


#Example10 : Removing items from the tuple - not possible bcoz tuple is immutable
# mytuple = ("apple","banana","cherry")
# mytuple.remove("apple")       # Invalid / It is not possible

# del mytuple
# print(mytuple)                  #NameError: name 'mytuple' is not defined. Did you mean: 'tuple'?


#Example11 : Joining / Combine tuple
# tuple1 = (10,20,30)
# tuple2 = ('a','b','c')
#
# tuple3 = tuple1 + tuple2
# print(tuple3)                   #(10, 20, 30, 'a', 'b', 'c')


#Example12 : Tuples comparison
tuple1 = (10,20,30)
# tuple2 = ('a','b','c')
tuple2 = (10,20,30)

if tuple1 == tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")