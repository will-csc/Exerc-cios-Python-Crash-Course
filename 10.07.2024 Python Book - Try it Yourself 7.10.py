poll = {}
while True:
	name = str(input("What's your name?: \n"))
	place = str(input("If you could visit one place in the world, where would you go?: \n"))
	poll[name] = place
	
	if input("\nWould you like to end this poll? Types 'quit'\n").lower() == "quit": break

for name,place in poll.items():
	print("A place {} would like to visit is {}".format(name,place))
