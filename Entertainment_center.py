import media
import fresh_tomatoes

#Create Movie instances for each movie
toy_story = media.Movie("Toy Story",
                        "This is a story about a boy and his toys coming to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "A Marine in an alien planet",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=5PSNL1qE6VY")

trolls = media.Movie("Trolls",
                        "Poppy and Branch set off on a journey to rescue their friends",
                         "https://upload.wikimedia.org/wikipedia/en/a/ad/Trolls_%28film%29_logo.png",
                         "https://www.youtube.com/watch?v=xyjm5VQ11TQ")

school_of_rock = media.Movie("School of Rock",
                             "Music to learn in school",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

chennai_express = media.Movie("Chennai Express",
                              "A Man's trip to fulfil his late grandfather's wishes",
                              "https://upload.wikimedia.org/wikipedia/en/1/1b/Chennai_Express.jpg",
                              "https://www.youtube.com/watch?v=1thZbOzzTHs")

frozen = media.Movie("Frozen",
                        "Princess Anna helps her sister Queen Elsa to control her power",
                         "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=TbQm5doF_Uc")


movies = [toy_story, avatar, trolls, school_of_rock, chennai_express, frozen]
fresh_tomatoes.open_movies_page(movies) 
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)


