import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/genres_evolution_per_year.csv' , encoding='latin-1')

df.columns = ['title', 'year', 'runtime', 'genre']

## Apartado B
# Show the evolution of the genres only 2005-2020 
df.where(
    df['year'].between(2005, 2020),
).groupby(['genre', 'year']).year.value_counts().unstack().plot(kind='bar' , stacked=True, title='Genres evolution year')
plt.show()

# Show bar chart with percentage of movies per genre
# df.groupby(['genre']).year.value_counts().plot(kind='bar' , title='Genres evolution year')
# plt.show()

# print(df)