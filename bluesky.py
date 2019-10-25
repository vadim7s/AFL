import pandas as pd
import os as os


def find_filenames( path_to_dir, suffix=".txt" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

def date_conversion(s):
    """
    This is an extremely fast approach to datetime parsing.
    For large data, the same dates are often repeated. Rather than
    re-parse these, we store all unique dates, parse them, and
    use a lookup to convert all dates.
    """
    dates = {date:pd.to_datetime(date) for date in s.unique()}
    return s.map(dates)

def scan_columns(df):
    '''
    this function loops through a DF's columns
    Need to get:
    1. Number of unique values
    2. Type
    3. $
    '''
    result=pd.DataFrame(columns=['Column_Type','Distinct_Values'])
    for column in df.columns:
        #first try to convert to dates
        try:
            df[column] = date_conversion(df[column])
        except:
            pass
        values=df[column].to_list()
        distinct_values = list(set(values))
        types = set([type(x) for x in distinct_values])
        print(types)
        #result.append([types,len(distinct_values)])
    return result

class Bluesky:

    max_rows = 1000 # limit max rows read
    
    def __init__(self,folder,extension,separator):
        self.folder = folder # the folder where source files are
        self.tables = find_filenames(self.folder,extension) # gets the list of files with expected extension
        self.separator = separator
        self.line_count_list = [] #this gets a list of how many lines each file has
        for table in self.tables:
            self.line_count_list.append(sum(1 for line in open(self.folder+'/'+table,encoding="utf8")))        
        self.dfs = []  # list of Dataframes representing first X rows of each table where X is defined by the class parameter max_rows
        for table in self.tables:
            self.dfs.append(pd.read_csv(self.folder+'/'+table,sep=self.separator ,parse_dates=True,nrows=self.max_rows))
            
# create an instance
my_class = Bluesky('./bluesky/Adventureworks','.txt','\t')
#my_class = Bluesky('./Adventureworks','.txt','\t')
print(my_class.tables[0])
print(scan_columns(my_class.dfs[0]))

