import imdb
ia = imdb.IMDB()
search = ia.get_top250_movies()
for movies in search:
	print (movies)
