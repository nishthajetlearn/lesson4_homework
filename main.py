import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# 1. Find the mean fare of passengers with respect to sex and Pclass
mean_fare = df.groupby(['Sex', 'Pclass'])['Fare'].mean().reset_index()

# Display the mean fare for all combinations
print("Mean Fare of Passengers with respect to Sex and Pclass:")
print(mean_fare)

# 2. Find the median age of passengers who died with respect to sex
# First, filter the dataset for passengers who did not survive
deceased_passengers = df[df['Survived'] == 0]

# Now, calculate the median age grouped by sex
median_age_deceased = deceased_passengers.groupby('Sex')['Age'].median().reset_index()

# Display the median age for deceased passengers
print("\nMedian Age of Deceased Passengers with respect to Sex:")
print(median_age_deceased)

# You can also calculate the mean age if required
mean_age_deceased = deceased_passengers.groupby('Sex')['Age'].mean().reset_index()
print("\nMean Age of Deceased Passengers with respect to Sex:")
print(mean_age_deceased)
