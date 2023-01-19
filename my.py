import pandas as pd
import pickle
import streamlit as st
new_df=pickle.load(open('movie.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(move):
    move_index = new_df[new_df['title'] == move].index[0]

    move_list = sorted(list(enumerate(similarity[move_index])), reverse=True, key=lambda x: x[1])[1:6]
    l=[]
    for i in move_list:
        l.append(new_df.iloc[i[0]].title)

    return l

st.title('MOVIE RECOMMEND')
moves=st.selectbox('Which Movie do you like to see',(new_df['title'].values))
if st.button('Recommend'):
    movies=recommend(moves)
    for i in movies:
        st.write(i)
