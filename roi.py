
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

workbook = xlsxwriter.Workbook('roi_calculate.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/dataset.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'year', 'genres', 'runtime', 'productionCountries',  'budget', 'revenue', 'popularity', 'voteAverage']

line_count = 0

for index, row in df.iterrows():

    if row.year != 1990:
        continue

    roi = (row.revenue - row.budget) / row.budget

    worksheet.write(line_count,0, row.title)

    worksheet.write(line_count,1, row.revenue)

    worksheet.write(line_count,2, row.budget)

    worksheet.write(line_count,5, row.roi)

    line_count+=1


workbook.close()