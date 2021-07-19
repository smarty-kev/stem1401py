"""
Data File.

1. csv
A CSV is a comma-separated values file, which allows data to be saved in a tabular format.
CSVs look like a garden-variety spreadsheet but with a .csv extension
CSV files can be used with most any spreadsheet program, such as Microsoft Excel or Google Spreadsheets

Text editor
spreadsheet program
database application export as .CSV

keywords:
csv file sample download

dataset source:
governement source

dataset size
big data file
1. split
2. streaming

data clean/ data washing
data pre-processing
dirty data
data processing and analysis

"""

title = "Year,Industry_aggregation_NZSIOC,Industry_code_NZSIOC,Industry_name_NZSIOC,Units,"\
    "de,Variable_name,Variable_category,Value,Industry_code_ANZSIC06"

titlelist = title.split(",")
print(len(titlelist))

data1 = "2019,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,\"728.239\",\"ANZSIC06 divisions A-S (excluding classes K6330 L6711 O7552 O760 O771 O772 S9540 S9601 S9602 and S9603)\""

datalist1 = data1.split(",")
print(len(datalist1))

for data in datalist1:
    print(data)
print()

data2 = "2019,Level 1,99999,All industries,Dollars (millions),H04,\"Sales, government funding, grants and subsidies\",Financial performance,\"643.809\",\"ANZSIC06 divisions A-S (excluding classes K6330 L6711 O7552 O760 O771 O772 S9540 S9601 S9602 and S9603)\""
datalist2 = data2.split(",")
print(len(datalist2))
print(datalist2)