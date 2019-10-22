#BlueSky

1 Create class
2 Scan tables
    - number
    - size - rows, columns
    - consider avoiding scanning into tables and memory
3 Scan columns
    - dates, how many, one always greater than other?, any open dates 99991231
    - numeric/text
    - can numeric be categorical due to repeated values
    - what could be keys
4 Define Entity table and its key & try to loop through columns to identify linked table
    - take a sample of a pre-defined size from each column
    - perform set intersection between columns in different tables
    - determin if one table set is a full subset of another or not
5 Think about a way to store these as attributes for some ML type application
