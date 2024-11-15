#This program outputs a random name based off a random generated number.
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_number = random.randint(0,4)

print(friends[rand_number])