
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

from core.util import eliminate_commas

workbook = xlsxwriter.Workbook('./result/top_10.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/valorationNetflix.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'valoration']

line_count = 0

# Compare movies valoration with Stranger Things
for index, row in df.iterrows():
    if row.title == 'Stranger Things':
       continue

    comparePorcentual =  row.valoration /df[df['title'] == 'Stranger Things'].valoration.values[0]

    if comparePorcentual > 1:
            comparePorcentual = comparePorcentual - 1    
    elif comparePorcentual < 1:
            comparePorcentual = comparePorcentual - 1


    worksheet.write(line_count,0, row.title)

    worksheet.write(line_count,1, row.valoration)

    worksheet.write(line_count,2, comparePorcentual)

    line_count+=1

workbook.close()

