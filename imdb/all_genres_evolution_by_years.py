
# Read de dataset in format csv, and split Production Countries by , and return new dataset in format xlsx
import csv
import xlsxwriter
import pandas as pd

workbook = xlsxwriter.Workbook('./result/allGenresEvolution.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_csv('./dataset/separateGenres.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'year', 'genres', 'runtime', 'productionCountries',  'budget', 'revenue', 'popularity', 'voteAverage']

line_count = 0

# Select all genres in the dataset
genres = df['genres'].unique()
print(genres)

for genre in genres:
  
    # Count the number of genres by year
    df_genre = df[df['genres'].str.contains(genre)]
    df_genre = df_genre.groupby(['year']).count()
    df_genre = df_genre.reset_index()

    year1995 = 0
    year1996 = 0 
    year1997 = 0 
    year1998 = 0 
    year1999 = 0 
    year2000 = 0
    year2001 = 0 
    year2002 = 0 
    year2003 = 0 
    year2004 = 0 
    year2005 = 0

    try:
        year1995 = df_genre[df_genre['year'] == 1995]['title'].values[0]
    except:
        pass

    try:
        year1996 = df_genre[df_genre['year'] == 1996]['title'].values[0]
    except:
        pass

    try:
        year1997 = df_genre[df_genre['year'] == 1997]['title'].values[0]
    except:
        pass

    try:
        year1998 = df_genre[df_genre['year'] == 1998]['title'].values[0]
    except:
        pass

    try:
        year1999 = df_genre[df_genre['year'] == 1999]['title'].values[0]
    except:
        pass

    try:
        year2000 = df_genre[df_genre['year'] == 2000]['title'].values[0]
    except:
        pass

    try:
        year2001 = df_genre[df_genre['year'] == 2001]['title'].values[0]
    except:
        pass

    try:
        year2002 = df_genre[df_genre['year'] == 2002]['title'].values[0]
    except:
        pass

    try:
        year2003 = df_genre[df_genre['year'] == 2003]['title'].values[0]
    except:
        pass

    try:
        year2004 = df_genre[df_genre['year'] == 2004]['title'].values[0]
    except:
        pass

    try:
        year2005 = df_genre[df_genre['year'] == 2005]['title'].values[0]
    except:
        pass

    worksheet.write(line_count,0, genre),
    worksheet.write(line_count,1, year1995),
    worksheet.write(line_count,2, year1995 + year1996),
    worksheet.write(line_count,3, year1995 + year1996 + year1997),
    worksheet.write(line_count,4, year1995 + year1996 + year1997 + year1998),
    worksheet.write(line_count,5, year1995 + year1996 + year1997 + year1998 + year1999),
    worksheet.write(line_count,6, year1995 + year1996 + year1997 + year1998 + year1999 + year2000),
    worksheet.write(line_count,7, year1995 + year1996 + year1997 + year1998 + year1999 + year2000 + year2001),
    worksheet.write(line_count,8, year1995 + year1996 + year1997 + year1998 + year1999 + year2000 + year2001 + year2002),
    worksheet.write(line_count,9, year1995 + year1996 + year1997 + year1998 + year1999 + year2000 + year2001 + year2002 + year2003),
    worksheet.write(line_count,10, year1995 + year1996 + year1997 + year1998 + year1999 + year2000 + year2001 + year2002 + year2003 + year2004),
    worksheet.write(line_count,11, year1995 + year1996 + year1997 + year1998 + year1999 + year2000 + year2001 + year2002 + year2003 + year2004 + year2005),
    line_count+=1

workbook.close()