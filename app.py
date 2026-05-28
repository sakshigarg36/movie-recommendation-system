import streamlit as st
from PIL import Image
import pickle
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values



st.header('MOVIE RECOMMENDATION SYSTEM')
image=Image.open('312c530a-d083-48a5-8263-65d7b3a2f2a3.jfif')

st.image(image,caption='movies are dream that you can watch')

selectvalue = st.selectbox("Select a movie from the dropdown", movies_list)


def recommend(movie):
    try:
        
        index = movies[movies['title'] == movie].index[0]
        
        distances = sorted(
            list(enumerate(similarity[index])),
            reverse=True,
            key=lambda x: x[1]
        )
        
        recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
        return recommended_movies
    except IndexError:
        return ["No recommendations available"]  


if st.button("Show Recommendation"):
    movie_names = recommend(selectvalue)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
    with col2:
        st.text(movie_names[1])
    with col3:
        st.text(movie_names[2])
    with col4:
        st.text(movie_names[3])
    with col5:
        st.text(movie_names[4])
     
