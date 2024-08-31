sandwich_orders = ["Chicken Sandwich","Egg Sandwich","Seafood Sandwich",
				   "Pastrami Sandwich","Pastrami Sandwich","Pastrami Sandwich"]
finished_sandwiches = []
print("deli has run out of pastra\n")
while "Pastrami Sandwich" in sandwich_orders:
	sandwich_orders.remove("Pastrami Sandwich")

for sandwich in sandwich_orders:
	print("I made your {}".format(sandwich))
	finished_sandwiches.append(sandwich)

print("The list of the sandwichs mades are: \n",
	  finished_sandwiches)
