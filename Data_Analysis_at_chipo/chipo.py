import pandas as pd


def bracket():
    print("--------------------------------------------------------------------------------------")


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Assign it to a variable called chipo.
chipo = pd.read_csv(
    "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv",
    sep = "\t"
    )

#  See the first 10 entries
print(chipo.head(10))
bracket()

# What is the number of observations in the dataset?
print("The number of observations in the chipo dataset is", len(chipo))
bracket()

# What is the number of columns in the dataset?
print("The number of columns in the chipo dataset is", len(chipo.columns))
bracket()

#  Print the name of all the columns.
print(chipo.columns)
bracket()

#  How is the dataset indexed?
print(chipo.index)

#  Which was the most-ordered item?
# get all quantity for all items
print(chipo.groupby("item_name")["quantity"].sum())
# get the sum of quantity of items by descending
print(chipo.groupby("item_name")["quantity"].sum().sort_values(ascending = False))
# .index returns a list. The first item of list is the most-ordered item.
print(chipo.groupby("item_name")["quantity"].sum().sort_values(ascending = False).index[0])
bracket()

# For the most-ordered item, how many items were ordered?
print(chipo.groupby("item_name")["quantity"].sum())
bracket()

# What was the most ordered item in the choice_description column?
description_df = chipo["choice_description"].dropna()

description_df = description_df.str.replace("[", "").str.replace("]", "")
print(description_df)

