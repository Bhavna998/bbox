# DATE : 13- MAY-2021

# EXERCISE 1:
# what will the following code produce
num = 27
num = 15
num = 8
print(num + num + num)  # the value of num is updated in every step

# EXERCISE 2:
# what's wrong with the following script
num = 7
# 2num = 4 # this shows an error because of some naming rule
_num = 6
_num2 = 9

# EXERCISE 3:
# fix the last line so that is outputs the sum of 1 and 2. please do not change the first two lines . only last line
x = "18"
y = 5
# print(x + y)  its shows typeError because x is a string
print(int(x) + y)

# EXERCISE 4:
# complete the script so that it print out the second item of the list
letters = ["u", "n", "w", "i", "r", "e", "d"]
print(letters[1])

# EXERCISE 5 :
# write a script so that it prints out list slice containing items d, e and f
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(letters[3:6])

# EXERCISE 6 :
# write a script so that it prints out the first three items of list 'letters'
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])

# EXERCISE 7:
# complete the script so that it prints out letters 'i' using negative indexing
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])

# EXERCISE 8 :
# Complete the script so that it prints out a list slice containing the last three items of list letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])

# EXERCISE 9 :
# complete the script so that it prints out a slice containing letters a, c, e, g and i.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# BOTH ARE SAME
print(letters[0:9:2])
print(letters[::2])

# EXERCISE 10 :
# create a script that generated and prints a list of numbers from 5 to 80.
list_1 = range(5, 81)
print(list(list_1))

# EXERCISE 11:
# Write a program to print first 10 numbers that sare divisible by 3 using range
my_range = range(0, 30, 3)
print(list(my_range))

# EXERCISE 12:
# Write a script so thai it removes duplicate items from the list
a = ["1", 1, "1", 2]
a = list(set(a))  # we need to convert list into set because set items cannot contain duplicate objects
print(a)

# EXERCISE 13:
# create a dictionary that contains the keys a and b and their respective values 1 and 2
d = {"a": 1, "b": 2}
print(d)

# EXERCISE 14:
# please complete the script so that it prints out the value of the key.
d = {"a": 1, "b": 2}
print(d["b"])

# EXERCISE 15:
# calculate the sum of the values of keys a and b
d = {"a": 1, "b": 2, "c": 3}
print("the sum of a and b is :", d["a"] + d["b"])

# EXERCISE 16 :
# Calculate the sum of all dictionary values.
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))  # use d.values method to print the sum of dictionary

# EXERCISE 17 :
# filter the dictionary by removing all items with a value of  greater than 1
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value > 1)
print(d)


# EXERCISE 18 :
# write the function that calculates acceleration given initial velocity v1, final velocity v2, start time t1 and the end time t2.
def acceleration(v1, v2, t1, t2):
    a = (v1 - v2) / (t1 - t2)
    return a


print("the total acceleration :", acceleration(0, 10, 0, 20))

# EXERCISE 19 :
# What will the following script output? please try to do this mentally if you can.
c = 1


def foo():
    return c


c = 3
print(foo())  # the output will be 3


# EXERCISE 20 :
# The following script throws a NameError in the last line saying that  c is not defined .
# please fix the function so that there is no error and the last line is able to print out the value of h.

def foo():
    global h
    h = 1
    return h


foo()
print(h)


# EXERCISE 21 :
# why is there an error in the code and how would you fix it

def foo(a=1, b=2):
    return a + b


# x = foo - 1 this line is an error
x = foo() - 1


# EXERCISE 22 :
# write a function that takes any string as input and returns the number of words for that string.
def count_words(strng):
    strng_list = strng.split(" ")
    return len(strng_list)


print(count_words("hey i am here"))


# EXERCISE 23 :
# write a function that takes any string as input amd returns the number of words for that string.
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)


print(count_words("word.txt"))


# EXERCISE 24 :
# write a function that takes a tect file as input and returns the number of words contained in the text file.
# please take into consideration that some words can be seperated by a comma with no space.
def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
        text = text.replace(",", "")
        string_list = text.split(" ")
        return len(string_list)


print(count_words("word.txt"))

# EXERCISE 25 :
# the following code is supposed to print out the square root of 9 , but it throws an error instead because another line before that is missing.
# please fix the script so that it prints out the square root of 9

import math

result = math.sqrt(9)  # we need to add import module
print(result)

# EXERCISE 26:
# create an english to portuguese translation program. the program takes a word from the user as input and translate it using the following dictionary
# as a vocabulary source

d = dict(weather='clima', earth='terra', rain='chuva')


def vocabulary(word):
    return d[word]


word = input("enter word :")
print(vocabulary(word))

# EXERCISE 27 :
# the code produces an error . please understand the error and try to fix it
# age = input("What's your age! ")  # this line produce an error because age takes  an input as string
age = int(input("What's your age! "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)

# EXERCISE 28 :
# print out the last name of the second employee
d = {"employees": [{"firstName": "john", "lastName": "doe"}, {"firstName": "komal", "lastName": "advani"},
                   {"firstName": "marry", "lastName": "berlin"}]}
print(d['employees'][1]['lastName'])

# EXERCISE 29 :
# please update the dictionary by changing the last name of the second employee from smith to smooth or whatever takes your fancy.
d = {"employees": [{"firstName": "john", "lastName": "doe"}, {"firstName": "komal", "lastName": "advani"},
                   {"firstName": "marry", "lastName": "berlin"}]}
d['employees'][1]['lastName'] = 'smooth'
print(d)

# EXERCISE 30 :
# please add a new employee to the dictionary
d = {"employees": [{"firstName": "john", "lastName": "doe"}, {"firstName": "komal", "lastName": "advani"},
                   {"firstName": "marry", "lastName": "berlin"}]}
d['employees'].append(dict(firstName='albert', lastName='bert'))
print(d)
