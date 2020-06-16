# 1. 	Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

user= input("Enter any String???")

rev=user[ : : -1]
print(rev)


# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_lower():
    uppercase=0
    lowercase=0
    user_input=input("Enter any string with both the uppercase and lowercase characters: ")
    for c in user_input:
        if c.isupper():
            uppercase+=1
        elif c.islower():
            lowercase+=1
        else :
            pass
    print("No. of Upper case characters :", uppercase )
    print("No. of Lower case Characters :", lowercase)

upper_lower()

# 3.        Create a function that takes a list and returns a new list with unique
#  elements of the first list.

def unique_element(list1):
    unique_list=[] 
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    print("The Unique Elements are: " ,unique_list)

unique_element([1,2,3,4,2,4,6,24,24,52,1,3])

# 4.         Write a program that accepts a hyphen-separated sequence of words
#  as input and prints the words in a hyphen-separated
#   sequence after sorting them alphabetically.

#ans-hef-dfee-ad =sort this alphabetically with the hipen saperated.

user=input("Enter the name of the students enrolled in BOOTCAMP seperated by hypen: ")

names=[i for i in user.split("-")]
names.sort()
print("-".join(names))


# 5.         Write a program that accepts a sequence of lines as input and 
# prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

user=input("Enter (You Already are in my bad book!!!)--copy paste the sentaence  in the barcket : ")

x=user.upper()
print(x)



# 6.          Define a function that can receive two integral numbers in string 
# form and compute their sum and print it in console.

# integral number are those who donot have fraction and all.
# eg: 3,6,5,7,8

def two_integral_numbers():
    num1=input("Enter first integral number : ")
    num2=input("Enter second integral number : ")
    # print(type(num1))
    # print(type(num2))
    
    res=int(num1)+int(num2)
    print(res)
two_integral_numbers()

# 7.        Define a function that can accept two strings as input and 
# print the string with maximum length in console. If two strings have the same length, 
# then the function should print all strings line by line.

def two_string():
    str1=input("Enter first string: ")
    str2=input("Enter second string: ")

    if len(str1) > len(str2):
        print("The string with maximum length is :",str1)
    else:
        print("The string with maximum length is :",str2)

    print("The first string is: ",str1)
    print("The second string is: ",str2)



two_string()

# 8.        Define a function which can generate and 
# print a tuple where the value are square of numbers between 1 and 20.

def square():    
    l=list()   
    for i in range(1,21):
       l.append(i*2)
    print(tuple(l))

    print(type(tuple(l))) 

square()

# 9.         Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
limit=int(input("Enter any number between 1 to 20!!! : "))
def showNumbers(limit):
    for i in range(0,limit+1): 
                                
        
        if i%2==0:
            print(i," EVEN")
           
        elif i%2 !=0:
            print(i," ODD")

showNumbers(limit)

# 10. 	Write a program which can filter() to make a list
#  whose elements are even number between 1 and 20 ( both included)


number =[*range(1,21,1)]    
                           


e = lambda x: x % 2 == 0  

# Example of lamda
# x = lambda a, b: a * b
# print(x(5, 6))


lis= list(filter(e, number)) 
print(lis)                    
            
# 12. 	Write a function to compute 5/0 and use try/except to 
# catch the exceptions

def try_catch():
    try:
        x=(5/0)  
        print(x)
    except:
        print("Error dividing with zero!!!")
try_catch()


# 13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 


import operator    
from functools import reduce    
from builtins import list, list
from multiprocessing.dummy import list

list = [[1, 2, 3], [4, 5], [6, 7, 8]]  
print(type(list))
print(type(list[0]))  

joinlist = reduce(operator.add, list)  
print(joinlist)                        


for i in joinlist:
    print(i,end="")

#  14. 		
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
