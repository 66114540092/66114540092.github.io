
#streamlit run streamlit/app03.py

import streamlit as st
s = st.subheader ('ไม่บอก')
p = st.write('ไม่บอก')
banner = st.markdown("![Goku Stare](https://tenor.com/view/goku-stare-goku-stare-xenoverse2-xenoverse2stare-gif-26924756)")
text = st.text_input('prompt: ')
if text:
    st.image('https://picsum.photos/400/200')
    st.write(f'กำลังไม่บอก...."{text}"')
    b = st.button('ไปต่อบ่....')