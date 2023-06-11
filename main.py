
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

len_list=len(names)
person_no=random.randint(0,len_list-1)
print(f"{names[person_no]} is going to buy the meal today!")


