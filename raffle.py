import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import snowflake.connector
from urllib.error import URLError
from wordcloud import WordCloud, ImageColorGenerator
import random
import time


st.title('🎰 RAFFLE 🧧')

add_selectbox = st.sidebar.text('Powered by: MPoint Analytics LLC.\n© Copyright 2022')

def cloud(kids):
    temp_kids=[x for x in kids]
    random.shuffle(temp_kids)
    text = ','.join(temp_kids)
    wc = WordCloud(background_color="white", colormap="magma",
    max_font_size=300, random_state=42)

    # generate word cloud
    wc.generate(text)

    # create coloring from image
    #image_colors = ImageColorGenerator(image)

    # show the figure
    plt.figure(figsize=(50,50))
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [5, 4]})
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    #axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")

    for ax in axes:
        ax.set_axis_off()
    placeholder=st.empty()
    placeholder.pyplot(fig)
    
    
    if st.button("START"):
        temp_kids=[x for x in kids]
        placeholder.empty()
        while len(temp_kids)>0:
            random.shuffle(temp_kids)
            text = ','.join(temp_kids)
            wc = WordCloud(background_color="white", colormap="magma",
            max_font_size=300, random_state=42)

            # generate word cloud
            wc.generate(text)

            # create coloring from image
            #image_colors = ImageColorGenerator(image)

            # show the figure
            plt.figure(figsize=(50,50))
            fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [5, 4]})
            axes[0].imshow(wc, interpolation="bilinear")
            # recolor wordcloud and show
            # we could also give color_func=image_colors directly in the constructor
            #axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")

            for ax in axes:
                ax.set_axis_off()
            #placeholder=st.empty()
            placeholder.pyplot(fig)
            time.sleep(1)
            placeholder.empty()
            winner=temp_kids[0]
            temp_kids.pop()
        placeholder.pyplot(fig)
        st.write(winner)
        kids.remove(winner)
        st.write(kids)
        


def main():
    orig_kids=['Christoff','Cedrick','Chaskell','Jazmine','Nathan','Arianne','Rye','TJ','Annika','Amielle','Aaron','Aedan','Angel','Niall','Ardene','Jasen','Shiloh','Abbey','Ava','Rayden','Edmund','Matt','Luigi','Abby']
    cloud(orig_kids)
                            

if __name__=="__main__":
  main()

