import math

WHOLE_PIZZA = 8
FAMILY = 4

#we know each whole pizza is 8 slices
#and we know that we are feeding a family of 4

print("We are feeding a family of 4.")

#make the user aware how many people we are feeding

slices_needed = FAMILY * int(input("How many slices of pizza will everyone eat?"))

#ask how many slices everyone would like, multiply that by 4

pizzas_needed = math.ceil(slices_needed / WHOLE_PIZZA)

#divide that number by 8 and round up to find out how many whole pizzas we need

leftover_slices = slices_needed%WHOLE_PIZZA

#find out the remaining slices

print("You will need", int(pizzas_needed), "pizzas.\nThere will be", leftover_slices, "remaining slices.")

#Display to the user "You will need x pizzas. There will be y remaining slices."
