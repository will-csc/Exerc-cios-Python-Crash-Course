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
		
class Admin(User):
	
	def __init__(self,first_name,last_name,age,gender,privileges):
		
		super().__init__(first_name,last_name,age,gender)
		self.privileges = Privileges(privileges)
			
class Privileges():
	
	def __init__(self,privileges=[]):
		self.privileges = privileges
		
	def show_privileges(self):
		print("Here are the set of privileges: ")
		for priv in self.privileges:
			print(priv)
		
		
privileges = ["can add post", "can delete post", "can ban user",]
administrator = Admin("William","Cesar",20,"Male",privileges)
administrator.privileges.show_privileges()
