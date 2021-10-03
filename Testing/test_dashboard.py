import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from utils import *
sns.set_theme()

geo_cnty, rep, dem, rep_st, dem_st = load_data()

"""
# Testing Dashboard
Trying to get the run_streamlit.sh script to work!
"""

'''
## 1. Get to know your data
Let's take a first look at the primary election data. We have four DataFrames of interest: `rep`, `dem`, `rep_st`, and `dem_st`.
The first two, `rep` and `dem`, are the county-level primary election results for the Republican and Democrat primaries, respecitvely.
We also have their state-level counterparts, `rep_st` and `dem_st`, that are home to the same data except summarized at the state level.
Let's start by looking at `rep`. Use `rep.head()` to view the first 5 rows of the Republican primary DataFrame.
'''

st.write(rep.head())
dem
# st.write(plt.plot(x, y, label='blah'))

# st.write("""
# Create a plot to do XYZ...
# """)