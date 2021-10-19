# Gets the newest version of the df set, manipulates it and saves it to a csv file.
# %%
import requests
import pandas as pd

# Downloads the latest version of the df set
csv_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
req = requests.get(csv_url)
url_content = req.content

# Writes it to a file
csv_file = open('data_covid.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# Rename first column from 'iso_code' to 'iso3' (don't know why)
df = pd.read_csv('data_covid.csv')
df = df.rename(columns={"iso_code": "iso3"})

# Removes the rows of all continents incl. the world
df = df.drop(df[df.continent.isnull()].index) 

# Adds two features
df["percentage_of_people_vaccinated"] = df["people_vaccinated"] / df["population"] * 100
df["percentage_of_people_fully_vaccinated"] = df["people_fully_vaccinated"] / df["population"] * 100

df.to_csv('data_covid.csv', index=False)

print("Task completed successfully.")
# %%