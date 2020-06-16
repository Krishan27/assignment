# 1.	Create a list of the 10 elements of four different types of 
# Data Type like int, string, complex and float.

x=[1,2,3,4,5,"krishan",3.14,(4+5j),4.5,"Consultadd"]
print(type(x))  
print(len(x))    

# 2. 	Create a list of size 5 and execute the slicing structure 

x=[1,2,3,4,5]
print(len(x))  


rev=x[: :-1]   
print(rev)

# 3.  Write a program to get the sum and multiply of all the items in a given list.

list=[1,2,3,4,5]

def sum():
    result=0     
    for i in list:
        result+=i
    print(result)
sum()

list1=[1,2,3,4,5]
def mul():
    result=1  
    for j in list1:
        result*=j
    print(result)
mul()

# 4.   	Find the largest and smallest number from a given list.



x=[1,2,3,4,5,6,7,8,9,10]


print(max(x))
print(min(x))

# 5. 	Create a new list which contains the specified numbers after removing 
# the even numbers from a predefined list. 

list=[1,2,3,4,5,6,7,8,9,10]
lis2=[]
for i in list:
    if i%2!=0:
        lis2.append(i)

print(lis2)

# 6.	Create a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30 (both included).

list=[1,2,3,4,5,6,7,8,9,10]

list1=[*range(1,31)]
print(list1)

lis=[]

for i in list1:
    lis.append(i*i)

x=lis[:5]
y=lis[-5:]
z=x+y
print(z)

# 7.	Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

num1=[1,3,5,7,9,10]



num1[-1:]=[2,4,6,8,"krishan","sharma"]   
 
print(num1)


# 8.	Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

dict1={1:"krishan",
       2:"sharma"}
# print(type(dict1))

dict2={3:"abacs",
       4:"krihg",
       5:"loknnh"}


dict=dict1.update(dict2)
print(dict)   

print(dict1)


d_update={}
for d in (dict1,dict2):
    d_update.update(d)  

print(d_update)


# 9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

user=int(input("Input a number "))
d = dict()

for x in range(1,user+1):   
    d[x]=x*x    
print(d) 

# 10. 	Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number. Suppose the following input 
# is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

user=(input("Enter numbers separated by a commas??? : "))

list=user.split(",")
print(list)
print(type(list)) 
tup=tuple(list)
print(tup)
print(type(tup))
























