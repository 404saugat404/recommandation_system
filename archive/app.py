import streamlit as st
import pickle
import pandas as pd
# movies_list=pickle.load(open('movies.pkl','rb'))
# movies_list=movies_list['title'].values
movies_list=pickle.load(open('movie_dictionary.pkl','rb'))
movies=pd.DataFrame(movies_list)
st.title("movie recommandations")

# option=st.selectbox(movies_list)

selectmovie_name=st.selectbox('search the movie',movies['title'].values)

if st.button('Recommand'):
    st.write(selectmovie_name)