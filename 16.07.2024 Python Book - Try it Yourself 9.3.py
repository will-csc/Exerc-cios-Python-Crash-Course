class User():
	
	def __init__(self,first_name,last_name,age,gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		
	def describe_user(self):
		attributes = vars(self)
		for atrib,atrib_value in attributes.items():
			print(f"The of {atrib} is {atrib_value}")
			
	def greet_user(self):
		print(f"Hello {self.first_name}, nice to have you here!")

William = User("William","Carvalho",20,"Male")
Julio = User("Julio","Carvalho",50,"Male")
Eliane = User("Eliane","Carvalho",51,"Female")

users = [William,Julio,Eliane]
for user in users:
	user.greet_user()
	user.describe_user()
	print()
