# COVID-19 Dashboard 

Interactive dashboard for tracking various statistics describing the spread of the COVID-19 virus on a global scale. Is based on the [d3-geomap library](https://github.com/yaph/d3-geomap) and uses the public data set of [Our World in Data](https://covid.ourworldindata.org/data/owid-covid-data.csv).

You can view the dashboard [here](https://glarkstoat.github.io/Corona-Dashboard/).

The dashboard features four graphs:

1. World Map
2. Top-20 Countries Ranking
3. Line Plots for Top-5 Countries
4. Correlation between two selected features

<p align="center">
  <img src="https://github.com/glarkstoat/Corona-Dashboard/assets/74681570/e9304338-b887-4a84-ae2e-348a8db925fa" width="100%" />
</p>

<p align="center">
  <img src="https://github.com/glarkstoat/Corona-Dashboard/assets/74681570/a5e60cf5-816e-4e23-9b16-1ebbb38be8ba" width="70%" />
</p>


## Usage

### Dropdown Menu

The dropdown menu in the upper left corner enables the viewer to select a feature which is visualized on the world map. 
These features include statistics like the number of total cases, total cases per capita, number of total deaths and many more.
To increase the potential insight into the data, general features of the "Our World in Data" data set such as life expectancy, GDP per capita as well median age were added to the dropdown menu.
The color code is shown on the left side of the world map, which visualizes the values for the chosen feature of each country.

The dropdown menu also controls the plots on the right side of the screen. With the upper plot showing the ranking of the Top-20 countries for each feature and selected date.
The lower plot shows the evolution of the specified feature for the Top-5 countries for the specified date. 

By clicking on a specific country on the world map, the corresponding evolution of the respective country is added to the lower right plot. There is no limit on the number of countries which can be added to this plot, however adding a large number of countries decreases the interpretability and readability of the plot greatly. By clicking the "Reset" button, the plot is reset and only shows the initial Top-5 countries.

### Time Bar

Using the bar below the world map, the user can select a certain date in time, for which the data is shown for the specified feature for each country. 
By clicking and dragging the cicular marker, the date can be selected.

By clicking the "Now" button, the user can return to the current date.
By pressing the "Play" button, the programs iterates trough the dates with a speed of approximately 1 year/min and shows the user the features for every date.


