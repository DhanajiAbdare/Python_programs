# Example1: How to create a list
# mylist1 = [10,20,30,40,50]
# mylist2 = ["apple","banana","cherry"]
# mylist3 = ["apple",10,"banana",20]
# mylist4 = list()     #empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist4)


# Example2: Accessing items from the list
# mylist = ["apple","banana","cherry"]        #Index starts from 0
#
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])       #access the last item
# print(mylist[-2])


# Example3: Range of indexes
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
# print(mylist[2:5])      #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])    #['orange', 'kiwi', 'melon']


#Example4: Change the item values from the list
# mylist = ["apple", "banana", "cherry"]
#
# print(mylist)           #['apple', 'banana', 'cherry']
# mylist[0] = "orange"    #this will change the values based on index
# print(mylist)           #['orange', 'banana', 'cherry']



#Example5: Read the list items using loop statements
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
# for i in mylist:
#     print(i)


#Example6: Check if the item is existed in the list or not
# mylist = ["apple", "banana", "cherry"]
#
# if "apple" in mylist:
#     print("Yes, apple is present")
# else:
#     print("No, apple is not present")


#Example7: List length (counting number of items in a list)
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))          #3


#Example8: Add items into the list (2 functions used- append() & insert())
# mylist = ["apple", "banana", "cherry"]
# mylist.append("orange")     #Adding new item at the end of the list
# print(mylist)               #['apple', 'banana', 'cherry', 'orange']
#
# mylist.insert(1,"melon")    #Add item somewhere in the middle of the list based on the index
# print(mylist)               #['apple', 'melon', 'banana', 'cherry', 'orange']


#Example9: Remove item from the list [3 methods available]
#pop() function
# mylist = ["apple", "banana", "cherry"]
# mylist.pop(0)       #Here we should specify the index to delete not the value
# print(mylist)       #['banana', 'cherry']

#del keyword
# mylist = ["apple", "banana", "cherry"]
# del mylist[2]       #Here del command removes single item based on the index
# print(mylist)       #['apple', 'banana']

#clear() function
# mylist = ["apple", "banana", "cherry"]
# mylist.clear()        #Clear all the items from the list but list variable is available
# print(mylist)         #[]


#Example10: Copy list  [2 functions - list() & copy()]
#list() function
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 =list(mylist1)
# print(mylist1)          #['apple', 'banana', 'cherry']
# print(mylist2)          #['apple', 'banana', 'cherry']

#copy() function
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 =mylist1.copy()
# print(mylist1)          #['apple', 'banana', 'cherry']
# print(mylist2)          #['apple', 'banana', 'cherry']


#Example11: Combine/Join the lists
# Using + operator
# list1 = ["a", "b", "c"]
# list2 = [1,2,3]
# list3 = list1+list2
# print(list3)             #['a', 'b', 'c', 1, 2, 3]

# Using looping statements
# list1 = ["a", "b", "c"]
# list2 = [1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)              #['a', 'b', 'c', 1, 2, 3]

# Using extend() function
# list1 = ["a", "b", "c"]
# list2 = [1,2,3]
# list1.extend(list2)
# print(list1)                #['a', 'b', 'c', 1, 2, 3]


#Example12 : List comparison
mylist1 = [10,20,30]
mylist2 = [10,20,30]

if mylist1 == mylist2:
    print("Lists are equal")
else:
    print("Lists are not equal")