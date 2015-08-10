# Movie Class - Stores catalogue information about your favorite movies

class Movie(object):
    def __init__(self,
                 title="Movie Title",
                 poster_image_url="no_poster.jpg",
                 trailer_youtube_url="https://www.youtube.com/watch?v=0xojO-4VFPw"):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
