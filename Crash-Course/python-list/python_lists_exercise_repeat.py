for num in [1, 2, 3, 4]:
    print(num)

print([num * 20 for num in [1, 2, 3, 4]])

print ([word[0] for word in ["Elie", "Tim", "Matt"]])

print ([num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0])

print ([num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]])

([word[::-1].lower() for word in ["Elie", "Tim", "Matt"]])

print ([char for char in "first" if char in "third"])

print ([num for num in range(1, 101) if num % 12 == 0]) 

print ([char for char in "amazing" if char not in "aeiou"])

print ([[i for i in range(3)] for j in range(3)])

print([list(range(10)) for x in range(10)])
