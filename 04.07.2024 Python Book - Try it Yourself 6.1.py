tamiles = {"first_name":"Tamiles", 
		   "last_name":"Araujo", 
		   "age":18,
		   "city":"Embu das Artes"}
		   
print("The informations about my girlfriend are:")
for key,value in tamiles.items():
	print("The {0} is {1}".format(key,value))
