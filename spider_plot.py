import matplotlib.pyplot as plt 
import pandas as pd 
from math import pi 

def normalize(col, low = 0, high = 1):
    min_val = col.min()
    max_val = col.max()
    new = col.apply(lambda x: low + (high - low) * (x - min_val) / (max_val - min_val))
    return new

df = pd.read_csv('data/public_playlist.csv', nrows=4, index_col='name')

cats = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness']
N = len(cats)

radars = df[cats].apply(normalize, axis = 1)
print(radars)

values = radars.iloc[0].values.flatten().tolist()
values += values[:1] # repeat the first value to close the circular graph
print(values)

# Calculate angle of each axis (plot / no. of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialize the radar plot
ax = plt.subplot(111, polar = True)

# Draw one axis per varibale + add labels
plt.xticks(angles[:-1], cats, color = 'grey', size = 8)

# Draw y label
ax.set_rlabel_position(0)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ['0.2', '0.4', '0.6', '0.8', '1.0'], color = 'grey', size = 7)
plt.ylim(0, 1)

# Plot data
ax.plot(angles, values, linewidth = 1, linestyle = 'solid')

# Fill area
ax.fill(angles, values, 'b', alpha = 0.1)

plt.show()