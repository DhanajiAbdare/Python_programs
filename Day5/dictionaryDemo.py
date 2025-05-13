# Example1 : Creating dictionary (key & value pair)
# mydict = {101:"x", 102:"y", 103:"z"}
# print(mydict)            # {101: 'x', 102: 'y', 103: 'z'}


# Example2 : Accessing items(values) from the dictionary
# mydict = {
#     "brand" : "Hyndai",
#     "model" : "i20",
#     "year" : 2021
#     }
# print(mydict["brand"])      # Hyndai
# print(mydict["model"])      # i10

# #Using get() function
# print(mydict.get("brand"))  # Hyndai


# Example3 : Change the values in dictionary
# mydict = {
#     "brand" : "Hyndai",
#     "model" : "i20",
#     "year" : 2020
#     }
# print(mydict)               # {'brand': 'Hyndai', 'model': 'i20', 'year': 2020}
# mydict["year"] = 2021       # new value
# print(mydict)               # {'brand': 'Hyndai', 'model': 'i20', 'year': 2021}


# Example4 : Reading items from the dictionary using looping statement
# mydict = {
#     "brand" : "Hyndai",
#     "model" : "i20",
#     "year" : 2020
#     }
# for i in mydict:
#     print(i)            # Prints only keys from the dictionary

# for i in mydict:
#     print(mydict[i])    # Prints only values from the dictionary

# for i in mydict.values():
#     print(i)              # Prints only values from the dictionary

# for x,y in mydict.items():
#     print(x,y)              # Print keys along with the values


# Example5 : Check key is existing in dictionary or not
# mydict = {
#     "brand" : "Hyndai",
#     "model" : "i20",
#     "year" : 2020
#     }
# if "model" in mydict:
#     print("exists")         # exixts
# else:
#     print("not exists")

# print("model" in mydict)      # True


# Example6 : Find number of items in dictionary
# mydict = {
#     "brand" : "Hyndai",
#     "model" : "i20",
#     "year" : 2020
#     }
# print(len(mydict))              # 3


# Example7 : Adding items to dictionary
# mydict = {
#     "brand" : "Hyndai",
#     "model" : "i20",
#     "year" : 2020
#     }
# mydict["color"]="red"
# print(mydict)           # {'brand': 'Hyndai', 'model': 'i20', 'year': 2020, 'color': 'red'}



# Example8 : Remove items (key & value) to dictionary
mydict = {
    "brand" : "Hyndai",
    "model" : "i20",
    "year" : 2020
    }
# mydict.pop("year")
# print(mydict)           # {'brand': 'Hyndai', 'model': 'i20'}

# del mydict["year"]
# print(mydict)           # {'brand': 'Hyndai', 'model': 'i20'}

# del mydict
# print(mydict)           # NameError: name 'mydict' is not defined.

# mydict.clear()
# print(mydict)             # {} (dictionary variable is present)


# Example9 : Copying dictionary
mydict1 = {
    "brand" : "Hyndai",
    "model" : "i20",
    "year" : 2020
    }
# Using copy function
# mydict2 = mydict1.copy()
# print(mydict2)          # {'brand': 'Hyndai', 'model': 'i20', 'year': 2020}

# Without using copy() function
mydict2 = mydict1
print(mydict2)          # {'brand': 'Hyndai', 'model': 'i20', 'year': 2020}