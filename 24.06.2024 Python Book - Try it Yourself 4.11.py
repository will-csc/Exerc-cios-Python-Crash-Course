list_pizzas = ["pepperoni","cheddar","bacon"]
friend_pizzas = list_pizzas[:]

list_pizzas.append("chicken")
friend_pizzas.append("chocolate")

print("My Favorite Pizzas Are: ")
for pizza in list_pizzas:
	print(pizza)
print("\nMy friend’s favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)
