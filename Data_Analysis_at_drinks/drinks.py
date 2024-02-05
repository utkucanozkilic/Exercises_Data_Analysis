import pandas as pd


pd.set_option("display.max_columns", 1881)
pd.set_option("display.width", 1881)


drinks = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv")

# Which continent drinks more beer on average?
drinks.groupby("continent")["beer_servings"].mean().idxmax()
# country,beer_servings,spirit_servings,wine_servings,total_litres_of_pure_alcohol,continent
# For each continent print the statistics for wine consumption.
drinks.groupby("continent")["wine_servings"].describe().T

# Print the mean alcohol consumption per continent for every column
drinks.groupby("continent")[["beer_servings", "spirit_servings", "wine_servings"]].agg("mean")

# Print the median alcohol consumption per continent for every column
drinks.groupby("continent")[["beer_servings", "spirit_servings", "wine_servings"]].agg("median")

# Print the mean, min and max values for spirit consumption.
drinks["total_litres_of_pure_alcohol"].describe().T