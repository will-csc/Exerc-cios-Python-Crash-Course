class User():
	
	def __init__(self,first_name,last_name,age,gender,login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.login_attempts = login_attempts
		
	def describe_user(self):
		attributes = vars(self)
		for atrib,atrib_value in attributes.items():
			print(f"The of {atrib} is {atrib_value}")
			
	def greet_user(self):
		print(f"Hello {self.first_name}, nice to have you here!")
	
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0
	
William = User("William","Carvalho",20,"Male",1)

for i in range(3):
	print(f"The total of logins attempts is {William.login_attempts}")
	William.increment_login_attempts()	

William.reset_login_attempts()
print(f"The total of login attemps have been reseted, now it is {William.login_attempts}")



