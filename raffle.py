import numpy as np
import pandas as pd
import streamlit as st
import snowflake.connector
from urllib.error import URLError

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.title('🎁Wishlist 2022')
st.subheader('For gift ideas...')
add_selectbox = st.sidebar.text('Powered by: MPoint Analytics LLC.\n© Copyright 2022')
st.markdown('---')

def snow_connect():
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    return my_cnx
  
main_sql="""
select name, age, wishlist
from list_monito
order by name
"""

