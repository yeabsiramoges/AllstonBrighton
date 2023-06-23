from urllib.request import urlopen

import json
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

from census import Census
from us import states

with open('/Users/yeabsiramoges/Documents/AllstonBrighton/geoJSON1990.geojson') as response:
    counties = json.load(response)


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

fig = ff.create_choropleth(fips=ab_dataframe.tract, 
                           scope=['Massachusetts'],
                           values=ab_dataframe.C17002_001E, 
                           title='NY Public Transit Use by County', 
                           legend_title='% Public Transit')
fig.layout.template = None
fig.show()