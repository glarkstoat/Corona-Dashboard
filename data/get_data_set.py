# Gets the newest version of the data set, manipulates it and saves it to a csv file.
# %%
import requests
import pandas as pd
import os
import pywintypes
from win10toast import ToastNotifier

# Windows notification
toast = ToastNotifier()
toast.show_toast("Covid Data Update", "The update has been started", duration=30)
os.chdir(r"C:\Users\chris\Documents\GitHub\Corona-Dashboard\data")

# Downloads the latest version of the data set
csv_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
req = requests.get(csv_url)
url_content = req.content

# Writes it to a file
csv_file = open('data_covid.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# Rename first column from 'iso_code' to 'iso3' (is necessary)
df = pd.read_csv('data_covid.csv')
df = df.rename(columns={"iso_code": "iso3"})

# Adds two features
df["percentage_of_people_vaccinated"] = df["people_vaccinated"] / df["population"] * 100
df["percentage_of_people_fully_vaccinated"] = df["people_fully_vaccinated"] / df["population"] * 100

# Removes the rows of all continents incl. the world and irrelevant features
df = df.drop(df[df.continent.isnull()].index) 
df = df.drop(columns=["new_cases_per_million", "new_cases", "new_deaths", 
                      "new_deaths_per_million", "icu_patients", "icu_patients_per_million", 
                      "icu_patients_per_million", "hosp_patients", "hosp_patients_per_million",
                      "weekly_icu_admissions", "weekly_icu_admissions_per_million", "weekly_hosp_admissions",
                      "weekly_hosp_admissions_per_million", "new_tests", "total_tests", "total_tests_per_thousand",
                      "new_tests_per_thousand", "new_tests_smoothed", "positive_rate", "tests_per_case", "tests_units",
                      "total_vaccinations", "people_vaccinated", "people_fully_vaccinated", "total_boosters", 
                      "new_vaccinations", "new_vaccinations_smoothed", "total_vaccinations_per_hundred", 
                      "people_vaccinated_per_hundred", "people_fully_vaccinated_per_hundred", "new_people_vaccinated_smoothed",
                      "population_density", "aged_65_older", "aged_70_older", "handwashing_facilities", 
                      "excess_mortality_cumulative_absolute", "excess_mortality_cumulative", "excess_mortality", "excess_mortality_cumulative_per_million"]) 

df.to_csv('data_covid.csv', index=False)

toast.show_toast("Covid Data Update Completed", "The update has been completed", duration=30)
# %%