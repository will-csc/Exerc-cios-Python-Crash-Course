current_users = ["William","Tamiles","Eliane","Julio","Irani"]
new_users = ["William","Daiane"]

for user in new_users:
	if user in current_users:
		print("You have to find another username, this one: {} is".format(user) +
			  " already being used")
	else:
		print("The user name: {} is avaliable".format(user))
