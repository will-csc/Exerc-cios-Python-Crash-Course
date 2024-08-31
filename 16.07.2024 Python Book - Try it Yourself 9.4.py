class Restaurant():
	
	def __init__(self,restaurant_name,cuisine_type,number_served=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served
		
	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name}")
		print(f"And your cuisine type is {self.cuisine_type}")
		
	def open_restaurant(self):
		print("The restaurant is open")
		
	def set_number_served(self,numb):
		self.number_served = numb
		print(f"The number of dishes serveds is {numb}")
		
	def increment_number_served(self,numb):
		print(f"The number of dishes served before is {self.number_served}")
		self.number_served += numb
		print(f"The number of dishes served after the increase is {self.number_served}")
		
restaurant = Restaurant("William's","Brazilian Cuisine")
restaurant.set_number_served(20)
restaurant.increment_number_served(20)
