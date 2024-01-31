import pandas as pd

pd.set_option('display.max_columns', 1881)
pd.set_option('display.width', 1881)

euro12 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/"
                     "02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")

# Select only the Goals column.
print(euro12.loc[:, "Goals"])

# How many team participated in the Euro2012?
print(euro12["Team"].value_counts().sum())

# What is the number of columns in the dataset?
print(len(euro12.columns))

# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
selected_index = ["Team", "Yellow Cards", "Red Cards"]
discipline = euro12[selected_index]

# Sort the teams by Red Cards, then to Yellow Cards
print(euro12["Red Cards"].sort_values(ascending = False))
print(euro12["Yellow Cards"].sort_values(ascending = False))

# Calculate the mean Yellow Cards given per Team
print(euro12.groupby("Team")["Yellow Cards"].mean())

# Filter teams that scored more than 6 goals
print(euro12[euro12["Goals"] > 6]["Team"])

# Select the teams that start with G
print(euro12[euro12["Team"].str[0] == "G"]["Team"])

# Select the first 7 columns
print(euro12.iloc[:, :8])

#  Select all columns except the last 3.
print(euro12.iloc[:, :-3])

# Present only the Shooting Accuracy from England, Italy and Russia
print(euro12[euro12["Team"].isin(["England", "Italy", "Russia"])][["Team", "Shooting Accuracy"]])