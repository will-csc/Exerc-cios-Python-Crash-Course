My_Name = "William"
Last_Name = "Carvalho"
Name = [My_Name,Last_Name]

if My_Name[0] == "W" and My_Name[-1] != "m":
	print("The name is written right, name:",My_Name)

print("The name written in lower case is: ",My_Name.lower())

My_Age = 20
if My_Age > 18:
	print("You're an adult")
if My_Age < 18:
	print("You're not an adult")
if My_Age >= 18:
	print("You could be an eldery")
if My_Age<= 12:
	print("You're a child")
	
if len(My_Name) > 5 or len(My_Name) < 10:
	print("You does have a name in the standards")

if My_Name in Name:
	print(My_Name," is on the name")
if "Cesar" not in Name:
	print("The name 'Cesar' is not in the name")
