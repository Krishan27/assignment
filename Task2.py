# 1.	Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.


num1=int(input("Enter a Number???"))  
if num1%3==0:
    print("Consultadd")




num2=int(input("Enter a Number???"))  
if num2%5==0:
    print("c")



num3=int(input("Enter a Number???"))  
if num3%3==0 and num3%5==0:      
    print("Consultadd Python Training")
    
    
# 2. 	Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition 
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average

user=int(input("Take any number from 1,2,3,4 or 5: "))

if user==1:
    print("Addition")
elif user==2:
    print("Subtraction")
elif user==3:
    print("Division")
elif user==4:
    print("Multiplication")
elif user==5:
    print("Average")


first=int(input("Enter first number???"))
second=int(input("Enter second number???"))

                 
user1=int(input("Choose any number from 1,2,3,4: "))
if user1==1:
    print(f"Addition: {first+second}")
elif user1==2:
    print(f"Subtraction: {first-second} ")
elif user1==3:
    print(f"Division: {first/second}")
elif user1==4:
    print(f"Multiplication: {first*second}")




first1=int(input("Enter first number???"))
second1=int(input("Enter second number???"))

user2=int(input("Choose any number from 1,2,3,4,5: "))
if user2==1:
    add=first1+second1
    print(f"Addition: {add}")
    if add<0:
        print("zsa")
elif user2==2:
    sub=first1-second1
    print(f"Subtraction: {sub} ")
    if sub<0:
        print("zsa")
elif user2==3:
    div=first1/second1
    print(f"Division: {div}")
    if div<0:
        print("zsa")
elif user2==4:
    mul=first1*second1
    print(f"Multiplication: {mul}")
    if mul<0:
        print("zsa")
elif user2==5:
    avg=(first1+second1)/2
    print(f"Average: {avg}")
    if avg<0:
        print("zsa")

#3. 	Write a program in Python to implement the given flowchart:

a=10
b=20
c=30

avg=(a+b+c)/3
print(avg)

if avg>a and avg>b and avg>c:
    print("Avg is higher than a, b and c")
elif avg>a and avg>b:
    print("average is higher than a and b")
elif avg>a and avg>c:
    print("average is higher than a and c")
elif avg>b and avg>c:
    print("average is higher than b and c")
elif avg>a:
    print("average is just higher than a")
elif avg>b:
    print("average is just higher than b")
elif avg>c:
    print("average is just higher than c")



# 4. 	Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”



var =int(input("Enter a number from 5 to -5 :"))                  
while var > 0:              
   print ("Current variable value : ", var)
   var = var -1
   if var == 0:
      break

print("Its over!") 


var1 =int(input("Enter a number from 5 to -5 :"))                  
while var1<=10 :              
   print ("Current variable value : ", var1)
   var1 = var1 +1
   if var1 == 5:
      continue

print("Its over!") 

# 5.   Write a program in Python which will find all such numbers which 
# are divisible  by 7 but are not a multiple of 5, between 2000 and 3200.

for num in range(2000,3200):
  if (num%7==0) and (num%5)!=0:
    print(num)
    
# 6. What is the output of the following code examples?

# x=123 
#   for i in x:
#     print(i)


x="123"
for i in x:
    print(i)



i = 0  
while i < 5: 
    print(i)     
    i += 1        
    if i == 3:     
        break
else:
    print("error")     





# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break             here the break spelling itself is wrong so shows an error


# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#        Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

counter=0
while counter<=6:
    
    if counter==3:
        counter=counter+1  
        continue
    if counter==6:
        break
    print(counter)
    counter+=1
    
# 8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

user=input("Enter the string mixed with the numbers???")

digit=0
letter=0
for character in user:
    if character.isdigit():
        digit=digit+1
    elif character.isalpha():
        letter=letter+1
   
print(user)    
print("Letters ", letter)
print("Digits ", digit)


# 9. Read the two parts of the question below: 
#  Write a program such that it asks users to “guess the lucky number”.
#   If the correct number is guessed the program stops, otherwise it continues forever. 

# Modify the program so that it asks users whether they want to guess again each time. 
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question
#  whether they want to continue guessing. The program stops if the user guesses the 
#  correct number or answers “no”. ( The program continues as long as a user has not
#   answered “no” and has not guessed the correct number)


winning_value=127 
game_over=False 


user_num=int(input("Guess your lucky number between 1 to 20??? :"))

while not game_over:
    if user_num==winning_value:
        print("Congratulations,You won the game!!!")
        game_over=True      

    else:
        print("You Lost the game !!!")
  
        user=input("Guess again??? answer in 'yes' or 'no' :")
        if user=="yes":
            user_num=int(input("Guess your lucky number between 1 to 20??? :"))
        elif user=="no":
            print("You Lost the game!!!")
            game_over=True  
            
            
# 10. Write a program that asks five times to guess the lucky number.
#  Use a while loop and a counter, such as
#            		counter=1
# 		While counter <= 5:
# 			print(“Type in the”, counter, “number”
# 			counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not).
#  If the correct number is guessed, the program outputs “Good guess!”, otherwise it 
#  outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.



winning_value=27 
game_over=False 
counter=0

user_num=int(input("Guess your lucky number between 1 to 20??? :"))

while not game_over:
    if user_num==winning_value:
        print("Good Guess!!!") 
        break
     
       
    elif user_num!=winning_value:
        user_num=int(input("Guess your lucky number between 1 to 20??? :"))
        counter=counter+1
        if counter==4:  
            print("Five wrong Guess!!! You ar out Game Ove!!!")
            break
        

              

            

  


  
            



                         











