"""A collection of function for doing my project."""

import numpy as np
import pandas as pd
df = pd.read_csv(r'/home/amortiz/Final_Project_COGS18_SP23/as-dec19-abortion-rates-by-age-of-woman.csv')
df


#any two columns, column_2 should be Abortion_rate
def highest_rate_per_year(column_1, column_2): 
    
    """ Uses the values in two columns chosen, the year and rate, and returns
    the highest abortion rate for each year regardless of the age column.
    
    Parameters
    ----------
    column_1 : string or label
        column labeled 'Period' containing years to be grouped by.
    column_2 : string or label
        column labeled 'Abortion_rate' from which the highest value is 
        chosen.
    
    Returns
    -------
    output : dtype : pandas.core.series.Series
        Series containing two cloumns, 'Period' and 'Abortion_rate', with the highest
        abortion rate per year.
    """
    
    #grouping by the year only, not age
    output = df.groupby(column_1)[column_2].max() 
    
    return output

highest_rate_per_year('Period','Abortion_rate')


#second DataFrame to save the data from function and use it for graph
df2 = pd.DataFrame(highest_rate_per_year('Period','Abortion_rate'))

"""code was used from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html
and then edited adn rewritten for this project"""

#reset index to show 'Period' in index as a column name
df2 = df2.reset_index()
df2['Period']
df2['Abortion_rate']

#testing to show that both columns and their labels appear
df2.columns
df2.plot.bar(x = 'Period', y = 'Abortion_rate')



def highest_rate_per_age(column_1, column_2, column_3):
    
    """"Looks at the highest rate and its corresponding age range
    per year.
    
    Parameters
    ----------
    column_1 : string or label
        column labeled 'Period' for first grouping
    column_2 : string or label
        column labeled 'Age_of_woman' for second grouping based on age
    column_3 : string or label
        column labeled 'Abortion_rate', the values we are most focused on
        and the highest values will be chosen from.
    
    Returns
    -------
    output : pandas.core.frame.DataFrame
        DataFrame displaying the highest rates and what ages they are associated
        with for each year.
    """
    
    highest_rate = df.loc[df.groupby(column_1)[column_3].idxmax()]
    output = highest_rate[[column_1, column_2, column_3]]
    
    return output

highest_rate_per_age('Period', 'Age_of_woman','Abortion_rate')



def highest_year(column_1):
    
    """""Looks at the highest rate overall, regardless of age
    or year.
    
    Parameters
    ----------
    column_1 : string or label
        column labeled 'Abortion_rate' since that is the column
        with the max value we are trying to find.
        
    Returns
    ------
    output : pandas.core.frame.DataFrame
        DataFrame displaying the highest overall value along
        with its age range and year
    """
    
    #idxmax() produces error
    output = df[df['Abortion_rate']== df['Abortion_rate'].max()]
    
    return output

highest_year('Abortion_rate')