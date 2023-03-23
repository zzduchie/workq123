# Lists.py
#
# @ author: A. N. Other
# date: September 2016
# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]
# nested list
my_list = ["mouse", [8, 4, 6]]
 
my_list = ['p','r','o','b','e']
# Output: p
print(my_list[1])
# Output: o
print(my_list[3])
# Output: e
print(my_list[2])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,6]]
# Nested indexing
# Output: a
print(n_list[0][2])
# Output: 5
print(n_list[1][2])
# using negative indexing
# Output: e
print(my_list[-2])
# Output: p
print(my_list[-4])