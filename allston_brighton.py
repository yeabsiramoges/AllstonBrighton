# Libraries
import streamlit as st

# Page Setup
st.set_page_config(layout="wide")

# Load Data
@st.cache_data
def load_images():
    images = {
        "county_map": "images/pop.png",
        "tract_maps": [],
        "percent_black": [],
        "income_maps": []
    }

    relative_file_path = "images/"
    file_extension = ".png"

    for year in range(2013, 2022):
        images["tract_maps"].append(relative_file_path + str(year) + file_extension)
        images["percent_black"].append(relative_file_path + str(year) + "_Percent_Black" + file_extension)
        images["income_maps"].append(relative_file_path + str(year) + "_Inflation_Adjusted_Income_and_Benefits" + file_extension)
    
    return images

# Sidebar Setup
options = (
    "County View",
    "Inflation Adjusted Income",
    "Percent Black",
)
add_sidebar = st.sidebar.selectbox("Menu Options", options)

# Sidebar Control Flow
if add_sidebar == "County View":
    st.title("County View")
    county_map = load_images()["county_map"]

    with st.expander("About"):
        st.write("Display overall map of county present day.")
    
    my_bar = st.progress(0)
    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1)
    
    st.image(county_map, width=750)

if add_sidebar == "Inflation Adjusted Income":
    st.title("Inflation Adjusted Income")
    income_maps = load_images()["income_maps"]

    with st.expander("About"):
        st.write("Display inflation adjusted income maps showing incremental changes.")
    
    my_bar = st.progress(0)
    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1)
    
    map_selector = st.slider("Select your year: ", 2013, 2021)

    st.image(income_maps[map_selector-2013], width=750)

if add_sidebar == "Percent Black":
    st.title("Percent Black")
    black_maps = load_images()["percent_black"]

    with st.expander("About"):
        st.write("Display percent black maps showing incremental changes.")
    
    my_bar = st.progress(0)
    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1)
    
    map_selector = st.slider("Select your year: ", 2013, 2021)

    st.image(black_maps[map_selector-2013], width=750)