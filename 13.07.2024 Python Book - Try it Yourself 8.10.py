def show_magicians(magicians):
	for magic in magicians:
		print(magic)
		
def make_great(magicians):
	for magic in magicians:
		magicians[magicians.index(magic)] += " the Great"

qnt_magicians = int(input("How many magician do you want to add?: \n"))
magicians = []
for i in range(qnt_magicians):
    magician = input(f"Digite o nome do mágico {i+1}: ")
    magicians.append(magician)

make_great(magicians)
show_magicians(magicians[:])

