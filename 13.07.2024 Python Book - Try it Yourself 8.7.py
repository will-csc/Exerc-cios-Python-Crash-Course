def make_album(tracks=None):
	author = input("Enter the name of the singer: \n")
	album_name = input("Enter the album name of the singer: \n")
	album = dict(singer=author,album=album_name)
	if tracks:
		album['tracks'] = tracks
	return album

for i in range(3):	
	albums = make_album(18)

print(albums)
