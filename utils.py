             #### TODO ####
## subset()
# Add Nine Nations of North America?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle

# load_data: loads and returns datasets
def load_data():

    geo_cnty = pickle.load(open('Datasets/geocnty.pkl', 'rb'))
    rep = pd.read_csv('Datasets/kaggle-presidential/rep_clean_county_facts.csv', dtype={'fips': str})
    dem = pd.read_csv('Datasets/kaggle-presidential/dem_clean_county_facts.csv', dtype={'fips': str})
    rep_st = pd.read_csv('Datasets/kaggle-presidential/rep_clean_state_facts.csv', dtype={'fips': str})
    dem_st = pd.read_csv('Datasets/kaggle-presidential/dem_clean_state_facts.csv', dtype={'fips': str})

    return geo_cnty, rep, dem, rep_st, dem_st

geo_cnty, rep, dem, rep_st, dem_st = load_data()

# subset: subsets the data to the filter and quantile the user wants
# bnw : Black and White
#     Select regions where Black and White individuals together are at least x% of the population.
# hnw : Hispanic and White
#     Select regions where Hispanic and White individuals together are at least x% of the population.
# percent : scalar, float or int (optional)
#     Percentage to filter by. See above on bnw and hnw filters. Must be in the range 0-100.
def subset(data, filt):
    """Subset a United States primary election DataFrame using one of the following filters:
    solid_blue, solid_red, swing :
        Select regions based on historical voting trends i.e. voting Democrat (blue), Republican (red), or neither (swing).
    northeast, midwest, south, west :
        Select regions based on their location within the United States.

    Parameters
    ----------
    data : pandas.DataFrame
        The data being subset. Should be one of rep, dem, rep_st, or dem_st.
    filt : str
        The name of the filter being applied. Should be one of:
        solid_blue, solid_red, swing, northeast, midwest, south, or west
    
    Returns
    -------
    data : pandas.DataFrame
        Subset of the original data with the filter applied.
    """
    assert filt in {
        'solid_blue', 'solid_red', 'swing', 'northeast', 'midwest', 'south', 'west'
        }, f"{filt} is not a valid filter for subset()."
    # if filt in {'bnw', 'hnw'}:
    #     assert percent is not None, "The bnw and hnw filters need a percent argument."
    #     assert 0 <= percent <= 100, "The percentage can't be less than 0 or greater than 100."
    #     if filt == 'bnw':
    #         bnw = data[(data.white + data.black) > percent]
    #         return bnw
    #     elif filt == 'hnw':
    #         hnw = data[(data.white + data.hispanic) > percent]
    #         return hnw
    if filt in {'solid_blue', 'solid_red', 'swing'}:
        if filt == 'solid_blue':
            solid_blue = ['California', 'Connecticut', 'Delaware', 'District of Columbia', 'Hawaii', 'Illinois', 'Maine', 'Maryland', 'Minnesota', 'New Jersey', 'New York', 'New Mexico', 'Oregon', 'Rhode Island', 'Vermont', 'Washington']
            blue_df = data["state"].isin(solid_blue)
            solid_blue_df = data[blue_df]
            return solid_blue_df
        elif filt == 'solid_red':
            solid_red = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'Georgia', 'Idaho', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'North Dakota', 'Oklahoma', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'West Virginia', 'Wyoming']
            red_df = data["state"].isin(solid_red)
            solid_red_df = data[red_df]
            return solid_red_df
        elif filt == 'swing':
            swing = ['Colorado', 'Florida', 'Iowa', 'Michigan', 'Nevada', 'New Hampshire', 'North Carolina', 'Ohio', 'Pennsylvania', 'Virginia', 'Wisconsin']
            swing_df = data["state"].isin(swing)
            swing_states_df = data[swing_df]
            return swing_states_df
    # Add US Census Regions
    elif filt in {'northeast', 'midwest', 'south', 'west'}:
        if filt == 'northeast':
            northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania']
            northeast_df = data["state"].isin(northeast)
            northeast_df = data[northeast_df]
            return northeast_df
        elif filt == 'midwest':
            midwest = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin', 'Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']
            midwest_df = data["state"].isin(midwest)
            midwest_df = data[midwest_df]
            return midwest_df
        elif filt == 'south':
            south = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'District of Columbia', 'West Virginia', 'Alabama', 'Kentucky', 'Mississippi', 'Tennessee', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas']
            south_df = data["state"].isin(south)
            south_df = data[south_df]
            return south_df
        elif filt == 'west':
            west = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming', 'Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']
            west_df = data["state"].isin(west)
            west_df = data[west_df]
            return west_df
    # Add Nine Nations of North America?


#### Nine Nations of North America ####
# https://en.wikipedia.org/wiki/The_Nine_Nations_of_North_America

# NN_new_england = ['Maine', 'New Hampshire', 'Vermont', 'Rhode Island', 'Massachusetts', 'Connecticut']
# foundry = 
# dixie = 
# breadbasket =
# islands = 
# mexamerica = 
# ecotopia = 
# empty_quarter = 

def choropleth(data, color):
    if np.any(data.columns == 'st_cnty'):
        level = 'county'
    elif not np.any(data.columns == "st_cnty"):
        level = 'state'
    if level == 'county':
        # assert np.any(data.columns == 'st_cnty'), """
        # No county level data detected in the given dataset.
        # Only the 'rep' and 'dem' dataframes have county level data. 
        # Use data.head() or data.columns to check columns."""

        fig = px.choropleth(
            data, color=color,
            hover_data={'st_cnty': True, 'fips': False},
            geojson=geo_cnty, locations='fips', 
            color_continuous_scale= px.colors.sequential.ice_r,
            scope="usa")
        fig.update_traces(marker_line_width=0.2, marker_opacity=1)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_geos(
        showsubunits=True, subunitcolor="black", subunitwidth=0.5
        )
    elif level == 'state':
        # assert not np.any(data.columns=="st_cnty"), """
        # No state level data detected in the given dataset.
        # Only the 'rep_st' and 'dem_st' dataframes have state level data. 
        # Use data.head() or data.columns to check columns."""

        fig = px.choropleth(
            data,
            color=color,
            locations='st_abbrev',
            locationmode="USA-states",
            color_continuous_scale= px.colors.sequential.ice_r,
            scope="usa")
    
    return fig


# def heatmap(data):
#     sns.heatmap(data.corr(),cmap='vlag', center=0)