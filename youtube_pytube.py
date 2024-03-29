import streamlit as st 
from pytube  import YouTube
import base64
from io import BytesIO

def main():
    path = st.text_input("Coloque aqui a URL do video")
    options = st.selectbox("selecione o tipo de download", ("audio","auta_resolução","baixa_resolução" ))
    
    if st.button("download"):
        video_object=YouTube(path)
        st.write("Video Title:" +  str(video_object.title))
        st.write(" Number of views:" + str(video_object.views))
        if options == "audio":
             video_object.streams.get_audio_only().download()
        elif options == "auta_resolução":  
             video_object.streams.get_highest_resolution().download()
        elif options == "baixa_resolução":  
             video_object.streams.get_lowest_resolution().download()        
    if st.button("view"):
        st.video(path)


if __name__ == '__main__':
    main()
