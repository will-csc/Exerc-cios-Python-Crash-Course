deceased_cared_people = ["Tio Lu","Vó Osvaldo","Pelé"]

for people in deceased_cared_people:
	print("I have a dinner for you, cared Sr(a)",people)
	
print(deceased_cared_people[2]," can't make to the dinner")
deceased_cared_people[2] = "Bisa"

for people in deceased_cared_people:
	print("I would like to invite you, cared Sr(a)",people)

print("We found a bigger table, let's send invitations again")
deceased_cared_people.insert(0,"Michael Jackson")
deceased_cared_people.insert(1,"Lil peep")
deceased_cared_people.append("Chester")
for people in deceased_cared_people:
	print("I would like to invite you, cared Sr(a)",people)

