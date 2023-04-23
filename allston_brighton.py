# Libraries
import streamlit as st

# Page Setup
st.set_page_config(layout="wide")

# Load Data
@st.cache_data
def load_images():
    images = {
        "county_map": "images/pop.png",
        "tract_maps": []
    }

    relative_file_path = "images/"
    file_extension = ".png"

    for year in range(2011, 2022):
        images["tract_maps"].append(relative_file_path + str(year) + file_extension)
    
    return images

# Sidebar Setup
options = (
    "County View",
    "Yearly Tract Maps",
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

if add_sidebar == "Yearly Tract Maps":
    st.title("Yearly Tract Maps")
    tract_maps = load_images()["tract_maps"]

    with st.expander("About"):
        st.write("Display yearly tract maps showing incremental changes.")
    
    my_bar = st.progress(0)
    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1)
    
    map_selector = st.slider("Select your year: ", 2011, 2020)

    st.image(tract_maps[map_selector-2010], width=750)
    pass