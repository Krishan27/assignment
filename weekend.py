# 1.Create a list of the 10 elements of four different types of Data Types 
# like int, string, complex and float.


x=[1,2,3,4,5,"krishan",3.14,(4+5j),4.5,"Consultadd"]
print(type(x)) 
print(len(x))    

# 2. 	Create a list of size 5 and execute the slicing structure 

x=[1,2,3,4,5]
print(len(x))   


rev=x[: :-1]   
print(rev)


# 3. 	Create a list of given structure and run 
# 	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
# Access list [600,  700]
# Access list [100, 300, 500, 600, 800]
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list [10]
# Access list [ ]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]  
print(type(x)) 


print(x[5][:4])


print(x[6:8])  


print(x[::2]) 


print(x[: : -1])


print(x[5][5][0]) 


print(x[:]) 

# 4. 	Create a list of thousand number using range and xrange 
# and see the difference between each other.

list=[*range(1,1001)]
print(list)


# 6. 	Write a program in Python to iterate through 
# the list of numbers in the range of 1,100 and 
# print the number which is divisible by 3 and a multiple of 2.

x=list(range(1,101))   

print(x)
print(type(x))
lis=[]

for i in x:
    if i%3==0:
        lis.append(i)
print(lis)

# 7. 	Write a program in Python to reverse a string and
#  print only the vowel alphabet if exist in the string with their index.


user=input("Enter any string of your choice ?? ")

lis=[]
for i in user:
    if i in "aeiouAEIOU":
        lis.append(i)
   

print(lis)

# 8. 	Write a program in Python to iterate through the string “hello my name is abcde” 
# and print the string which has even length of word.


def even_length_string(str):
    result=""
    for i in range(len(str)):   
        if i%2==0:               
          result+=str[i]
    return result

print(even_length_string("hello my name is abcde"))



# 10. 	Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number
#  is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list 
# and return the maximum out of the list.



def even_odd(user):
    even_list=[]
    odd_list=[]
    for i in user:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(even_list)
    print(odd_list)
even_odd([2, 5, 13, 17, 51, 62, 73, 84, 95] ) 

    # 11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement.
    #  Example: 12abcbacbaba344ab  
    #  Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

user=input("Enter any string that holdes character as well as the numbers : ")


wordfreq = []   
for w in user:
    wordfreq.append(user.count(w))  
print((list(zip(user, wordfreq))))

# 12.Generate and print another tuple whose values are even numbers
#  in the given tuple (1,2,3,4,5,6,7,8,9,10).

tup=(1,2,3,4,5,6,7,8,9,10)



list=[]
for i in tup:
    if i%2==0:
        list.append(i)
print(list)

tup1=tuple(list)
print(tup1)
print(type(tup1))

   






