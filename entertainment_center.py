import fresh_tomato
import MovieProject


a_bronx_tale = MovieProject.Movie("A Bronx Tale",
                        "A story of a boy growing up in the bronx",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcTDDRNbI3UdAioxV5h4E1RyQysUFqIh5kUBNrYpJOgU2c08mD6h",
                        "https://www.youtube.com/watch?v=z50PjmZYS4A")
#print(toy_story.storyline)
                        
the_hunger_games = MovieProject.Movie("The Hunger Games",
                            "An economically divided society craves violence that is set as a distraction.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC",
                            "https://www.youtube.com/watch?v=LrXIG4oK7Ew")

the_dark_knight = MovieProject.Movie("The Dark Knight",
                                     "Batman must save Gotham from Joker",
                                     "https://usercontent2.hubstatic.com/13349231_f520.jpg",
                                     "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

good_will_hunting = MovieProject.Movie("Good Will Hunting",
                                       "A young adult discovers his true potential",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Good_Will_Hunting.png/220px-Good_Will_Hunting.png",
                                       "https://www.youtube.com/watch?v=z02M3NRtkAA")

lion_king = MovieProject.Movie("Lion King",
                               "A cub becomes a Lion",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg",
                               "https://www.youtube.com/watch?v=4sj1MT05lAA")

forrest_gump = MovieProject.Movie("Forrest Gump",
                                  "Meet Forrest, Forrest Gump",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                                  "https://www.youtube.com/watch?v=bLvqoHBptjg")
#print(the_dark_knight.storyline)                                     
#the_dark_knight.show_trailer()
movies =[a_bronx_tale, the_hunger_games, the_dark_knight, good_will_hunting, lion_king, forrest_gump]
fresh_tomato.open_movies_page(movies)
#print(MovieProject.Movie.VALID_RATINGS)
print(MovieProject.Movie.__doc__)
