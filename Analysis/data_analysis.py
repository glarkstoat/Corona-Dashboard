#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
sns.set(color_codes=True)
sns.set_context('paper')

data = pd.read_csv("../data/data_covid.csv")
print(data.info())
print(data.head())

# %% Checking syntactic accuracy

print(f"Unique continents: {data['continent'].unique()}")
print(f"Unique countries: {data['location'].unique()}")
print(f"Unique countries-abbriviations: {data['iso3'].unique()}")

# %%

# %%
data[(data["date"] == "2020-07-07") & (data["location"] == "Myanmar")]["total_deaths_per_million"]

# %%
data["new_people_vaccinated_smoothed_per_hundred"]
# %%
