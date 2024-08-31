age = 70
if age < 2:
	print("You're a baby")
elif age in range(2,4):
	print("You're a toddler")
elif age in range(4,13):
	print("You're a kid")
elif age in range(13,20):
	print("You're a teenager")
elif age in range(20,65):
	print("You're an adult")
else:
	print("You're an elder")
