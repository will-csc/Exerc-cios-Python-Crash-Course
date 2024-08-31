def create_dict(country,population,fact):
	return dict(country = country,population = population,fact = fact)

cities = {"Embu das Artes":create_dict("Brazil",276.535,"Tourism city"),
		  "Taboão da Serra":create_dict("Brazil",293.652,"City for work"),
		  "Ribeirão Preto":create_dict("Brazil",711.825,"Brasilian Calinofornia"),
		  "São Paulo":create_dict("Brazil",(12.33*100000),"City for Work"),
		  "Seattle":create_dict("United States",749.256,"The city a wanna live")}

for city in cities.keys():
	print("Here's the facts about the {} city".format(city))
	for charac,value in cities[city].items():
		print("His {} is {}".format(charac,value))
	print("\n")

