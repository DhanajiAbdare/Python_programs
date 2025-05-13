# Example1 : Creating set
# myset = {"apple", "banana", "cherry"}
# print(myset)        # {'banana', 'cherry', 'apple'}


# Example2 : Accessing items from the set
# myset = {"apple", "banana", "cherry"}
# for i in myset:
#     print(i)


# Example3 : Value exists in set or not
# myset = {"apple", "banana", "cherry"}
# print("banana" in myset)        # True
# print("banana1" in myset)       # False


# Example4 : Adding items to the set
# 2 methods used: add()- add single item  &  update()- add multiple items
# myset = {"apple", "banana", "cherry"}
# # myset.add("orange")                # {'banana', 'apple', 'cherry', 'orange'}
# myset.update(["mango","grapes"])     # {'cherry', 'mango', 'apple', 'banana', 'grapes'}
# print(myset)


# Example5 : Find number of items in a set
# myset = {"apple", "banana", "cherry"}
# print(len(myset))         # 3


# Example6 : Remove the items from the set
# 2 methods are used : remove() & discard()
# myset = {"apple", "banana", "cherry"}
# myset.remove("banana")
# print(myset)                # {'apple', 'cherry'}
# myset.remove("xyz")         # KeyError: 'xyz' -(Imp)

# myset.discard("banana")
# print(myset)                 # {'apple', 'cherry'}
# myset.discard("xyz")         # Will not through any error


# Example7 : Clear all items from set
# myset = {"apple", "banana", "cherry"}
# myset.clear()
# print(myset)                   # set() -empty set
#
# del myset
# print(myset)                   # NameError: name 'myset' is not defined


# Example8 : Joining 2 sets - union() & update() functions are used
# set1 = {"a","b", "c"}
# set2 = {1,2,3}
# set3 = set1.union(set2)
# print(set3)                     # {'a', 1, 2, 3, 'b', 'c'}

# update() function
set1 = {"a","b", "c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)                      # {'a', 1, 2, 'c', 3, 'b'}


