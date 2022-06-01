import pandas as pd
import matplotlib.pyplot as plt
from core.util import eliminate_commas

df = pd.read_csv('./result/correlation.csv', on_bad_lines='skip', engine ='python')

newDataset = []
for index, row in df.iterrows():
    if row.title in ["Jurassic Park III", "X-Men", "The Lost World: Jurassic Park", "Isn't She Great"]:
        continue

    newDataset.append([
     row.title,
     row.revenue,
     row.budget,
     row.popularity,
     row.voteAverage,
    ]) 

# Display correlation between revenue and budget with a scatter plot using panda
def display_correlation_revenue_budget(newDataset):
    revenue = []
    budget = []
    for i in range(len(newDataset)):
        revenue.append(newDataset[i][1])
        budget.append(newDataset[i][2])

    # Create scatter plot
    scatter_plot = pd.DataFrame({'Revenue': revenue, 'Budget': budget})
    scatter_plot.plot(kind='scatter', x='Revenue', y='Budget', figsize=(10, 10))
    
    plt.show()

    print('Correlación Pearson: ', df['budget'].corr(df['revenue'], method='pearson'))

# Display correlation between popularity and voteAverage with a scatter plot using panda
def display_correlation_popularity_voteAverage(newDataset):
    popularity = []
    voteAverage = []
    for i in range(len(newDataset)):
        popularity.append(newDataset[i][3])
        voteAverage.append(newDataset[i][4])

    # Create scatter plot
    scatter_plot = pd.DataFrame({'Popularity': popularity, 'Vote Average': voteAverage})
    scatter_plot.plot(kind='scatter', x='Popularity', y='Vote Average', figsize=(10, 10), alpha=0.8)

    print('Correlación Pearson: ', df['voteAverage'].corr(df['popularity'], method='pearson'))
    plt.show()

# Display correlation between revenue and voteAverage with a scatter plot using panda
def display_correlation_revenue_voteAverage(newDataset):
    revenue = []
    voteAverage = []
    for i in range(len(newDataset)):
        revenue.append(newDataset[i][1])
        voteAverage.append(newDataset[i][4])

    # Create scatter plot
    scatter_plot = pd.DataFrame({'Revenue': revenue, 'Vote Average': voteAverage})
    scatter_plot.plot(kind='scatter', x='Revenue', y='Vote Average', figsize=(10, 10), alpha=0.8)

    print('Correlación Pearson: ', df['voteAverage'].corr(df['revenue'], method='pearson'))

    plt.show()

display_correlation_popularity_voteAverage(newDataset)