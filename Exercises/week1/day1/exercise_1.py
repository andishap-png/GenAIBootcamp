# Exercise 1: Print the following output using one line of code:

print ("hello world\nhello world\nhello world\nhello world")


# Exercise 2
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).
print ((99 ** 3) * 8) 

# Exercise 3
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare
5 < 3 False
3 == 3 True
3 == "3" False
"3" > 3 TypeError 
"Hello" == "hello" False

#Exercise 4: Your computer brand
computer_brand = "Apple"
print (f"I have a {computer_brand} computer")

#Exercise 5: 
name = "Andi"
age = 35
shoe_size = 5
info = (f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}.")
print (info)

# Exercise 6: A & B
a = 10
b = 5
if a > b:
    print ("Hello World")

#Exercise 7: Odd or Even
number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("That number is even!")
else:
    print("That number is odd!")

# Exercise 8: What’s Your Name?
name = "Andi"
user_name = input("What's your name? ")
if user_name == name:
    print ("That is a nice name!")
else:
    print ("That is a nice name too!")

#Exercise 9: Tall Enough to Ride a Roller Coaster
user_height = int(input("Please enter your height in inches: "))    
if user_height >= 145:
    print ("You are tall enough to ride!")
else:    
    print ("Sorry, you need to grow some more to ride.")

