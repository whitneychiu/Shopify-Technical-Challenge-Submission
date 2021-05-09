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

def describe_order_amount(df):
    print(df.order_amount.describe())

def main():
    df = load_df()
    get_total_revenue(df)
    get_aov(df)
    explore_order_amount_distribution(df)
    describe_order_amount(df)

if __name__ == "__main__":
    main()
