import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import snowflake.connector
from urllib.error import URLError
from wordcloud import WordCloud, ImageColorGenerator
import random


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.title('🎁RAFFLE')

add_selectbox = st.sidebar.text('Powered by: MPoint Analytics LLC.\n© Copyright 2022')

def cloud(text):
    
    wc = WordCloud(background_color="white", colormap="hot",
    max_font_size=300, random_state=42)

    # generate word cloud
    wc.generate(text)

    # create coloring from image
    #image_colors = ImageColorGenerator(image)

    # show the figure
    plt.figure(figsize=(480,360))
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    #axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")

    for ax in axes:
        ax.set_axis_off()
    st.pyplot(fig)

def main():
    st.write("# Text Summarization with a WordCloud")
    kids=['Christoff','Cedrick','Chaskell','Jasmine','Nathan','Arianne','Rye','TJ','Annika','Amielle','Aaron','Aedan','Angel','Niall','Ardene','Jasen','Shiloh','Abbey','Ava','Rayden','Edmund','Matt','Luigi','Abby']
    random.shuffle(kids)
    text = ','.join(kids)
    if text is not None:
        if st.button("START"):
            st.write(cloud(text), use_column_width=True)

if __name__=="__main__":
  main()

