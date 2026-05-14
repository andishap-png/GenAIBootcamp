#Write the following Python code to do the following (complete ALL of these using list comprehension).

#Given a list [1,2,3,4], print out all the values in the list.
for number in [1, 2, 3, 4, 5]:
    print (number)

#Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
print ([number * 20 for number in [1, 2, 3, 4, 5]])

#Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).
print ([name[0] for name in ["Elie", "Tim", "Matt"]])

#Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
print ([number for number in [1, 2, 3, 4, 5, 6] if number % 2 == 0])

#Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
print ([number for number in [1, 2, 3, 4] if number in [3, 4, 5, 6]])
#Given a list of words [“Elie”, “Tim”, “Matt”] return a new list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).
print ([name[::-1].lower() for name in ["Elie", "Tim", "Matt"]])

#Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).
print ([char for char in "first" if char in "third"])

#For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
print ([number for number in range(1, 101) if number % 12 == 0])

#Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).
print ([char for char in "amazing" if char not in "aeiou"])

#Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
print ([[i for i in range(3)] for j in range(3)])

#Generate a list with the value:
my_list = [list(range(10)) for x in range(10)]
print(my_list)