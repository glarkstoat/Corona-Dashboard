#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
sns.set(color_codes=True)
sns.set_context('paper')

data = pd.read_csv("../data_covid.csv")
print(data.info())
print(data.head())

# %% Checking syntactic accuracy

print(f"Unique continents: {data['continent'].unique()}")
print(f"Unique countries: {data['location'].unique()}")
print(f"Unique countries-abbriviations: {data['iso3'].unique()}")

# %%
plt.rcParams["figure.figsize"] = (23,12)
fig=plt.figure()
fig.suptitle('General Information', fontsize=20, fontweight='bold')

plt.subplot(241)
sns.histplot(data["total_cases"]) # california, texas and ny are top-3
plt.xticks(rotation=90, fontsize=7)

plt.subplot(242)
sns.histplot(data["new_cases_smoothed"]) # most are handeled by the fbi

plt.subplot(243)
sns.histplot(data["total_deaths"]) # roughly 3/4 of cases are solved

plt.subplot(244)
sns.histplot(data["new_deaths_smoothed"]) # most are carried out using handgut, revolver, pistol
plt.xticks(rotation=90)

plt.subplot(245)
sns.histplot(data["total_cases_per_million"]) # in most cases the relationship was not determined
plt.xticks(rotation=90)

plt.subplot(246)
sns.histplot(data["new_cases_smoothed_per_million"]) # sharp rise in 2020

plt.subplot(247)
sns.histplot(data["new_deaths_smoothed_per_million"]) # pretty even spread
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
# %%
sns.histplot(data[data["date"] == "2021-12-02"]["new_cases_smoothed_per_million"].dropna()) 

sns.histplot(data[""]) # sharp rise in 2020

# %%
