def make_album(author,album_name,tracks=None):
	album = dict(singer=author,album=album_name)
	if tracks:
		album['tracks'] = tracks
	return album

author = ""
album_name = ""
condicao = len(author) < 1 and len(album_name) < 1
while condicao:
	author = input("Enter the name of the singer: \n")
	album_name = input("Enter the album name of the singer: \n")	
	
	condicao = len(author) < 1 and len(album_name) < 1
	if condicao:
		opcao = input("Deseja desistir?: \n")
		if len(opcao) > 0:
			exit()
	
albums = make_album(author,album_name)
print(albums)
