
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

from core.util import eliminate_commas

workbook = xlsxwriter.Workbook('./result/treeMap.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/relation.csv' , encoding='latin-1')

df.columns = ['title', 'year', 'genres','imdb', 'tmdb']

line_count = 0

# Compare movies revenue with The Lord of the Rings: The Two Towers and return the difference
for index, row in df.iterrows():
    if row.genres == '[]':
       continue

    genre = row.genres.split(' ')[0]

    worksheet.write(line_count,0, row.title)

    worksheet.write(line_count,1, row.year)

    worksheet.write(line_count,2, row.imdb)

    worksheet.write(line_count,3, row.tmdb)

    worksheet.write(line_count,4, genre)

    line_count+=1

workbook.close()

