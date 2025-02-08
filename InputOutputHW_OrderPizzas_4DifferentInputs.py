import math

WHOLE_PIZZA = 8

#we know each whole pizza is 8 slices

person1 = int(input('How many slices of pizza will the first person eat?'))
person2 = int(input('How many slices of pizza will the second person eat?'))
person3 = int(input('How many slices of pizza will the third person eat?'))
person4 = int(input('How many slices of pizza will the fourth person eat?'))

#ask 4 different people how many slices they would like

slices_needed = person1 + person2 + person3 + person4

#add up how many slices everyone wanted

pizzas_needed = math.ceil(slices_needed / WHOLE_PIZZA)

#divide that number by 8 and round up to find out how many whole pizzas we need

leftover_slices = (pizzas_needed * WHOLE_PIZZA)%slices_needed

#find out the remaining slices. I had to change the formula for this one
#from the other python file I made because it wasn't working properly
#with the inputs 5 4 3 2 which I was using to test.

print("You will need",int(pizzas_needed), "pizzas.\nThere will be", leftover_slices, "remaining slices.")

#Display to the user "You will need x pizzas. There will be y remaining slices."
