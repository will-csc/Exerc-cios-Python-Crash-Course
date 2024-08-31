def show_magicians():
	magicians = []
	for i in range(qnt_magicians):
		magician = input(f"Digite o nome do mágico {i+1}: ")
		magicians.append(magician)
	for magic in magicians:
		print(magic)
		
def make_great(magicians):
	for magic in magicians:
		magicians[magicians.index(magic)] += " the Great"

qnt_magicians = int(input("How many magician do you want to add?: \n"))

copy_magicians = magicians
make_great(copy_magicians)
show_magicians(copy_magicians)
