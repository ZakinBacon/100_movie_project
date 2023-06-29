from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_webpage = response.text

# Creating our Soup
soup = BeautifulSoup(yc_webpage, "html.parser")

# Finds the titles
all_movies = soup.find_all(name="h3", class_="title")

# gets the text of all the movies
movie_titles = [movie.getText() for movie in all_movies]

# Getting the movies in reverse order since it comes in from 100-1 and we want 1-100
movies = movie_titles[::-1]

# Printing all of the movies to the Txt file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

