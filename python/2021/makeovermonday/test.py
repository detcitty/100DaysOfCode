# https://ugoproto.github.io/ugo_py_doc/intro_to_data_world_in_python/

#%pylab inline
import pandas as pd
import os

# Import the datadotworld module as dw
import datadotworld as dw
# First
# Import the city council votes dataset
dataset = dw.load_dataset('stephen-hoover/chicago-city-council-votes')
all_dfs = dataset.dataframes
votes = all_dfs['alderman_votes']
print(votes.head())
print(votes.describe())
print(all_dfs)
print(dataset)
#print(dataset.head())

votes.groupby('make').sum()
