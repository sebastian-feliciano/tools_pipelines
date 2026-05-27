# Hypothetical dataframe called orders_df

import pandas as pd

orders_df = pd.read_csv("orders.csv")

# List of possible pandas summarization operations
sum = orders_df["sales"].sum()
count = orders_df["order_id"]
distinctcount = orders_df["user_id"].nunique()
