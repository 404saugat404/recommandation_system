import streamlit as st
import pickle
import pandas as pd




# movies_list=pickle.load(open('movies.pkl','rb'))
# movies_list=movies_list['title'].values



movies_list=pickle.load(open('movie_dictionary.pkl','rb'))
movies=pd.DataFrame(movies_list)

def recommand(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommanded_movies=[]

    for i in movie_list:
        recommanded_movies.append(movies.iloc[i[0]].title)
    return recommanded_movies

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("movie recommandations")

# option=st.selectbox(movies_list)

selectmovie_name=st.selectbox('search the movie',movies['title'].values)

if st.button('Recommand'):
    recommendations=recommand(selectmovie_name)
    for i in recommendations:
        
        st.write(i)