import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
from streamlit import write
from Details import *
from utils import *

# activity = ['Design','About',]
# choice = st.sidebar.selectbox("Select Activity",activity)
# exec(open('main.py').read())


# def main():

st.title('Harsh Malra')

# st.title('Portfolio')
# st.header('          ... Portfolio')
# st.subheader('For Data Science')

image('me.jpg', width=200)



#Links
info = '''
Mobile: +91 9140624310 <br>
Email = malraharsh@gmail.com
'''
html(info)
html(link_all)

##############################################

do('About', 1)
st.write('*I am Harsh Malra; I am a machine-learning enthusiast. I like to learn state of the art technologies and understand them. I keen to learn new things, keep myself updated and improve constantly.*')

##############################################

do('Professional Skills and Interests:')

info = '''
>
- Python 
- Machine Learning Algorithms and Deep Learning
- Computer Vision
- Scikit-learn, Pandas, Numpy
- Competitive Programming 
- Visualization
    - Tableau
    - Matplotlib / Seaborn
'''

write(info)

##############################################
from Details import project_data

do('Blogs / Publications ->')

info = f'''
>
1. {title_blogs[0]}
2. {title_blogs[1]}
'''

button = st.button('Know More')

if not button:
    write(info)
else:
    st.button('Know Less')

    for title, img, link in data_blogs:


        # do(title, 3)
        text_to_link(title, link)
        st.image(img, width=300)
        write(' ')


##############################################
# Project


do('Project ->')
button = st.checkbox('More', value=True)

info = '''
>
1. Self-Driving Car using CNN and OpenCV: Made a self-driving car which learns initially by cloning the behavior of user (Behavioral cloning), then imitates its learning even to new environment (Dec 2019)
2. Invisible Cloak: Detecting the region of interest (ROI) and segmenting the color with background to give the illusion of invisibility (April 2020)
3. Predicting Survival Rate in Titanic:  In this, I first performed data analysis on the Titanic dataset to see which features are most prominent in predicting the survival rate and predicted based on it.
'''

if button:


    n = st.slider('No. of Projects', 3, 8, value=3)



    write(info)
    # more = st.button('Know More')
    more = st.checkbox('Know More')

    if more:

        project_title = st.selectbox('Select the Project ->', projects_titles)
            
        idx = projects_titles.index(project_title)
        img = project_data[idx]['image']
        info = project_data[idx]['info']
        do(project_title, 3)
        st.image(img, width=600)
        write(info)





##############################################

do('Education')
button = st.checkbox('More', value=True, key='1')

info = '''
>
**_College : _**
>>
- Bachelor of Technology (B.Tech CSE) 
- College - Amity University Lucknow (Uttar Pradesh, India)
- GPA - 8.56 CGPA 

>
**_School :_**
>>
- School – Kendriya Vidyalaya Aliganj (Lucknow)
- Percentage 12th - 92.8%
- Percentage 10th – 95%
'''
if button:
    write(info)

##############################################
# Achievements

do('Achievements')

info = '''
>
1. College Scholarship for good Academic Performance.
2. Got featured in Amity Social Media Pages for Navigation using Gestures project.
3. Cash price of Rs. 5,000 for excellence in boards.

'''

write(info)


##############################################

do('Other Relevant Info.')

info = '''
>
- **Languages**: English (Intermediate), German (Beginner), Hindi (Advanced)
- **Computer Skills**: Touch typing, Excel (Intermediate)
- **Hobbies**: Reading (Nonfiction), Programming, Exercise, Meditation
'''

write(info)


##############################################

# Contact Me
do('Contact Me -')


contacts = ('LinkedIn', 'Github', 'G-Mail', 'Mobile')

contact = st.radio("How do you want to Connect", contacts)


idx = contacts.index(contact)

idx2info = {0: [img_li, link_li],
            1: [img_github, link_github],
            # 2: [img_gmail, link_gmail],
            # 3: [img_mobile, link_mobile]
            }

img, link = idx2info[idx]

icon_link(img, link)
