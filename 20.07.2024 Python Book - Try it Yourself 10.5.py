while True:
	reason = input("Tel me a reason to love programming: \n")
	if reason == "q":
		break
	with open("reasons.txt","a") as f:
		f.write(reason+"\n")
	
	print("\n Type 'q' if you wanna quit \n")
