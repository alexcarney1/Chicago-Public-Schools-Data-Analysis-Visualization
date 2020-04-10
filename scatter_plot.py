#
# Author: Alex R. Carney
# Date: 4/9/2020
# Summary: Creates a scatterplot comparing the College Enrollment Rate
# to the School Instruction Score of Chicago Public Schools in the 
# 2011-2012 school year. This scatterplot shows a moderately strong, 
# positive, linear association between higher Instruction Scores and College
# Enrollment Rates. 
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

#Func Name: clean_and_type_data
#Purpose: Replaces NDA values with np.nan. Ignores rows 
# in desired columns with NaN values. Converts col values to float.
#Params: df: dataframe, col1 is first desired col, col2 is second desired col
#Returns: df: original data frame but with desired columns properly typed 
# and rows with NaN values removed.
def clean_and_type_data(df, col1, col2):
    df =df.replace('NDA', np.nan)
    df.dropna(subset = [col1], inplace = True)
    df.dropna(subset = [col2], inplace = True)
    df[col1] = df[col1].astype(float)
    df[col2] = df[col2].astype(float) 
    return df

#Func Name: plot_data
#Purpose: Plots the data to a scatterplot.
#Params: df: dataframe, col1 is first desired col, col2 is second desired col
#Returns: 
def plot_data(df, col1, col2):
    df.plot(kind='scatter',x=col1,y=col2, color='red')
    plt.xlabel("Instruction Score", fontsize = 14)
    plt.ylabel("College Enrollment Rate (%)", fontsize = 14)
    plt.title("College Enrollment Rate Vs. School Instruction Score", fontsize = 14)
    
#Func Name: plot_regression
#Purpose: Plots a  linear regression line to the scatterplot.
#Params: df: dataframe, col1 is first desired col, col2 is second desired col
#Returns:    
def plot_regression(df,col1,col2):
    x = np.array(df[col1])   
    y = np.array(df[col2])   
    m,b = np.polyfit(x,y,1)

    plt.plot(x, m*x + b)
    
def main():
    f_name = 'Chicago_Public_Schools_-_Progress_Report_Cards__2011-2012_.csv'
    col1 = 'Instruction Score'
    col2 = 'College Enrollment Rate %'        
    df = csv_to_df(f_name)
    df = clean_and_type_data(df,col1,col2)
    plot_data(df, col1, col2)
    plot_regression(df, col1,col2)
    plt.show()
    
main()