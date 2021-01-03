#PLEASE BE AWARE CODE IS A DUMMY AS OF THIS AND CAN ONLY TAKE 4 GENRES AS A USER INPUT WHILE FILTERING

from imdb import IMDb  
import pandas as pd  
import numpy as np

ia = IMDb()
top250Movies = ia.get_top250_movies()

#get top 20 Movies this way which returns lot of details including genres
top250Movies = [ia.get_movie(movie.movieID) for movie in top250Movies[:250]]
dataset=[ movie['title'] for movie in top250Movies ]

"""
Full list of genre types on IMDB
    Action
    Adventure
    Animation
    Biography
    Comedy
    Crime
    Drama
    Family
    Fantasy
    Film-Noir
    History
    Horror
    Music
    Musical
    Mystery
    Romance
    Sci-Fi
    Sport
    Thriller
    War
    Western

Filtering can be done through this, alternatively
#dataset_genre['action_1'] = dataset_genre['genresall'].str.count('Action')
#dataset_genre['crime_1'] = dataset_genre['genresall'].str.count('Crime')
#dataset_genre['drama_1'] = dataset_genre['genresall'].str.count('Drama')
#dataset_genre['thriller_1'] = dataset_genre['genresall'].str.count('Thriller')
#dataset_genre['western_1'] = dataset_genre['genresall'].str.count('Western')
#dataset_genre.columns=['Action','Crime','Drama','Thriller','War']
#dataset_frames.columns=['Titles','Genre_Action','Genre_Crime','Genre_Drama','Genre_Thriller','Genre_Western','genresall','IMDBScore']

"""

dataset=pd.DataFrame(dataset)
dataset_genre=[ movie['genres'] for movie in top200Movies]
dataset_genre=pd.DataFrame(dataset_genre)
dataset_genre = dataset_genre.fillna(value='')
dataset_genre['genresall']=''
dataset_genre['genresall'] = dataset_genre[[0,1,2,3]].astype(str).agg(''.join, axis=1)
dataset_genre=dataset_genre.drop([0,1,2,3],axis=1)
dataset_rating=[ movie['rating'] for movie in top200Movies]
dataset_rating=pd.DataFrame(dataset_rating)
dataset_frames=[]
dataset_frames=[dataset,dataset_genre,dataset_rating]
dataset_frames=pd.concat(dataset_frames,axis=1,sort=False)
dataset_frames = dataset_frames.fillna(value='')


while True:
    genre_selection = input('Tell me the genre Action/Crime/Drama/Thriller/Western: ')
    if genre_selection == 'Action':
        print('Hello those are the top200 IMDB action movies')
        referrer_index = dataset_frames['genresall'].str.contains('Action')
        action_movies = dataset_frames[referrer_index]
        action_movies=pd.DataFrame(action_movies)
        display(action_movies)
    elif genre_selection == 'Crime':
        print('Hello those are the top200 IMDB crime movies')
        referrer_index = dataset_frames['genresall'].str.contains('Crime')
        crime_movies = dataset_frames[referrer_index]
        crime_movies=pd.DataFrame(crime_movies)
        print(crime_movies)
    elif genre_selection == 'Thriller':
        print('Hello those are the top200 IMDB cthriller movies')
        referrer_index = dataset_frames['genresall'].str.contains('Thriller')
        thriller_movies = dataset_frames[referrer_index]
        thriller_movies=pd.DataFrame(thriller_movies)
        print(thriller_movies)
    elif genre_selection == 'Western':
        print('Hello those are the top200 IMDB western movies')
        referrer_index = dataset_frames['genresall'].str.contains('Western')
        western_movies = dataset_frames[referrer_index]
        western_movies=pd.DataFrame(western_movies)
        print(western_movies)
    else:
        print('something is wrong')

