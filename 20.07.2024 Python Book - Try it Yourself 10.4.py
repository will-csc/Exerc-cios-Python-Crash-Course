User = ""
while not User:
	User = input("What's your name?: \n")

print(f"I'm, happy for you be here {User}")
with open("guest_book.txt","a") as f:
	f.write(f"The {User} was here \n")
	
