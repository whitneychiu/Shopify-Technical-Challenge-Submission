import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

def load_df():
    """ 
    args:
        csv file
        
    returns: 
        pandas.DataFrame
    """
    df = pd.read_csv("data/2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
    return df

def get_total_revenue(df):
    """
    args:
        df (pandas.DataFrame): dataframe with order_amount
        
    returns:
        integer: total revenue
    """
    total_rev = df["order_amount"].sum(axis= 0)
    return total_rev

def get_aov(df):
    """
    args:
        df (pandas.DataFrame): dataframe with order_amount
        
    returns:
        integer: average order value
    """
    aov = get_total_revenue(df)/ df.shape[0]
    print(aov)

def explore_order_amount_distribution(df):
    """
    args:
        df (pandas.DataFrame): dataframe with order_amount
        
    returns:
        pandas boxplot
    """
    boxplot = df.boxplot(column='order_amount')
    plt.show()

def describe_order_amount(df):
    """
    args:
        df (pandas.DataFrame): dataframe with order_amount
        
    returns:
        pandas.Series: descriptive statistics for order_amount
    """
    print(df.order_amount.describe())

def main():
    df = load_df()
    get_total_revenue(df)
    get_aov(df)
    explore_order_amount_distribution(df)
    describe_order_amount(df)

if __name__ == "__main__":
    main()
