import pandas as pd
import os as os


def find_filenames( path_to_dir, suffix=".txt" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

class Bluesky:
    
    def __init__(self,folder,extension):
        self.folder = folder # the folder where source files are
        self.tables = find_filenames(self.folder,extension) # gets the list of files with expected extension
        
    
my_class = Bluesky('./bluesky/Adventureworks','.txt')

print(my_class.tables)

line_count_list=[]
for table in my_class.tables:
    lines=sum(1 for line in open(my_class.folder+'/'+table,encoding="utf8"))
    line_count_list.append(lines)
print(line_count_list)