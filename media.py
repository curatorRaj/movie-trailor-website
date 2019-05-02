import webbrowser


class Movie():
    # this class accept the movie title,trailer,poster image and youtube url
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailor_youtube
                 ):
        # this function make space in memory for functioning of class
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailor_youtube
		 
    def show_trailer(self):
        # this function show movie trailer in browser
        webbrowser.open(self.trailer_youtube_url)
