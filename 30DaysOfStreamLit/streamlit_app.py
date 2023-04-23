import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time
import datetime

st.set_page_config(layout="wide")

# menu options

options = (
    "Control Statement", 
    "Write", 
    "Slider", 
    "Line Chart", 
    "Select Box",
    "Multi-Select",
    "Checkbox",
    "Profiling",
    "Latex",
    "Customization",
    "File Uploader",
    "Layout",
    "Progress",
    "Form")
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
    # Use select slider for choosing days
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
        value=(datetime.time(11, 30),datetime.time(12, 45))
    )
    st.write("Youre scheduled for:", appointment)

    st.subheader("Date-Time Slider")
    start_time = st.slider(
        "When do you start?",
        value=datetime.datetime(2023, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm"
    )
    st.write("Start Time: ", start_time)

elif add_sidebar == "Line Chart":
    st.header("Line Chart")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

elif add_sidebar == "Select Box":
    st.header("st.selectbox")
    option = st.selectbox(
        "What is your favorite color?",
        ("Blue", "Red", "Green")
    )
    st.write("Your favorite color is ", option)

elif add_sidebar == "Multi-Select":
    st.header("st.multiselect")
    options = st.multiselect(
        "What are your favorite colors",
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red']
    )
    st.write("You selected: ", options)

elif add_sidebar == "Checkbox":
    st.header("st.checkbox")
    st.write("What would you like to order?")

    icecream = st.checkbox("Ice cream")
    coffee = st.checkbox("Coffee")
    cola = st.checkbox("Cola")

    output_message = ""
    if icecream:
        output_message = "Great! Here's some more icecream"
    if coffee:
        output_message = "Okay, here's some coffee"
    if cola:
        output_message = "Here you go, more cola"
    st.write(output_message)

elif add_sidebar == "Latex":
    st.header("st.latex")
    st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
    
elif add_sidebar == "Customization":
    st.title('Customizing the theme of Streamlit apps')
    st.write('Contents of the `.streamlit/config.toml` file of this app')

    st.code("""
    [theme]
    primaryColor="#F39C12"
    backgroundColor="#2E86C1"
    secondaryBackgroundColor="#AED6F1"
    textColor="#FFFFFF"
    font="monospace"
    """)

    number = st.sidebar.slider('Select a number:', 0, 10, 5)
    st.write('Selected number from slider widget is:', number)

elif add_sidebar == "File Uploader":
    st.title("st.file_uploader")
    st.subheader("Input CSV")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.subheader("DataFrame")
        st.write(df)
        st.subheader("Descriptive Statistics")
        st.write(df.describe())
    else:
        st.info("Upload a CSV file")

elif add_sidebar == "Layout":
    st.title("How to layout a streamlit app")
    with st.expander("About this app"):
        st.write("This app shows the ways to layout an app.")
        st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
    
    st.sidebar.header("Input")
    user_name = st.sidebar.text_input("What is your name?")
    user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
    user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

    st.header("Output")
    column1, column2, column3 = st.columns(3)

    with column1:
        if user_name != '':
            st.write(f'👋 Hello {user_name}!')
        else:
            st.write('👈  Please enter your **name**!')

    with column2:
        if user_emoji != '':
            st.write(f'{user_emoji} is your favorite **emoji**!')
        else:
            st.write('👈 Please choose an **emoji**!')

    with column3:
        if user_food != '':
            st.write(f'🍴 **{user_food}** is your favorite **food**!')
        else:
            st.write('👈 Please choose your favorite **food**!')

elif add_sidebar == "Progress":
    st.title("st.progress")
    with st.expander("About"):
        st.write("Display progress of calculations.")
    
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

elif add_sidebar == "Form":
    st.title('st.form')
    st.header("1. Example of using with notation")
    st.subheader("Coffee Machine")

    