# def main():

st.write('Harsh Malra')

st.title('Portfolio')
st.header('... in Streamlit')
st.subheader('For Data Science')


img = Image.open("shapes.png")
data = np.asarray(img, dtype='int32')[:200, :200]
st.image(data)

def do(text, size=2):
    return write(''*size + ' ' + text)


def html(text):
    return st.markdown(text, unsafe_allow_html=True)


#Links

html(link_all)

##############################################

do('About')
st.write('I am Harsh Malra; I am a machine-learning enthusiast. I like to learn state of the art technologies and understand them. I keen to learn new things, keep myself updated and improve constantly.')

##############################################

do('Professional Skills and Interests:')

info = '''
- Python 
- Machine Learning Algorithms and Deep Learning
- Computer Vision
- Scikit-learn, Pandas, Numpy and Matplotlib
- SQL, Tableau / Visualization
- Competitive Programming 
    - ad
'''

write(info)

##############################################
from Details import project_data

do('Publications')

info = '''
>
Navigation using Gestures with Object Localization
<img src={img} alt="Italian Trulli" style="width:42px;height:42px;">

'''




##############################################
# Project

info = '''
1. Self-Driving Car using CNN and OpenCV: Made a self-driving car which learns initially by cloning the behavior of user (Behavioral cloning), then imitates its learning even to new environment (Dec 2019)
2. Invisible Cloak: Detecting the region of interest (ROI) and segmenting the color with background to give the illusion of invisibility (April 2020)
3. Predicting Survival Rate in Titanic:  In this, I first performed data analysis on the Titanic dataset to see which features are most prominent in predicting the survival rate and predicted based on it.
'''


projects_titles = ['Navigation using Gestures with Object Localization',
    'Playing Tekken with Body'
    ]


do('Project')


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

info = '''
>
- Bachelor of Technology (B.Tech CSE) 
- College - Amity University Lucknow (Uttar Pradesh, India)
- GPA – 8.56 CGPA 

>> - Schooling
- School – Kendriya Vidyalaya Aliganj (Lucknow)
- Percentage 12th – 92.8%
>>> - Percentage 10th – 95%
'''

write(info)

##############################################

do('Other Relevant Info.')

info = '''
>
- Languages: English (Intermediate), German (Beginner), Hindi (Advanced)
- Computer Skills: Touch typing, Excel (Intermediate)
- Hobbies: Reading (Nonfiction), Programming, Exercise, Meditation
'''

write(info)


def show(img):
    img = Image.open(img)
    data = np.asarray(img, dtype='int')
    return st.image(data, output_format='png')

##############################################

# Contact Me
do('Contact Me -')


contacts = ('LinkedIn', 'Github', 'G-Mail', 'Mobile')

contact = st.radio("How do you want to Connect", contacts)

def icon_link(img, link):
    info = '''<a href="{}">
    <img src='{}' alt="HTML tutorial" style="width:42px;height:42px;">
    </a>'''.format(link, img)

    return html(info) 

idx = contacts.index(contact)

idx2info = {0: [img_li, link_li],
            1: [img_github, link_github],
            # 2: [img_gmail, link_gmail],
            # 3: [img_mobile, link_mobile]
            }

img, link = idx2info[idx]

icon_link(img, link)



# if __name__ == '__main__':
#     main()

