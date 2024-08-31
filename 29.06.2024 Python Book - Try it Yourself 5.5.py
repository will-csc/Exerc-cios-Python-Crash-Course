def points_earned(alien_color):
	if alien_color == "green":
		print("The player just earned 5 points")
	elif alien_color == "yellow":
		print("The player just earned 10 points")
	elif alien_color == "red":
		print("The player just earned 15 points")

[points_earned(color) for color in ["yellow","green","red"]]
