favorite_languages = {
					'jen': 'python',
					'sarah': 'c',
					'edward': 'ruby',
					'phil': 'python',
					}

people_joining = ["William","Tamiles","Julio","Eliane","sarah"]
for people in people_joining:
	favorite_languages[people] = "Don't have any"
for key,value in favorite_languages.items():
	if value == "Don't have any":
		print("{} don't have any favorite language".format(key))
	else:
		print("The favorite languague of "+
			  "{} is {}".format(key,value))
