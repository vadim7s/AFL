import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
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

def scan_columns(dfs,tables):
    '''
    this function loops through a DF's columns and puts it all in one dataframe
    '''
    result=pd.DataFrame(columns=['Table_Name','Column_Name','Column_Type','Distinct_Values','Null_Count'])
    for df,table in zip(dfs,tables):
        for column in df.columns:
            #first try to convert to dates
            
            if not is_numeric_dtype(df[column]):
                try:
                    df[column] = date_conversion(df[column])
                except:
                    pass
            null_count=df[column].isna().sum()
            df[column]=df[column].dropna() 
            values=df[column].to_list()
            distinct_values = list(set(values))
            #types = list(set([type(x) for x in distinct_values]))
            types = str(df[column].dtype)
            new_line=pd.DataFrame({'Table_Name':[table],'Column_Name':[column],'Column_Type':[types],'Distinct_Values':[len(distinct_values)],'Null_Count':[null_count]})
            result = pd.concat([result,new_line])
            pass
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
        self.column_scan=scan_columns(self.dfs,self.tables)
            
# create an instance
my_class = Bluesky('./bluesky/Adventureworks','.txt','\t')
#my_class = Bluesky('./Adventureworks','.txt','\t')


print(my_class.column_scan)

