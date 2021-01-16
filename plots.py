import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('data/public_playlist.csv', nrows=4, index_col='name')

# ? Histogram of time
dates = pd.to_datetime(df['release_date'])
plt.figure(figsize = (8, 6))
plt.hist(dates, color = 'grey')
plt.xlabel('Year')
plt.ylabel('Number of Songs')
plt.title('Histogram of songs I listen to by year')
plt.show()


# ? Histogram of tempo
plt.figure(figsize = (8, 6))
plt.hist(df['tempo'], color = 'skyblue')
plt.xlabel('Tempo')
plt.ylabel('Number of Songs')
plt.title('Tempo Histogram')
plt.show()