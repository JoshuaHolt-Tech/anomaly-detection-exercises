import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


def outlier_detector(dataframe, col, k=1.5, return_high = True, return_low = True, print_bounds = False):
    """
    This function takes in a dataframe and looks for upper and lower outliers.
    """
    q1, q3  = dataframe[col].quantile(q=[0.25, 0.75])
    iqr = q3 - q1
    
    
    lower_bound = q1 - (k * iqr)
    upper_bound = q3 + (k * iqr)
    
    if print_bounds == True:
        print(f'Upper bound: {upper_bound:.4f}')
        print(f'Lower bound: {lower_bound:.4f}')

    
    high_items = dataframe[col] > upper_bound
    low_items = dataframe[col] < lower_bound

    if return_high and return_low:
        return dataframe[low_items | high_items]
    elif return_high:
        return dataframe[high_items]
    elif return_low:
        return datagrame[low_items]
    else:
        print(f'No items returned despite {len(high_items) + len(low_items)} outliers present.')


def z_outlier_detector(df, col, z=2, return_high = True, return_low = True):
    """
    This function takes in a dataframe and looks for upper and lower outliers.
    """
    #Mask
    z_score = stats.zscore(df[col])
    
    #Apply mask
    high_items = df[z_score > z]
    low_items = df[z_score < (-1 * z)]

    if return_high and return_low:
        return low_items, high_items
    elif return_high:
        return high_items
    elif return_low:
        return low_items
    else:
        print(f'No items returned despite {len(high_items) + len(low_items)} outliers present.')
        


def outlier_ejector(dataframe, column, k=1.5, eject_low = True, eject_high = True, print_bounds = False):
    """
    This function takes in a dataframe and removes outliers for upper and/or lower items.
    """
    q1, q3  = dataframe[column].quantile(q=[0.25, 0.75])
    iqr = q3 - q1
    
    
    lower_bound = q1 - (k * iqr)
    upper_bound = q3 + (k * iqr)
    
    if print_bounds == True:
        print(f'Upper bound: {upper_bound:.4f}')
        print(f'Lower bound: {lower_bound:.4f}')
        
    high_items = dataframe[column] > upper_bound
    low_items = dataframe[column] < lower_bound

    if eject_high and eject_low:
        return dataframe[~low_items | ~high_items]
    elif eject_high:
        return dataframe[~high_items]
    elif eject_low:
        return datagrame[~low_items]
    else:
        print(f'No items rejected despite {len(high_items) + len(low_items)} outliers present.')