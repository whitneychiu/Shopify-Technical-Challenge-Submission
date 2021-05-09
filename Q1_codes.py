import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

def load_df():
    df = pd.read_csv("data/2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
    return df

def get_total_revenue(df):
    total_rev = df["order_amount"].sum(axis= 0)
    return total_rev

def get_aov(df):
    aov = get_total_revenue(df)/ df.shape[0]
    print(aov)

def explore_order_amount_distribution(df):
    boxplot = df.boxplot(column='order_amount')
    plt.show()

def stratify_df(df):
    Q1 = df.order_amount.quantile(q=0.25)
    Q2 = df.order_amount.quantile(q=0.5)
    Q3 = df.order_amount.quantile(q=0.75)
    IQR = Q3 - Q1
    df_small_orders = df[(df.order_amount < Q2 + IQR * 1.5) & (df.order_amount > Q2 - IQR * 1.5)]
    df_large_orders = df.loc[(df["order_amount"] > Q2 + IQR * 1.5) | (df["order_amount"] < Q2 - IQR * 1.5)]
    return df_small_orders, df_large_orders

def describe(df):
    print(df.order_amount.describe())

def main():
    df = load_df()
    get_total_revenue(df)
    get_aov(df)
    explore_order_amount_distribution(df)

    df_small_orders, df_large_orders = stratify_df(df)
    describe(df_small_orders)
    explore_order_amount_distribution(df_small_orders)
    describe(df_large_orders)
    explore_order_amount_distribution(df_large_orders)

    get_aov(df_small_orders)
    get_aov(df_large_orders)

if __name__ == "__main__":
    main()