import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNzc4NGNkNmNmNDA5YWNjZTNhMjM5YThkODQ4ZWI3YSIsInN1YiI6IjY1MmUwNDFlMGNiMzM1MTZmZWM5M2M2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8L0orXnb5xBdhC0D1HS_poeXFbuI1-hulMzTrzilzoQ"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]




def recommend(movie):
   movie_index=movies[movies['title']== movie].index[0]
   distances=similarity[movie_index]
   movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
   
   recommended_movies=[]
   posters=[]
   for i in movies_list:
      movie_id=movies.iloc[i[0]].movie_id
      #fetch poster api
      recommended_movies.append(movies.iloc[i[0]].title)
      posters.append(fetch_poster(movie_id))
   return recommended_movies,posters

movies= pickle.load(open('movies .pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
moviess=movies['title'].values
st.title('Movie Recommender System')

option=st.selectbox(
    'Select an option',
    (moviess)

)

if st.button('Recommend'):
    names,posters=recommend(option)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])