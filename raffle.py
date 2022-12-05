import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import snowflake.connector
from urllib.error import URLError
from wordcloud import WordCloud, ImageColorGenerator
import random
import time
from io import BytesIO

st.title('🎰 RAFFLE 🧧')

add_selectbox = st.sidebar.text('Powered by: MPoint Analytics LLC.\n© Copyright 2022')

def cloud(kids):
    temp_kids=[x for x in kids]
    random.shuffle(temp_kids)
    text = ','.join(temp_kids)
    colormap='magma'
    colormap='winter'
    wc = WordCloud(background_color="white", colormap=colormap,
    max_font_size=150, random_state=42, width=800, height=400)

    # generate word cloud
    wc.generate(text)

    # create coloring from image
    #image_colors = ImageColorGenerator(image)

    # show the figure
    #plt.figure(figsize=(10,5))
    #fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [5, 4]})
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.imshow(wc, interpolation="bilinear")

    #for ax in axes:
    ax.set_axis_off()
    placeholder=st.empty()
    placeholder.pyplot(fig)
    
    
    if st.button("START"):
        #st.write(kids)
        temp_kids=[x for x in kids]
        placeholder.empty()
        while len(temp_kids)>0:
            random.shuffle(temp_kids)
            text = ','.join(temp_kids)
            colormap='magma'
            colormap='winter'
            wc = WordCloud(background_color="white", colormap=colormap,
            max_font_size=150, random_state=42,width=800, height=400)

            # generate word cloud
            wc.generate(text)

            # create coloring from image
            #image_colors = ImageColorGenerator(image)

            # show the figure
            #plt.figure(figsize=(12,6))
            #fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [5, 4]})
            fig, ax = plt.subplots(figsize = (12, 6))
            ax.imshow(wc, interpolation="bilinear")

            #for ax in axes:
            ax.set_axis_off()
            #placeholder=st.empty()
            placeholder.pyplot(fig)
            if len(temp_kids)>=20:
                time.sleep(0.5)
            else:
                time.sleep(1)
            placeholder.empty()
            winner=temp_kids[0]
            temp_kids.pop()
        st.snow()
        placeholder.pyplot(fig)
        #st.write(winner)
        #kids.remove(winner)
        #st.write(kids)


def main():
    #orig_kids=['Christoff','Cedrick','Chaskell','Jazmine','Nathan','Arianne','Rye','TJ','Annika','Amielle','Aaron','Aedan','Angel','Niall','Ardene','Jasen','Shiloh','Abbey','Ava','Rayden','Edmund','Matt','Luigi','Abby']
    #orig_kids=['Abbey','Aedan','Annika','Ardene','Arianne','Ava','Cedrick','Christoff','Edmund','Jasmine','Luigi','Nathan','Niall','Raiden','Rye','TJ']
    adults=['LJ','Toby','Alvin','Martin Wife','Martin','Nini','Val','Dulce','Nanay ni My','Lolo Dad','Lola Mah','V','Khetz','Tomas','Bing','Josie','Juvy','Andrew','Ness','Nyer','Ednil','Raymund','Jeanet','Shayla','Karlo','Jerose','Ricky','Leah','Chris','Apol','Myra','Alvin R','Tere','Ron']
    #cloud(orig_kids)
    cloud(adults)
                            

if __name__=="__main__":
  main()

