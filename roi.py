
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

from core.util import eliminate_commas

workbook = xlsxwriter.Workbook('./result/roi_calculate.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/dataset.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'year', 'genres', 'runtime', 'productionCountries',  'budget', 'revenue', 'popularity', 'voteAverage']

line_count = 0

for index, row in df.iterrows():

    if row.year != 1990:
        continue

    roi = (int(eliminate_commas(row.revenue)) - int(eliminate_commas(row.budget))) / int(eliminate_commas(row.budget))

    worksheet.write(line_count,0, row.title)

    worksheet.write(line_count,1, row.revenue)

    worksheet.write(line_count,2, row.budget)

    worksheet.write(line_count,3, roi)

    line_count+=1


workbook.close()

