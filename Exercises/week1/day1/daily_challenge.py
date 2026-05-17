user_str = input("Please enter a string exactly 10 characters long: ")

if len (user_str) < 10: 
    print ("String not long enough.")
if len (user_str) > 10:
    print ("String too long.")
if len (user_str) == 10:
    print ("String is exactly 10 characters long.")

print (f"First character: {user_str[0]}")
print (f"Last character: {user_str[-1]}")


constructed_str = ""
for char in user_str:
    constructed_str += char 
    print (constructed_str)