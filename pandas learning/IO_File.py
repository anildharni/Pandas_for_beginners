__author__ = 'swapna'
import pandas as pd

# How to read csv
df_c = pd.read_csv("C:\Users\swapna\Desktop\Python Task1\Regional.csv")

# Convert csv to excel file
df_c.to_excel('C:\Users\swapna\Desktop\Python Task1\Reg_excel.xlsx', sheet_name='New')

# read the excel file
df_x = pd.read_excel("C:\Users\swapna\Desktop\Python Task1\Reg_excel.xlsx")

# How to sort the Unique ID
df_sorted = df_x.sort_values(['Sno'], ascending=True)

# How to sort the Unique ID and Sno
df_sorted = df_c.sort_values(['Sno','User_ID'], ascending = [False,False])

# To print  sorted file
df_sorted.to_excel('C:\Users\swapna\Desktop\Python Task1\Reg_sorted.xlsx', sheet_name='New', merge_cells=False)

# To print the Total number of rows (n size) in the file
print "Range of Index", (df_c.index)
print "Columns / Variables in data file", df_c.columns
print "Values/data in data file", df_c.values

# Identify which observations are duplicates
print df_c.duplicated()

# How to Check Remove Duplicates in User_ID
df_d = df_c.drop_duplicates(['User_ID'], keep='last')
# keep : {‘first’, ‘last’, False},

# To see the after remove duplicate values file
df_d.to_excel('C:\Users\swapna\Desktop\Python Task1\Reg_Dul.xlsx', sheet_name='New')

# Now we find the missing values in any column
def num_missing(x):
  return sum(x.isnull())
print "Missing values per column:"
print df_c.apply(num_missing, axis=0) #axis=0 defines that function is to be applied on each column

print "Missing values per row:"
print df_c.apply(num_missing, axis=1) #axis=1 defines that function is to be applied on each row

# To fill missing values with mean
df_s = df_c.fillna(df_c.mean())

# To get/print csv without missing values
# Convert csv to excel file
df_s.to_excel('C:\Users\swapna\Desktop\Python Task1\Reg_Replace Missing values With_Mean.xlsx', sheet_name='New')

# To print Crosstab
print pd.crosstab(df_c["S4_AGE"],df_c["Country_code"])

# To print Crosstab with Total column  - Using the margins option in crosstab to compute row and column totals
print pd.crosstab(df_c["S4_AGE"],df_c["Country_code"], margins=True)

# with pd.crosstab(df_c["S4_AGE"],df_c["Country_code"]).apply(lambda r: r/r.sum(), axis=1)
# and pd.crosstab(df.A, df.B).apply(lambda r: r/r.sum(), axis=0)
