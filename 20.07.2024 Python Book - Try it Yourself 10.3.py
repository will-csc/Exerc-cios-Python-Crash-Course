name = input("Write your name: \n")
with open("guest.txt","a") as f:
	f.write(name + " \n")
	
with open("guest.txt","r") as f:
	print(f.read())
