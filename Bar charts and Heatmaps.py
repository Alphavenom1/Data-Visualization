#setup
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#Read the IGN data file into ign_data. Use the "Platform" column to label the rows.
ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath,index_col='Platform')

#print the entire dataset
print(ign_data.to_string())

#the highest average score received by PC games,for any genre?
high_score = 7.759930

#lowest average score? 
worst_genre ='Simulation'

#Create a bar chart that shows the average score for racing games, for each platform. Your chart should have one bar for each platform.
plt.figure(figsize=(40,10))
plt.title("Average score for racing games")
sns.barplot(x=ign_data.index,y=ign_data['Racing'])
plt.ylabel("IGN plateforms")

#Based on the bar chart, the wii racing games has a lower score than all of the other platforms

#create a heatmap of average score by genre and platform.
plt.figure(figsize=(16,10))
plt.title("Heatmap of average score by genre and platform")
sns.heatmap(data=ign_data,annot=True)
plt.ylabel("IGN platforms")

#combination of genre and platform receives the highest average ratings: Playstation 4 Simulation games
#combination of genre and platform receives the lowest average ratings: GameBoy Color : Fighting and Shooting
