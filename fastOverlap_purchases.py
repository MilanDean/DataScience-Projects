# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:32:30 2019

@author: Milan Dean
"""

import numpy as np
import pandas as pd
import time

try:
    data_one = input('Please enter the name of the CSV file containing first time buyers.')
    data_two = input('Please enter the name of the CSV file you wish to compare against first time buyers.')
    
    df1 = pd.read_csv(data_one)
    df2 = pd.read_csv(data_two)

except:
    df1 = pd.read_csv(data_one+'.csv')
    df2 = pd.read_csv(data_two+'.csv')

def fast_overlap():
    
    """This algorithm determines the number of customer Id's from the first dataframe that
    matches the customer Id's from the second dataframe."""
    
    column = input('\nPlease input the name of the column containing customer IDs')
    
    print('\nCalculating total customers who have bought both products...')
    time.sleep(1)
    
    set_df1 = set(np.array(df1[column]))
    set_df2 = set(np.array(df2[column]))
    
    result = [value for value in set_df1 if value in set_df2]
    
    percent = round((len(result)/len(df1[column]))*100, 2)    
    
    print('\nTotal overlapping purchases:', len(result))
    print('\nPercent of people who bought second product after initially buying first product: {}{}.'.format(percent, '%'))

    
fast_overlap()