import pandas as pd
import os as os


def find_filenames( path_to_dir, suffix=".txt" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

class Bluesky:
    
    def __init__(self,folder):
        self.folder = folder
    
    def get_tables(self):
        #result = [] # list of dataframes to return
        result=find_filenames(self.folder) 
        return result

my_class = Bluesky('C:\\Users\\A30001596\\AFL\\Adventureworks')

print(my_class.get_tables())