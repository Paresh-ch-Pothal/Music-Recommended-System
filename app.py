import streamlit as st
import numpy as np
import pandas as pd
import pickle

music_dict=pickle.load(open("music_dict.pkl","rb"))
new_df=pd.DataFrame(music_dict)
similarity=pickle.load(open("similarity.pkl","rb"))

def recommendSongs(song_name):
    li=[]
    song_index=new_df[new_df["song"] == song_name].index[0]
    distances=similarity[song_index]
    songList=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    for i in songList:
        newSong=new_df.iloc[i[0]]
        li.append((newSong.song , newSong.artist , newSong.link))
    return li

st.title("Music Recommended System")
selected_music_names=st.selectbox("Type Your Music Name",options=new_df["song"].values)
button=st.button("Recommend Music")
if button:
    recommendSong=recommendSongs(selected_music_names)
    st.subheader("Recommended Only For You")
    df = pd.DataFrame(recommendSong, columns=["Song", "Artist", "Song Link"])
    st.table(df)
