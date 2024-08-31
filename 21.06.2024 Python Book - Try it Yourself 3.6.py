deceased_cared_people = ["Tio Lu","Vó Osvaldo","Pelé"]

for person in deceased_cared_people:
	print("I have a dinner for you, cared Sr(a)",person)
	
print("\n",deceased_cared_people[2]," can't make to the dinner\n")
deceased_cared_people[2] = "Bisa"

for person in deceased_cared_people:
	print("I would like to invite you, cared Sr(a)",person)

print("\nWe found a bigger table, let's send invitations again\n")
deceased_cared_people.insert(0,"Michael Jackson")
deceased_cared_people.insert(1,"Lil peep")
deceased_cared_people.append("Chester")
for person in deceased_cared_people:
	print("I would like to invite you, cared Sr(a)",person)

print("\nI'm sorry to say, but we can only invite two persons to dinner")
for i in range(4):
	deceased_cared_people.pop()
for person in deceased_cared_people:
	print("Sr(a) ",person,"You're still invited")
