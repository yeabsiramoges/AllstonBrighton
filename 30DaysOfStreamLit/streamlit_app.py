import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from datetime import time, datetime

# menu options

options = ("Control Statement", "Write", "Slider")
add_sidebar = st.sidebar.selectbox("Menu Options", options)

if add_sidebar == "Control Statement":
    st.header('st.button')

    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

elif add_sidebar == "Write":
    #Text
    st.header("st.write")

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

elif add_sidebar == "Slider":
    st.header("st.slider")

    st.subheader("Slider")
    age = st.slider("How old are you?", 0, 130, 25)
    st.write("Im ", age, "years old")

    st.subheader("Range Slider")
    values = st.slider(
        "Select a range of values",
        0.0, 100.0, (25.0, 75.0)
    )
    st.write("Values: ", values)

    st.subheader("Range Time Slider")
    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30),time(12, 45))
    )
    st.write("Youre scheduled for:", appointment)

    st.subheader("Date-Time Slider")
    start_time = st.slider(
        "When do you start?",
        value=datetime(2023, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm"
    )
    st.write("Start Time: ", start_time)