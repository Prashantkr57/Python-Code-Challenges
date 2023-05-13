import random
from random import randint

rand_list = []
for i in range(25):
    rand_list.append(random.randint(0, 100))

print(rand_list)
rand_list.sort()
print(f"The max and min in list is: {rand_list[0]} and {rand_list[-1]}")
#print(max(rand_list))
#print(min(rand_list))