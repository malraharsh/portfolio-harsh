import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import time

'''
https://guides.github.com/features/mastering-markdown/
'''

# title header, subheader

 streamlit.video(data, format='video/mp4', start_time=0)
  streamlit.button(label, key=None)
  treamlit.checkbox(label, value=False, key=None)
  radio, seelectbox, multisleect, 
  slider, textinput, selectslider, textarea, betacolor,
  st.sidebar.selectbox
  

button, checkbox, radio, selectbox, multiob, slider






s = '''
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

__You *can* combine them__

'''

st.markdown(s)


st.title('My first apps')

st.write('Here our first attempt to create table') #can write everything, df

df = pd.DataFrame({'first column': [1, 2, 3, 4],
    'second column': [10, 30, 10, 40]})

st.dataframe(df)

#or
#df

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selecteds: ', option*10

img = Image.open("shapes.png")
data = np.asarray(img, dtype='int32')
st.image(data)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

x = st.slider('choose x', 0, 120, 20, step=10)  # 👈 this is a widget
st.write(x, 'squared is', x * x)


add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
st.write(add_selectbox)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write(add_slider)

with st.echo():
    st.write('This code will be printed')




progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(0):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()


with st.spinner('Wait for it...'):
    time.sleep(1)
    st.success('Done!')








my_placeholder = st.empty()

# Now replace the placeholder with some text:
my_placeholder.text("Hello world!")

# And replace the text with an image:
# my_placeholder.image(my_image_bytes)




import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time

fig, ax = plt.subplots()

max_x = 5
max_rand = 10

x = np.arange(0, max_x)
ax.set_ylim(0, max_rand)
line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
the_plot = st.pyplot(plt)

def init():  # give a clean slate to start
    line.set_ydata([np.nan] * len(x))

def animate(i):  # update the y values (every 1000ms)
    line.set_ydata(np.random.randint(0, max_rand, max_x))
    the_plot.pyplot(plt)

init()
for i in range(100):
    animate(i)
    time.sleep(0.1)




