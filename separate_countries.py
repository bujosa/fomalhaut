
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

workbook = xlsxwriter.Workbook('./result/separateCountries.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/dataset.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'year', 'genres', 'runtime', 'productionCountries',  'budget', 'revenue', 'popularity', 'voteAverage']

line_count = 0

for index, row in df.iterrows():
    countries = row['productionCountries'].split(',')
    for key in countries:  
        worksheet.write(line_count,0, row.title),
        worksheet.write(line_count,1, row.year),
        worksheet.write(line_count,2, row.genres),
        worksheet.write(line_count,3, row.runtime),
        worksheet.write(line_count,4, key),
        worksheet.write(line_count,5, row.budget),
        worksheet.write(line_count,6, row.revenue),
        worksheet.write(line_count,7, row.popularity),
        worksheet.write(line_count,8, row.voteAverage),
        line_count+=1

workbook.close()