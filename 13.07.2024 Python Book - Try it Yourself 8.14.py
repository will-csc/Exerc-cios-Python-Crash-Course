def make_car(manufacturer,model,**others):
	car = {}
	car["manufacturer"] = manufacturer
	car["model"] = model
	for key,value in others.items():
		car[key] = value
	return car
		
my_car = make_car('subaru', 'outback', color='blue',motor=1.6)
print(my_car)
