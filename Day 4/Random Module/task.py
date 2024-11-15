import random

rand_num = random.randint(1, 10)

print("This is a test of what number " + str(rand_num))

head_or_tail = rand_num % 2

print("This is a test of what number " + str(head_or_tail))

if head_or_tail == 0:
    print("Head")
else:
    print("Tail")