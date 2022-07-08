#setup
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
#Loading
spotify_filepath = "../input/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

## Change the style of the figure
sns.set_style("white")        #we can replace white with : "darkgrid","whitegrid","dark",ticks"

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
