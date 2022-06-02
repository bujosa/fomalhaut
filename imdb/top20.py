
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

from core.util import eliminate_commas

workbook = xlsxwriter.Workbook('./result/top_20.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/dataset.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'year', 'genres', 'runtime', 'productionCountries',  'budget', 'revenue', 'popularity', 'voteAverage']

# Create new dataset with revenue converted to int
newDataset = []
for index, row in df.iterrows():
    newDataset.append([row.title, int(eliminate_commas(row.revenue))])

# Sort dataset by revenue and return top 20
df = pd.DataFrame(newDataset, columns = ['title', 'revenue'])
df = df.sort_values(by=['revenue'], ascending=False)
movies = df.head(20).reset_index()

# Search The Lord of the Rings: The Two Towers in the top 20
print(movies[movies['title'] == 'The Lord of the Rings: The Two Towers'].revenue.values[0])
print(movies)
line_count = 0

# Compare movies revenue with The Lord of the Rings: The Two Towers and return the difference
for index, row in movies.iterrows():
    if row.title == 'The Lord of the Rings: The Two Towers':
       continue

    comparePorcentual =  row.revenue / movies[movies['title'] == 'The Lord of the Rings: The Two Towers'].revenue.values[0]

    worksheet.write(line_count,0, row.title)

    worksheet.write(line_count,1, row.revenue)

    worksheet.write(line_count,2, comparePorcentual)

    line_count+=1

workbook.close()

