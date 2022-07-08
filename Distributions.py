#Load the data
cancer_filepath = "../input/cancer.csv"
cancer_data =pd.read_csv( "../input/cancer.csv",index_col='Id')

#Review the data
cancer_data.head()


#In the first five rows of the data, what is the
# largest value for 'Perimeter 
max_perim = 87.46
#the value for 'Radius ' for the tumor with Id 8510824
mean_radius =9.504

# create two histograms that show the distribution in values for 'Area (mean)', separately for both benign and malignant tumors
sns.histplot(data=cancer_data,x='Area (mean)',hue='Diagnosis')
plt.title("Histograms for Area distribution in benign and malignant tumors")
#Malignant tumors have high Area(mean) values

#create two KDE plots that show the distribution in values for 'Radius (worst)', separately for both benign and malignant tumors.
sns.kdeplot(data=cancer_data,x='Radius (worst)',hue='Diagnosis',shade=True)
plt.title("Distribution in values for Radius (worst) for benign and malignant tumors")

#Given a tumor with a value for 'Radius (worst)' of 25 it will more likely be Malignant according to the plot
