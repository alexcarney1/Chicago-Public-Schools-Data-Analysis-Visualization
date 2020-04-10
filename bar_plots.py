#
# Author: Alex R. Carney
# Date: 4/9/2020
# Summary: Creates a bar plot showing the average environment and safety scores
# of all reporting Chicago school networks.
#
# Dataset: 
# https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t
#

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

#Func Name: csv_to_df
#Purpose: Converts .csv dataset to a pandas dataframe
#Params: f_name: the file name of the dataset 
#Returns: df: pandas dataframe conversion of the .csv dataset
def csv_to_df(f_name):
    df = pd.read_csv(f_name,index_col =0)
    return df

#Func Name: clean_df
#Purpose: Removes rows where desired column value is NaN
#Params: df: pandas dataframe conversion of the .csv dataset
#Returns: df: pandas dataframe cleaned
def clean(df):
    df.replace("",np.nan)
    df.replace(" ",np.nan)
    df.replace("NDA",np.nan)
    df.dropna(subset = ['Environment Score'], inplace = True)
    df.dropna(subset = ['Safety Score'], inplace = True)
    return df

#Func Name: plot
#Purpose: creates bar plot of average Environment and Safety Scores by
#    school network.
#Params: df: cleaned pandas dataframe conversion of the .csv dataset
#Returns: df: pandas dataframe cleaned
def plot(df):
    #get appropriate data and calculate means
    school_networks = df['Network Manager']
    environment_score_series= df.groupby('Network Manager')['Environment Score'].mean()
    safety_score_series= df.groupby('Network Manager')['Safety Score'].mean()
    
    #plot setup
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 15)
    ax.set_ylim(0,100)
    n = np.arange(len(environment_score_series.values))
    width = 0.35
    plt.bar(n, environment_score_series.values,width, label = 'Environment Score', color = 'indianred')
    plt.bar(n + width, safety_score_series.values,width, label = 'Safety Score', color = 'cornflowerblue')
    plt.xticks(n + width / 2, environment_score_series.index, fontsize =10)
    
    plt.legend(loc='best')
    plt.ylabel("Score")
    plt.title("Environment and Safety Score by School Network", fontsize =10)    
    fig.autofmt_xdate() 
    plt.show()

def main():
    f_name = 'Chicago_Public_Schools_-_Progress_Report_Cards__2011-2012_.csv'
    df = csv_to_df(f_name)
    df = clean(df)
    plot(df)
main()
