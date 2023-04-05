import pandas as pd
import numpy as np
from env import get_connection
import os

#Removes warnings and imporves asthenics
import warnings
warnings.filterwarnings("ignore")

def wrangle_logs():
    """
    This function gets all data from the connection_logs database.
    """
    filename = "curriculum_logs.csv"
    
    #Checks if file is catched
    if os.path.isfile(filename):
        
        df = pd.read_csv(filename, infer_datetime_format=True)

        #Changes to datetime type
        df['datetime'] = pd.to_datetime(df['datetime'], infer_datetime_format=True)
        df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

        #Sets index
        df = df.set_index('date')

        return df
    
    else:
        
        # read the SQL query into a dataframe
        query = """
        SELECT * FROM logs
        LEFT JOIN cohorts on logs.cohort_id = cohorts.id;
        """
        #Gets connection to Codeup database
        df = pd.read_sql(query, get_connection('curriculum_logs'))
        
        #Prepares data for exploration
        df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], utc=True)

        #Removes time offset
        df['datetime'] = df['datetime'].dt.tz_localize(None)

        #Changes date to datetime object
        df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

        #Caching
        df.to_csv(filename, index=False)
        #Sets index
        df = df.set_index('date')

        #Return the dataframe
        return df
    
def wrangle_grocery():
    """
    This function gets all data from the connection_logs database.
    """
    filename = "grocery.csv"
    
    #Checks if file is catched
    if os.path.isfile(filename):
        
        df = pd.read_csv(filename, index_col='customer_id')
        
        return df
    else:
        
        # read the SQL query into a dataframe
        query = """
        SELECT *
        FROM grocery_customers;
        """
        
        #Gets connection to Codeup database
        df = pd.read_sql(query, get_connection('grocery_db'))
        
        #Caching
        df.to_csv(filename, index=False)
        
        df = df.set_index('customer_id')

        #Return the dataframe
        return df
    
def pour_wine():
    """ 
    This function takes the red and white wine quality csvs, adds a type column and combines into the wine DataFrame.
    """
    
    filename = "winequality.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        red_df = pd.read_csv("winequality-red.csv")
        white_df = pd.read_csv("winequality-white.csv")

        red_df['type'] = 'red'
        white_df['type'] = 'white'

        wine_df = pd.concat([red_df, white_df], ignore_index=True)

        wine_df.to_csv(filename, index=False)
    
    return wine_df