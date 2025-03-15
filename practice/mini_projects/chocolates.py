import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = ""

#download = https://www.kaggle.com/datasets/rtatman/chocolate-bar-ratings
df = pd.read_csv(file)

print(df)

len(df) #How many tuples are in the dataset

df.columns

#How many unique company names are there in the dataset?
len(df["Company \n(Maker-if known)"].unique())

df["Review\nDate"].unique()

#How many review were made in 2013?
len(df[df["Review\nDate"] == 2013])

#How many missing values are in the Bean Type column?
df.isna().sum()

#An output plot of the histogram of the values in the column named Ratings
plt.title("Histogram of Ratings ")
plt.hist(df["Rating"], bins = 10)

# Convert to float (whole percentage)
df["Cocoa\nPercent"] = df["Cocoa\nPercent"].str.rstrip('%').astype('float')

df["Cocoa\nPercent"]

plt.title("cocoa percent vs rating")
plt.scatter(df["Cocoa\nPercent"], df["Rating"], alpha = 0.5)

#plots
plt.xlabel('Cocoa Percent (%)')
plt.ylabel('Rating')
plt.title('Cocoa Percent vs Rating')

#Normalize data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df["Normalized_Rating"] = scaler.fit_transform(df[["Rating"]])
df[["Rating", "Normalized_Rating"]]

#List the companies ordered by their average score (averaged over each company’s reviews).

company_average_score = df.groupby("Company \n(Maker-if known)")["Normalized_Rating"].mean()
company_average_score = company_average_score.sort_values(ascending=False)
company_average_score 
