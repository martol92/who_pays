import random

print("This app will randomly determine who will pay for the dinner")

names = input("Please enter a list of names separated by comma (Matt,Lauren,Tim)")
list_of_names = names.split(",")

number_of_persons = len(list_of_names)
 
who_pays = random.randint(1, number_of_persons)
pay_person = list_of_names[who_pays-1]

print(f"This evening {pay_person} pays for the dinner")