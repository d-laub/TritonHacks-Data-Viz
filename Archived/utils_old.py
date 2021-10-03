#### TODO ####
## subset()
# Add US Census Regions
# Add Nine Nations of North America?
# New filters?

## choropleth
# plot features (winner, demographics, winner's vote %, etc.) of each county
# plot features of each state, need to summarize to state level
    # What % of counties each candidate won?
    # What % of vote each candidate won?
    # Which candidate won the state?
    # Demographics at state level?


import pandas as pd
import pickle

def unity(x, n):
    """Computes unity of voting on [0, 1] scale.

    Parameters
    ----------
    x: list-like
        Vote fractions for each candidate
    n: int
        Number of candidates
    
    Returns
    -------
    unity: float
        Measure of unity on [0, 1] scale

    Examples:
    Votes are perfectly split across candidates -> 0
    Votes are all for one candidate -> 1 
    """
    assert len(x) <= n, "More candidates input than assumed for uniform distribution."
    err = ((x-1/n)**2).sum()
    if len(x) > n: # Assume missing candidates received no votes
        err += (n - len(x))/n**2
    return err/(1 - 1/n)

# wrapper checklist: subset, choropleth, load_data, 

# geo, rep, dem = load_data();

# load_data: loads and returns datasets
# def load_data():
#     geo_cnty = pickle.load(open('geocnty.pkl', 'rb'))
#     rep = pd.read_csv('Datasets/kaggle-presidential/rep_clean_county_facts.csv')
#     dem = pd.read_csv('Datasets/kaggle-presidential/dem_clean_county_facts.csv')
#     return geo_cnty, rep, dem

# # subset: subsets the data to the filter and quantile the user wants
# # param data: the dataset to be subsetted
# # param filt: specific filters (can add more)
# # param threshold: ??
# def subset(data, filt, quantile=None):
#     assert filt in {'bnw', 'hnw', 'solid_blue', 'solid_red', 'swing'}, "Not an acceptable filter"
#     if filt in {'bnw', 'hnw'}:
#         assert quantile is not None, "Helpful description of what failed."
#         if filt == 'bnw':
#             # better filters - some counties may just be one (same with hnw)
#             bnw = data[(data.white + data.black) > (data.white + data.black).quantile(quantile)]
#             # bnw white > 80% or bnw black > 80% ? 
#             return bnw
#         elif filt == 'hnw':
#             hnw = data[(data.white + data.hispanic) > (data.white + data.hispanic).quantile(quantile)]
#             return hnw
#     if filt in {'solid_blue', 'solid_red', 'swing'}:
#         if filt == 'solid_blue':
#             solid_blue = ['California', 'Connecticut', 'Delaware', 'District of Columbia', 'Hawaii', 'Illinois', 'Maine', 'Maryland', 'Minnesota', 'New Jersey', 'New York', 'New Mexico', 'Oregon', 'Rhode Island', 'Vermont', 'Washington']
#             blue_df = data["state"].isin(solid_blue)
#             solid_blue_df = data[blue_df]
#             return solid_blue_df
#         elif filt == 'solid_red':
#             solid_red = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'Georgia', 'Idaho', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'North Dakota', 'Oklahoma', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'West Virginia', 'Wyoming']
#             red_df = data["state"].isin(solid_red)
#             solid_red_df = data[red_df]
#             return solid_red_df
#         else filt == 'swing':
#             swing = ['Colorado', 'Florida', 'Iowa', 'Michigan', 'Nevada', 'New Hampshire', 'North Carolina', 'Ohio', 'Pennsylvania', 'Virginia', 'Wisconsin']
#             swing_df = data["state"].isin(swing)
#             swing_states_df = data[swing_df]
#             return swing_states_df
    
#     # Add US Census Regions
#     # Add Nine Nations of North America?


#     else:
#         return None


# #### US Census Regions ####
# # https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

# # Northeast
# new_england = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']
# mid_atlantic = ['New Jersey', 'New York', 'Pennsylvania']

# # Midwest
# east_north_central = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']
# west_north_central = ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']

# # South
# south_atlantic = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'District of Columbia', 'West Virginia']
# east_south_central = ['Alabama', 'Kentucky', 'Mississippi', 'Tennessee']
# west_south_central = ['Arkansas', 'Louisiana', 'Oklahoma', 'Texas']

# # West
# mountain = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming']
# pacific = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']


# #### Nine Nations of North America ####
# # https://en.wikipedia.org/wiki/The_Nine_Nations_of_North_America

# # NN_new_england = ['Maine', 'New Hampshire', 'Vermont', 'Rhode Island', 'Massachusetts', 'Connecticut']
# # foundry = 
# # dixie = 
# # breadbasket =
# # islands = 
# # mexamerica = 
# # ecotopia = 
# # empty_quarter = 
    

# #  what's this??????
# #    (cnty_fts.white > 80) & (cnty_fts.voter_turnout < 0.5)

# # creates a map of the counties of the USA based on the data passed in
# # should adjust to state or county level? add level param?
# # data: data to be plotted
# # level: either county or state
# def choropleth(data, level):
#     if level == 'county':
#         fig = px.choropleth(data, geojson=geo_cnty, locations='fips', color='candidate',scope="usa")
#         fig.show()
#     else:
#         #fig = px.choropleth(data, geojson=geo_cnty, locations='fips', color='candidate',scope="usa")
#         fig.show()
    
#     # another way
#     # pip install plotutils
#     # https://python-plot-utilities.readthedocs.io/en/stable/api_docs/choropleth_map.html

# def barplot(x, y, palette="Blues_d"):
#     sns.barplot(x, y, palette="Blues_d")



# # # ?
# # def boxplot(data, x, y, hue):
# #      fig, ax = plt.subplots()
# #      sns.boxplot(data=data, x=x, y=y, hue=hue, ax=ax)
# #      st.write(fig)

# # # ?
# # def scatter(data, x, y, hue=None):
# #     sns.scatterplot(data, x, y , hue)
# #     plt.xlabel()
# #     plt.ylabel()
# #     plt.plot(x, y)
# #     st.write(plt.gcf())

# def heatmap(data):
#     sns.heatmap(data.corr(),cmap='vlag', center=0)