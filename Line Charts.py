#Environement
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

#Load the data
# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath,index_col='Date',parse_dates=True)

#Review the data :Use a Python command to print the last 5 rows of the data.
museum_data.tail()

#How many visitors did the Chinese American Museum receive in July 2018?
ca_museum_jul18 =2620

#In October 2018, how many more visitors did Avila Adobe receive than the Firehouse Museum?
avila_oct18 = 14658

#Create a line chart that shows how the number of visitors to each museum evolved over time. 
plt.figure(figsize=(16,4))
plt.title("Number of visitors over time")
sns.lineplot(data=museum_data)

#Create a line chart that shows how the number of visitors to Avila Adobe has evolved over time
plt.figure(figsize=(16,4))
plt.title("Avila Adobe visitors over time")
sns.lineplot(data=museum_data['Avila Adobe'],label="Avila Adobe")
plt.xlabel("Years")

#Does Avila Adobe get more visitors: in September-February (in LA, the fall and winter months), or in March-August (in LA, the spring and summer)?
#It gets more visitors during spring and summer because the number of visitors is higher in March-August and Lower in September-February
