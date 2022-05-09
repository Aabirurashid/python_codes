import random

number_list=[19,11,21,28,35,42,49,56,63,70]
print("orignal list:",number_list)

random.shuffle(number_list)
print("list after first",number_list)

random.shuffle(number_list)
print("list after secound shuffle:",number_list)