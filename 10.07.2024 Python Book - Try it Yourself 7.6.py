def get_value(val):
	val = int(val)
	if val in range(0,2):
		return "free"
	elif val in range(3,12):
		return 10
	elif val > 12:
		return 15

user_age = ""
while not user_age.isnumeric():
    user_age = input("What's your age?: \n")
    print("The ticket is going to cost: {}".format(get_value(user_age)))
        
