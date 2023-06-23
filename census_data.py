import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import plotly.express as px

from census import Census
from us import states

API_KEY = "7a380eb1576dec7f290e40892fc84b4ceda20019"

census_client = Census(API_KEY)

# ABCDC stands for Allston-Brighton Community Development Corporation
# AB stands for Allston-Brighton

# Call Census API to get American Community Survey data from 2009-2021

ACS5_Years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009]
yearly_ab_census = []
census_fields = ('NAME', 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E')

for year in ACS5_Years:
    yearly_ab_census.append(census_client.acs5.state_county_tract(fields = census_fields,
                                        state_fips = states.MA.fips,
                                        county_fips = "*",
                                        tract = "*",
                                        year = year))


# Create dataframe
ab_dataframe = pd.DataFrame(yearly_ab_census[0])
print(ab_dataframe.head(2))
print("Shape: ", ab_dataframe.shape)

# Access Shapefile
ma_tract = gpd.read_file("https://www2.census.gov/geo/tiger/TIGER_RD18/STATE/25_MASSACHUSETTS/25/tl_rd22_25_tract.zip")

# Reproject to UTM (Universal Transverse Mecator) Zone 17N
ma_tract = ma_tract.to_crs(epsg = 32617)
print(ma_tract.head(2))
print("Shape: ", ma_tract.shape)

# Check shapefile projection
print("\nThe shapefile projection is: {}".format(ma_tract.crs))

# Create new GEOID row to make accessing counties easier
ab_dataframe["GEOID"] = ab_dataframe["state"] + ab_dataframe["county"] + ab_dataframe["tract"]

# Print head of dataframe
ab_dataframe.head(2)

# Remove unnecessary columns
ab_dataframe = ab_dataframe.drop(columns = ["state", "county", "tract"])

# Show updated dataframe
ab_dataframe.head(2)

# Check column data types for census data and shapefile
print("Column data types for census data:\n{}".format(ab_dataframe.dtypes))
print("\nColumn data types for census shapefile:\n{}".format(ab_dataframe.dtypes))

ab_merge = ma_tract.merge(ab_dataframe, on = "GEOID")

# Show result
print(ab_merge.head(2))
print('Shape: ', ab_merge.shape)

ab_poverty_tract = ab_merge[["STATEFP", "COUNTYFP", "TRACTCE", "GEOID", "geometry", "C17002_001E", "C17002_002E", "C17002_003E", "B01003_001E"]]

# Show dataframe
print(ab_poverty_tract.head(2))
print('Shape: ', ab_poverty_tract.shape)

# Dissolve and group the census tracts within each county and aggregate all the values together
# Source: https://geopandas.org/docs/user_guide/aggregation_with_dissolve.html
ab_poverty_county = ab_poverty_tract.dissolve(by = 'COUNTYFP', aggfunc = 'sum', numeric_only=True)

# Show dataframe
print(ab_poverty_county.head(2))
print('Shape: ', ab_poverty_county.shape)

# Get poverty rate and store values in new column
ab_poverty_county["Poverty_Rate"] = (ab_poverty_county["C17002_002E"] + ab_poverty_county["C17002_003E"]) / ab_poverty_county["B01003_001E"] * 100

# Show dataframe
ab_poverty_county.head(2)

fig = px.choropleth(ab_poverty_county,
                   geojson=ab_poverty_county.geometry,
                   locations=ab_poverty_county.index,
                   projection="mercator")

fig.update_geos(fitbounds="locations", visible=False)
fig.show()