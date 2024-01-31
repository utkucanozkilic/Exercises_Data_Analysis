import pandas as pd
import numpy as np


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
print(chipo.groupby("item_name")["quantity"].sum()["Chicken Bowl"])
bracket()

# What was the most ordered item in the choice_description column?
# df'ten ilgili sütunu filtreleyerek al
description_df = chipo["choice_description"].dropna()
bracket()

# her satırdaki değerin içindeki []'leri at.
description_df = description_df.str.replace("[", "").str.replace("]", "")
description_df_list = []

# description_df içinde gez ve eğer i içinde virgül yoksa doğrudan description_df_list'e ekle.
# eğer virgül varsa 'virgül+space' olacak şekilde parçala, bunu geçici _ listesine at ve bu listeden de
# description_df_list'e at.
for i in description_df:
    if "," not in i:
        description_df_list.append(i)
    else:
        _ = i.split(", ")
        for z in _:
            description_df_list.append(z)

# description_df_list'i Pandas Serisine dönüştür, value_counts() ile grupla, değerleri azalan olarak sırala
# ve ilk değeri al
most_ordered_item = pd.DataFrame(description_df_list).value_counts().sort_values(ascending = False).index[0]
# daha uygun formatlı çıktı için listeye çevir ve bastır.
print(list(most_ordered_item))
bracket()

# Step 13. Turn the item price into a float
# Step 13.a. Check the item price type
# Step 13.b. Create a lambda function and change the type of item price
# Step 13.c. Check the item price type

print(chipo["item_price"].head())
chipo["item_price"] = chipo["item_price"].apply(lambda x: x.replace("$", "")).astype("float64")
print(chipo["item_price"].head(), chipo["item_price"].dtype)
bracket()
# How much was the revenue for the period in the dataset?
chipo["total_price"] = chipo["quantity"] * chipo["item_price"]
print("The total revenue for the period is", chipo["total_price"].sum())
bracket()
# How many orders were made in the period?
print(len(chipo.groupby("order_id")), "orders were made in the period.")
bracket()
#  What is the average revenue amount per order?
print(chipo["total_price"])
print(chipo.groupby("order_id")["total_price"].mean())
bracket()
# How many different items are sold?
print(chipo["item_name"].value_counts().sum())