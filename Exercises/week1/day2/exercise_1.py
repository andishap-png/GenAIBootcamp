# # Exercise 1: Favorite Numbers

# Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers = set ([13, 17, 35, 62, 24])    

# Add two new numbers to the set.
my_fav_numbers.add(7)
my_fav_numbers.add(3)
print (my_fav_numbers)

# Remove the last number you added to the set
my_fav_numbers.remove(3)

# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = set([2, 8, 14, 26, 41])

# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print (our_fav_numbers)

# # Exercise 2: Tuple

my_tuple = (1, 2, 3, 4, 5)
list1 = list(my_tuple)
list1.append(6)
print (list1)
new_tuple = tuple(list1)
print (new_tuple)

# Exercise 3: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
print (basket)

basket.remove("Blueberries")
print (basket)

basket.append("Kiwi")
print (basket)

basket.insert(0, "Apples")
print (basket)

print (basket.count("Apples"))

basket.clear()
print (basket)

# # Exercise 4: Floats

my_list = []
num = 1.5
while num <= 5.5:
    my_list.append(num)
    num += 0.5  
    my_list [-1] = int(my_list[-1]) if my_list[-1].is_integer() else my_list[-1]
print (my_list)

#Exercise 5: For Loop

for i in range(1, 21):  
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)    

# #Exercise 6: While Loop

user_name = input("Please enter your name: ")
while user_name .isdigit () == True:
    user_name = input("Please enter your name:")

print ("Thank you")

Exercise 7: Favorite Fruits

fave_fruits_list = input("Please enter your favorite fruits, separated by spaces: ")
user_fruit = input("Please enter a fruit: ")
if user_fruit in fave_fruits_list: 
    print ("You chose one of your favorite fruits! Enjoy!")
else:    print ("You chose a new fruit. I hope you enjoy")

#Exercise 8: Pizza Toppings

Toppings = ""
Toppings_list = []

while Toppings != "quit":
    Toppings = input("Enter a pizza topping (or 'quit' to finish): ")
    if Toppings != "quit":
        print(f"Adding {Toppings} to your pizza.")
        Toppings_list.append(Toppings)

print(f"Your pizza has the following toppings: {Toppings_list}")

total_price = 10 + 2.5 * len(Toppings_list)
print(f"The total price of your pizza is: ${total_price}")

#Exercise 9: Cinemax Tickets


Kid_counter = 0
Grownup_counter = 0
member_age = ""
family_members = int(input("How many family members? "))
for _ in range(family_members):
    print("Enter the age of each family member (or 'quit' to finish):")
    member_age = input("Enter your age (or 'quit' to finish): ")
    if member_age != "quit":
        member_age = int(member_age)
        if member_age > 3 and member_age < 12:
            Kid_counter += 1
        elif member_age >= 12:
            Grownup_counter += 1
