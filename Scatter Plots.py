#Read the candy data file into candy_data. Use the "id" column to label the rows.
candy_filepath = "../input/candy.csv"
candy_data = pd.read_csv(candy_filepath,index_col='id')

#print the first five rows of the data.
candy_data.head()

#candy that was more popular with survey respondents
more_popular ='3 Musketeers'
#candy that has higher sugar content
more_sugar = 'Air Heads'

#Create a scatter plot that shows the relationship between 'sugarpercent' and 'winpercent' 
plt.figure(figsize=(10,4))
plt.title("Relationship between sugarpercent and winpercent among candies")
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
#the scatter plot doesn't show a strong correlation between the two variables

#scatter plot with a regression line
plt.figure(figsize=(10,4))
plt.title("Relationship between sugarpercent and winpercent among candies")
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

#The regression line shows that there's a little correlation between the two variables which means that people slightly tend to prefer candy with more sugar

#create a scatter plot to show the relationship between 'pricepercent' and 'winpercent' . Use the 'chocolate' column to color-code the points
plt.figure(figsize=(40,6))
plt.title("Relationship between pricepercent and winpercent among candies")# Your code here
sns.swarmplot(x=candy_data['pricepercent'], y=candy_data['winpercent'],hue=candy_data['chocolate']) 

#Create the same scatter plot you created in Step 5, but now with two regression lines, corresponding to (1) chocolate candies and (2) candies without chocolate.
sns.lmplot(x='pricepercent', y='winpercent',hue='chocolate', data=candy_data)

#we conclude that candies without chocolate are more popular the cheaper they are ,and candies with chocolate are more popular the more expensive they are

#Create a categorical scatter plot to highlight the relationship between 'chocolate' and 'winpercent'
sns.swarmplot(x=candy_data['chocolate'],y=candy_data['winpercent'])

#the categorical plot showcases better how chocolate candies are more popular

                            
