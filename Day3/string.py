# Create a string variable

# Example1 : Ways of creating string variable
# s='welcome'
# s="welcome"
# s=str('welcome')
# s=str("welcome")

# Creating empty string variables
# name=''
# name=""
# name=str()


# Example2 : How the string memory is changed
# mutable - cannot change the value of the variable
# immutable - can change the value of the variable
# string is immutable - if the value(id) is changed after update then it is immutable

# str1="welcome"
# print(id(str1))               #2491334479344 --memory location id of str1
# str1=str1+"to python"
# print(id(str1))               #2491336492816 --memory location id of str1


# Example3 : + and * with strings
# str="python"
# print(str+"programming")      #concatination/joining - pythonprogramming
# print(str*5)                  # print string value multiple times - pythonpythonpythonpythonpython


# Example4 : Slicing []
# starting index is 0
# ending index is 1

# str="welcome"
# print(str[1:3])         # el
# print(str[:6])          # welcom -here starting index is 0 by default
# print(str[2:])          # lcome  -here ending index is till the string ends
# print(str[1:-1])        # elcom - here last 1 char removed
# print(str[1:-2])        # elco - here last 2 char removed


# Example5 : ord() and chr() functions
# print(ord('A'))         # 65 - returns the Ascii code of the character
# print(chr(65))          # A - returns the character represented by Ascii number


# Example6 : max()  min()  len()
# print(max('abc'))       # c - returns last character
# print(min('abc'))       # a - returns first character
# print(len('abc'))       # 3 - returns string length


# Example7 : in , not in operators - returns True/False
# s="welcome"
# print('come' in s)            # True
# print('lome' in s)            # False
#
# print('come' not in s)        # False
# print('lome' not in s)        # True


# Example8 : String comparison   (True/False)
# print("tin" == "tie")           # False
# print("free" != "freedom")      # True
# print("arrow" > "aron")         # True
# print("right" >= "left")        # True
# print("teeth" < "tee")          # False
# print("yellow" <= "fellow")     # False
# print("abc" > "")               # True


# Example9 : Testing strings     (True/False)
# s="welcome to python"
# print(s.isalnum())                 # False (If the string contains the number, returns True)
# print("welcome".isalpha())         # True
# print("2012".isdigit())            # True
# print("first number".isidentifier())    #False (String is not contains any python keywords)
# print(s.islower())                 # True
# print("WELCOME".isupper())         # True
# print(" ".isspace())               # True


# Example10 : Searching for substrings
# s="welcome to python"
# print(s.endswith("thon"))           # True
# print(s.startswith("good"))         # False
# print(s.find("come"))               # 3 (returns position
# print(s.find("become"))             # -1 (Not present in the main string)
# print(s.count("t"))                 # 2 (Returns the number of occurrences of substring the string)


# Example11 : Converting string
# s="string in PYTHON"
# s1= s.capitalize()
# print(s1)               # String in python
#
# s2= s.title()
# print(s2)                # String In Python
#
# s3 = s.lower()
# print(s3)               # string in python
#
# s4 = s.upper()
# print(s4)               # STRING IN PYTHON
#
# s5 = s.swapcase()
# print(s5)               # STRING IN python
#
# s6 = s.replace("in", "on")
# print(s6)               # strong on PYTHON


# Example12 : Reverse the string
# Method1
s = "welcome"
rev_str =""
for i in s:                             # last value of s is assign to i then its previous & so on
    rev_str = i + rev_str               # e  em  emo  emoc   emocl   emocle   emoclew
print("Reversed string is :", rev_str)  # emoclew

# Method2 (Using slicing operator)
s = "welcome"
rev_str = s[::-1]       # s[0:7:-1]
print(rev_str)          # emoclew