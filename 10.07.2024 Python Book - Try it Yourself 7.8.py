sandwich_orders = ["Chicken Sandwich","Egg Sandwich","Seafood Sandwich"]
finished_sandwiches = []

for sandwich in sandwich_orders:
	print("I made your {}".format(sandwich))
	finished_sandwiches.append(sandwich)

print("The list of the sandwichs mades are: \n",
	  finished_sandwiches)
