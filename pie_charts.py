#
# Author: Alex R. Carney
# Date: 4/9/2020
# Summary: Creates a series of pie charts via subplots of interesting
# categorical data across all reporting Chicago public schools.
#
# Dataset: 
# https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t
#

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

figs, axs = plt.subplots(2,2)

#Func Name: csv_to_df
#Purpose: Converts .csv dataset to a pandas dataframe
#Params: f_name: the file name of the dataset 
#Returns: df: pandas dataframe conversion of the .csv dataset
def csv_to_df(f_name):
    df = pd.read_csv(f_name,index_col =0)
    return df

#Func Name: clean_df
#Purpose: Removes rows where desired column value is NaN
#Params: df: pandas dataframe conversion of the .csv dataset, query: desired column
#Returns: df: pandas dataframe cleaned
def clean_df(df, query):
    df =df.replace('NDA', np.nan)
    df =df.replace('Not Enough Data', np.nan)
    df.dropna(subset = [query], inplace = True)    
    return df

#Func Name: plot_pie_chart
#Purpose: Removes rows where desired column value is NaN
#Params: df: pandas dataframe conversion of the .csv dataset, query: desired column
    #sub_pos_1, sub_pos_1 axs position for this pie chart, color_scheme: pie chart colors
#Returns:
def plot_pie_chart(df,query,title,sub_pos_1, sub_pos_2,color_scheme):
    df= clean_df(df, query)
    data_series= df[query].value_counts()
    axs[sub_pos_1,sub_pos_2].pie(data_series.values, labels=data_series.index, autopct='%1.f%%',
    colors=color_scheme,startangle=270)    
    axs[sub_pos_1, sub_pos_2].axis('equal')
    axs[sub_pos_1, sub_pos_2].set_title(title,  fontsize = 12)

def main():
    f_name = 'Chicago_Public_Schools_-_Progress_Report_Cards__2011-2012_.csv'
    df = csv_to_df(f_name)
    color_schemes = [['aqua', 'crimson','wheat'],['mistyrose', 'gold','teal'],['grey', 'lightcoral','lightgrey'],
                     ['darkcyan', 'coral','lime']]
    plot_pie_chart(df, 'Parent Engagement Icon ', 'Parent Engagement',0,0,color_schemes[0])
    plot_pie_chart(df, 'Parent Environment Icon', 'Parent Environment',0,1, color_schemes[1])
    plot_pie_chart(df, 'Adequate Yearly Progress Made? ', 'Made Adequate Yearly Progress',1,0, color_schemes[2])
    plot_pie_chart(df, 'CPS Performance Policy Level', 'CPS Performance Policy Level',1,1, color_schemes[3])
    plt.tight_layout()
    plt.show()
    
main()