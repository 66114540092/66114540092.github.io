
#streamlit run streamlit/app04.py
import torch
import streamlit as st
from diffusers import DiffusionPipeline as DP
from PIL import Image
h = st.header ('Diffusion.AI')
s = st.subheader ('ไม่บอก')
p = st.write('ไม่บอก')
banner = st.markdown("![Goku Stare](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc0YzY2aThna3k1amVhNGN2ODhiaHg5ZWZjc3ptODQ1dHh4Y3ozZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SIuI7syOPvm1HAd5GF/giphy.gif)")
text = st.text_input('prompt: ')
if text:
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5",
                            torch_dtype=torch.float16)
    #st.image('https://picsum.photos/400/200')
        

    st.write(f'กำลังไม่บอก...."{text}"')

    b = st.button('ไปต่อบ่....')

    