import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the "Stocks.dat" file
data = pd.read_csv(""copy the file path HERE of Stocks"/Stocks.CSV", sep="\s+", header=None)

# Rename the columns as A, B, C, D, and E
data.columns = ["A", "B", "C", "D", "E"]

# Compute the sample mean vector mu and the sample covariance matrix Sigma
mu = np.mean(data, axis=0)
Sigma = np.cov(data.T)

# Print the sample mean vector mu and the sample covariance matrix Sigma
print("Sample Mean Vector:")
print(mu)
print("\nSample Covariance Matrix:")
print(Sigma)

# Compute the correlation matrix R
R = np.corrcoef(data.T)

# Print the correlation matrix R
print("\nCorrelation Matrix:")
print(R)

# Plot the heat map of the correlation matrix R
sns.heatmap(R, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Find the indices of the maximum correlation coefficient in R
max_corr_idx = np.unravel_index(np.argmax(np.abs(R - np.identity(5))), R.shape)

# Print the pair of stocks with the highest correlation
print("\nPair of Stocks with the Highest Correlation: {} and {}".format(chr(max_corr_idx[0]+65), chr(max_corr_idx[1]+65)))
