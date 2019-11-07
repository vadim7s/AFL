import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import os as os

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_filenames( path_to_dir, suffix=".txt" ):
    '''
    finds files in a folder with a given extension
    '''
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



class Bluesky:
    
    max_rows = 1000 # limit max rows read
    
    def __init__(self,folder,extension,separator,entity):
        self.folder = folder # the folder where source files are
        self.tables = find_filenames(self.folder,extension) # gets the list of files with expected extension
        self.separator = separator
        self.line_count_list = [] #this gets a list of how many lines each file has
        for table in self.tables:
            self.line_count_list.append(sum(1 for line in open(self.folder+'/'+table,encoding="utf8")))        
        self.dfs = []  # list of Dataframes representing first X rows of each table where X is defined by the class parameter max_rows
        for table in self.tables:
            df=pd.read_csv(self.folder+'/'+table,sep=self.separator ,parse_dates=True,nrows=self.max_rows)
            if table==entity:
                self.entity_df=df
            self.dfs.append(df)
        self.entity = entity
        self.column_table=self.scan_columns() # create table of all columns
        self.entity_columns = self.column_table[self.column_table['Entity_Flag']==1]
        self.loop_columns = self.column_table[self.column_table['Entity_Flag']==0]
        self.candidates = pd.DataFrame() # create an empty table of possible links
        self.get_linkages() # have a go at finding links

    def scan_columns(self):
        '''
        this function loops through a DF's columns and puts it all in one dataframe
        '''
        result=pd.DataFrame(columns=['Table_Name','Column_Name','Column_Type','Length','Distinct_Values','Null_Count','Entity_Flag'])
        for df,table in zip(self.dfs,self.tables):
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
                length=len(values)
                distinct_values = list(set(values))
                #types = list(set([type(x) for x in distinct_values]))
                types = str(df[column].dtype)
                if table==self.entity:
                    entity_flag=1
                else:
                    entity_flag=0
                new_line=pd.DataFrame({'Table_Name':[table],'Column_Name':[column],'Column_Type':[types],'Length':[length],'Distinct_Values':[len(distinct_values)],'Null_Count':[null_count],'Entity_Flag':[entity_flag]})
                result = pd.concat([result,new_line])
                pass
        return result
    
    def get_linkages(self):
        '''
        this method finds columns most likely being linking columns
        initially between entity table and all other tables
        '''
        
        for i, row in self.entity_columns.iterrows():
            # conditions to take a column as a possible key
            From_Table = row[0]
            From_Column =row[1]
            From_Type = row[2]
            From_Length = row[3]
            From_Distinct = row[4]
            From_Nulls = row[5]
            From_Entity_Flag = row[6]
            if From_Nulls==0:   # there should not be nulls 
                if From_Type[0:3]!='date' and From_Type[0:4]!='float':  # it cannot be a date or float
                    if From_Length==From_Distinct: # all available values should be unique
                        # now for columns which are good candidates for IDs try to match to other tables
                        entity_values = set(self.entity_df[From_Column])
                        for curr_df, tab_name in zip(self.dfs, self.tables):
                            for j, tabl in self.loop_columns.iterrows():
                                To_Table = tabl[0]
                                To_Column =tabl[1]
                                To_Type = tabl[2]
                                To_Length = tabl[3]
                                To_Distinct = tabl[4]
                                To_Nulls = tabl[5]
                                To_Entity_Flag = tabl[6]    
                                if tab_name==To_Table and To_Type[0:3]!='date' and To_Type[0:4]!='float':
                                    #
                                    # now look at the actual data and if its intersects
                                    values = set(curr_df[To_Column])
                                    current_intersection = entity_values.intersection(values)
                                    number_matching= len(current_intersection)
                                    if number_matching>0:
                                        new_row = pd.DataFrame({'From_Table':[From_Table],'From_Column':[From_Column],'To_Table':[To_Table],'Candidate_Column':[To_Column],'Matching_Values':[number_matching],'Len_From':[From_Length],'To_Distinct_Vals':[To_Distinct],'Name_Similarity':[similar(From_Column,To_Column)]})
                                        new_row['Share_Matched']=new_row['Matching_Values']/new_row['To_Distinct_Vals']
                                        self.candidates = pd.concat([self.candidates,new_row])                                

# start timer            
import time
start = time.time()
# create an instance
#my_class = Bluesky('./bluesky/Adventureworks','.txt','\t','Customer.txt')

my_class = Bluesky('./Adventureworks','.txt','\t','Customer.txt')

end = time.time()
my_class.candidates.to_csv('candidates.csv')
print('Finished with execustion time of: ',end - start)