'''
this is to try converting strings to dates 
and use error handling to determine that
the value is not a date

'''

import pandas as pd

def date_conversion(s):
    """
    This is an extremely fast approach to datetime parsing.
    For large data, the same dates are often repeated. Rather than
    re-parse these, we store all unique dates, parse them, and
    use a lookup to convert all dates.
    """
    dates = {date:pd.to_datetime(date) for date in s.unique()}
    return s.map(dates)

df = pd.DataFrame({'date-column': ['2019-12-31','12/31/2018','a string']})


try:
    df['date-column'] = lookup(df['date-column'])
except:
    print('there was an error')
else:
    print('all went ok')
types = [type(x) for x in df['date-column']]
print(df)
print(types)
print(type(df['date-column']))