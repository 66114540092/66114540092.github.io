
#streamlit run xtra01.py
import streamlit as st
page_bg_img = '''<style>
.stApp {
    background-image: url("https://pbs.twimg.com/media/EVPZSSzUUAIBswf?format=jpg&name=large");
    background-size: cover;       
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("My Webpage")
st.sidebar.header ("with")
st.sidebar.subheader("Beautiful Background Image")
with st.expander ('see my video?'):
    c = st.container()
    video_file = open('star.mp4', 'rb')
    video_bytes = video_file.read()
    c.write('This is my home.')
    c.video(video_bytes)
    c.write('this is my image')
    c.image('https://cdn.dribbble.com/userupload/11586052/file/original-38cdd3cb62b332868fc6d12d47a4cb5e.png?resize=752x.png')
