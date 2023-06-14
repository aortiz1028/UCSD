"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.rates import my_func, my_other_func
##
##

def test_my_func():

    assert my_func() == None

def test_my_other_func():

    assert my_other_func() == None
    


from my_module.rates import highest_rate_per_year, highest_rate_per_age, highest_year

def highest_rate_per_year(column_1, column_2):

    assert highest_rate_per_year(column_1, column_2) is not None

def highest_rate_per_age(column_1, column_2, column_3):

    assert highest_rate_per_age(column_1, column_2, column_3) is not None                
    
def highest_year(column_1):
    assert highest_year(column_1) is not None