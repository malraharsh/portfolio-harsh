import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
from streamlit import write

def do(text, size=2):
    return st.write('#'*size + f' **{text}** ')

def html(text):
    return st.markdown(text, unsafe_allow_html=True)

def image(name, width=300): 
    return st.image(name, width=width)

def text_to_link(text, link):
    return html(f'[__*{text}*__]({link})')

def icon_link(img, link):
    info = '''<a href="{}">
    <img src='{}' alt="HTML tutorial" style="width:42px;height:42px;">
    </a>'''.format(link, img)

    return html(info) 






