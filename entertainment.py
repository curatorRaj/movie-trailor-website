import media
import fresh_tomatoes


# toystory:movie title,storyline,poster image,youtube url
toystory = media.Movie(
  'toystory',
  'story of toy that come to life',
  'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
  'https://youtu.be/KYz2wyBy3kc'
   )


# infinitywar:movie title,storyline,poster image,youtube url
infinitywar = media.Movie(
   'Infinity War',
   'super hero moovie',
   'https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg',
   'https://youtu.be/6ZfuNTqbHE8'
   )


# thor:movie title,storyline,poster image,youtube url
thor = media.Movie(
   'thor ragnarok',
   'about super hero thor',
   'https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg',
   'https://youtu.be/ue80QwXMRHg'
    )


# kingsman:movie title,storyline,poster image,youtube url
kingsman = media.Movie(
   'Kingsman The Golden Circle',
   'the story of kingsman spy',
   'https://upload.wikimedia.org/wikipedia/en/f/fb/Kingsman_The_Golden_Circle.png',
   'https://youtu.be/6Nxc-3WpMbg'
    )


# fiftyshades:movie title,storyline,poster image,youtube url
fiftyshades = media.Movie(
   'Fifty shades of freed',
   'it is a romantic film',
   'https://upload.wikimedia.org/wikipedia/en/e/e5/Fifty_Shades_Freed_poster.png',
   'https://youtu.be/nJCc5HRPxYA'
    )


# sanju:movie title,storyline,poster image,youtube url
sanju = media.Movie(
   'Sanju',
   'the biography of sanjay dutt',
   'https://upload.wikimedia.org/wikipedia/en/e/e5/Sanju_-_Theatrical_poster.jpg',
   'https://youtu.be/1J76wN0TPI4'
   )


# set the movie that will be passed to media file
movies = [toystory, infinitywar, thor, kingsman, fiftyshades, sanju]


# open the webbrowser via the fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
