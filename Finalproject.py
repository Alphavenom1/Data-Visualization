#Setup
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

#uploading netflix-tv-shows dataset link: https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies
my_filepath = "../input/netflix-tv-shows-and-movies/titles.csv"
my_data = pd.read_csv(my_filepath)
my_data.head()    #viewing the first 5 rows 

#Visualizing 
sns.set_style("dark")
plt.figure(figsize=(16,4)) 
sns.histplot(data=my_data,x='release_year',hue='type')
plt.title("Movie and show releases through the years")
