# Import relevant python scripts
import fresh_tomatoes
from media import Movie

# Create a list of favorite movies
movies = []

# Create movie objects to be displayed by fresh_tomatoes
movies.append(Movie("Ex Machina",
                    "http://spinoff.comicbookresources.com/wp-content/uploads/2015/04/Ex_Machina_FF_Poster2.jpg",
                    "http://www.youtube.com/watch?v=bggUmgeMCdc"))
movies.append(Movie("Hot Fuzz",
                    "http://cdn.gowatchit.com/posters/original/movie_47312.jpg",
                    "https://www.youtube.com/watch?v=ayTnvVpj9t4"))
movies.append(Movie("John Wick",
                    "https://s-media-cache-ak0.pinimg.com/736x/f1/a2/33/f1a233c713cf3fe12b57bf0fdd32e9bc.jpg",
                    "https://www.youtube.com/watch?v=uRkDFEXnZwA"))
movies.append(Movie("Kingsman: The Secret Service",
                    "http://orig04.deviantart.net/8657/f/2015/063/7/5/kingsman_poster_2_by_eaglesg-d8kf91c.png",
                    "https://www.youtube.com/watch?v=kl8F-8tR8to"))
movies.append(Movie("Live Die Repeat: Edge of Tomorrow",
                    "http://www.impawards.com/2014/posters/edge_of_tomorrow_ver9_xlg.jpg",
                    "https://www.youtube.com/watch?v=yUmSVcttXnI"))
movies.append(Movie("Misson: Impossible - Ghost Protocol",
                    "http://www.movie-poster-artwork-finder.com/posters/mission-impossiblemdashghost-protocol-poster-artwork-tom-cruise-jeremy-renner-paula-patton.jpg",
                    "https://www.youtube.com/watch?v=V0LQnQSrC-g"))
movies.append(Movie("Oblivion",
                    "http://img05.deviantart.net/af10/i/2013/321/4/1/oblivion_movie_poster_by_brblol-d6ujxmj.png",
                    "https://www.youtube.com/watch?v=XmIIgE7eSak"))
movies.append(Movie("Total Recall (2012)",
                    "http://imgdex.com/i/4fba8c7bb3413.jpg",
                    "https://www.youtube.com/watch?v=pPAy56Otr-E"))
movies.append(Movie("Tropic Thunder",
                    "http://www.impawards.com/2008/posters/tropic_thunder_ver4.jpg",
                    "https://www.youtube.com/watch?v=T-6YhRZowgc"))
movies.append(Movie("Up",
                    "http://thaliongraff.ca/wp-content/uploads/2012/10/UP-poster.jpg",
                    "https://www.youtube.com/watch?v=pkqzFUhGPJg"))
movies.append(Movie("Zoolander",
                    "http://media.tumblr.com/41beb184d2dedaa7050cafc03d96c173/tumblr_inline_mgh5mz4NQZ1qjuf55.jpg",
                    "https://www.youtube.com/watch?v=YtQq0T3ExLs"))

# Use the open_movies_page function in fresh_tomatoes.py to generate an HTML page listing the above movies
fresh_tomatoes.open_movies_page(movies)
