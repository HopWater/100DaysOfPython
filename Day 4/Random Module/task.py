import random

rand_num = random.randint(1, 10)

#print("This is a test of what number " + str(rand_num))

head_or_tail = rand_num % 2

#print("This is a test of what number " + str(head_or_tail))

if head_or_tail == 0:
    print("Heads")
else:
    print("Tails")



# random_integer = random.randint(1,10)
# print(random_integer)\
#
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(0,10)
# print(random_float)