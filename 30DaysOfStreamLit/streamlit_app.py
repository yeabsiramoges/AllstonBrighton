import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# menu options

options = ("Control Statement", "Write")
add_sidebar = st.sidebar.selectbox("Menu Options", options)

if add_sidebar == "Control Statement":
    st.header('st.button')

    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

elif add_sidebar == "Write":
    #Text
    st.write("st.write")

    #Italics and emojis
    st.write("Hello, *World!* :sunglasses:")

    #Numbers
    st.write(1234)

    #Dataframes
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    st.write(df)

    st.write("Below is a Dataframe: ", df, "Above is a dataframe.")

    df2 = pd.DataFrame(
        np.random.rand(200, 3),
        columns=['a', 'b', 'c']
    )
    c = alt.Chart(df2).mark_circle().encode(
        x = 'a', y = 'b', size='c', color = 'c', tooltip=['a', 'b', 'c']
    )
    st.write(c)