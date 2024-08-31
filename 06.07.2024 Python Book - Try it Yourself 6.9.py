favorite_places = {"William":"Any place cool",
				   "Dad":"Home",
				   "Mother":"Grandmother's home",
				   "Tamiles":"Any place cool"
				  }
for key,value in favorite_places.items():
	print("{}: Hello {}! What's your favorite place?".format("Me",key))
	print("{}: My favorite place is {}\n".format(key,value))
