import pandas as pd
import matplotlib.pyplot as plt
from core.util import eliminate_commas

df = pd.read_csv('./dataset/popularidadTMDB.csv', on_bad_lines='skip', engine ='python')

df.columns = ['title', 'popularidad', 'tmdb']

newDataset = []
for index, row in df.iterrows():
    newDataset.append([
     row.title,
     row.popularidad,
     row.tmdb
    ]) 

# Display correlation between imdb and tmdb with a scatter plot using panda
def display_correlation_popularidad_tmdb(newDataset):
    popularidad = []
    tmdb = []
    for i in range(len(newDataset)):
        popularidad.append(newDataset[i][1])
        tmdb.append(newDataset[i][2])

    # Create scatter plot
    scatter_plot = pd.DataFrame({'Popularidad': popularidad, 'Tmdb': tmdb})
    scatter_plot.plot(kind='scatter', x='Popularidad', y='Tmdb', figsize=(10, 10), alpha=0.8)

    print('Correlación Pearson: ', df['popularidad'].corr(df['tmdb'], method='pearson'))

    plt.show()



display_correlation_popularidad_tmdb(newDataset)