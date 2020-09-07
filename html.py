import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import time


# https://www.w3schools.com/html/html_styles.asp



# def html(text):
#     return st.markdown(text, unsafe_allow_html=True)


# h = '''
# <h1 style="background-color:powderblue;">This is a heading</h1>
# <h1 style="color:red;">This is a heading</h1>
# <h1 style="font-family:verdana;">This is a heading</h1>
# <h1 style="font-size:300%;">This is a heading</h1>
# <h1 style="text-align:center;">Centered Heading</h1>
# '''

# for i in h.splitlines():
#     html(i)

# st.write('done')



def html(text):
    return st.markdown(text, unsafe_allow_html=True)

img = 'shapes.png'
link = 'ads'
img = 'https://www.iconfinder.com/data/icons/social-media-free-13/32/Github_social_media_logo-512.png'

info = f'''<a href="{link}">
    <img src='{img}' alt="HTML tutorial" style="width:42px;height:42px;">
    </a>'''

info = f'''
> Hiii ii <br>
<img src={img} alt="Italian Trulli" style="width:42px;height:42px;">
'''

# html(info)

# st.image(img, width=300)

# st.radio(
#      "What's your favorite movie genre",
#      ('Comedy', 'Drama', 'Documentary'))

if st.button('Say hello', key='ae'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# st.checkbox('asd')

# st.selectbox(
#      'How would you like to be contacted?',
#      ('Email', 'Home phone', 'Mobile phone'))

# st.multiselect()


# multiob, slider
