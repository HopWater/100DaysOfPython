# TypeError
# len(123)

# No TypeError
len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name_of_user")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name_of_user: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name_of_user: " + str(length_of_name))
