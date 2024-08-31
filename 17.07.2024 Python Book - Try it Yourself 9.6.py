class Restaurant():
	
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name}")
		print(f"And your cuisine type is {self.cuisine_type}")
		
	def open_restaurant(self):
		print("The restaurant is open")
		
class IceCreamStand(Restaurant):
	
	def __init__(self,restaurant_name,cuisine_type,flavors):
		
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors
		
	def display_flavors(self):
		print("The flavors are: ")
		for flav in self.flavors:
			print(flav)
	
Ice_restaurant = IceCreamStand("William's","Ice Cream",["Chocolate","Strawberry","Napolitano"])
Ice_restaurant.display_flavors()
