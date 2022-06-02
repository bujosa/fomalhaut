import pandas as pd
import xlsxwriter

workbook = xlsxwriter.Workbook('./result/genres_evolution_per_year.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/genres_evolution.csv' , encoding='latin-1')

line_count = 0

df.columns = ['title', 'year', 'runtime', 'genres']

# Compare movies revenue with The Lord of the Rings: The Two Towers and return the difference
for index, row in df.iterrows():
    if row.genres == '[]':
       continue

    genres = row.genres.split(' ')

    for genre in genres:
        worksheet.write(line_count,0, row.title)

        worksheet.write(line_count,1, row.year)

        worksheet.write(line_count,2, row.runtime)

        worksheet.write(line_count,3, genre)

        line_count+=1

workbook.close()


