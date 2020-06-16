# 1.	Create three variables in a single a line and assign different 
# values to them and make sure their data types are different. Like one is 
# int, another one is float and the last one is a string.

a=10
b=10.14
c="Krishan"

print(type(a))
print(type(b))
print(type(c))

# 2. 	Create a variable of value type complex and swap it with 
# another variable whose value is an integer.

d= 50 + 3j  
print(type(d)) 

b=d   #here I swap the value of d with the b and then printed
print(b)

# 3 Swap two numbers using the third variable as the result name
#  and do the same task without using any third variable.
a1=10
b1=5
result=a1
a1=b1
b1=result
print(a1)   


# 4. 	Write a program to print the value given
#  by the user by using both Python 2.x and Python 3.x Version.

user1=input("Type your name???")
print(user1)
age1=int(input("Type your age???"))
print(age1)


# 6. 	Write a program to check the data type of the entered values. 
# HINT: Printed output should say -  The input value data type is: int/float/string/etc

a=10
b=10.14
c="Krishan"
d=True

print(f"The input value data type is: {type(a)}")
print(f"The input value data type is: {type(b)}")
print(f"The input value data type is: {type(c)}")
print(f"The input value data type is: {type(d)}")

# 7. 	If one data type value is assigned to ‘a’ variable and then a different data 
# type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?

a=5
a=6
print(a) 









