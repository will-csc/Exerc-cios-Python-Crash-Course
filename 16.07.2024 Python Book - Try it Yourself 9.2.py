class Restaurant():
	
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name}")
		print(f"And your cuisine type is {self.cuisine_type}")
		
	def open_restaurant(self):
		print("The restaurant is open")

my_restaurant = Restaurant("William's","Brazilian Cuisine")
Lolla_Osteria = Restaurant("Lolla Osteria","Italian Cuisine")
Aspro_Alogo = Restaurant("Aspro Alogo","Greece Cuisine")

restaurantes = [my_restaurant,Lolla_Osteria,Aspro_Alogo]
for restaur in restaurantes:
	restaur.describe_restaurant()
