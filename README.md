# Stock Exchange Analysis 
## 1- Importing Required Libraries

```python import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

```
Here, we are importing the required libraries, including NumPy for numerical computations, pandas for data manipulation, seaborn for data visualization, and matplotlib for plotting.

## 2- Loading the Data
```python data = pd.read_csv("Stocks.dat", sep="\s+", header=None)

```
Here, we are reading the data from the "Stocks.dat" file using pandas' read_csv() function. We use the sep parameter to specify that the data is separated by one or more whitespace characters, and the header parameter to specify that the data does not have a header row.

## 3- Renaming the Columns
```python data.columns = ["A", "B", "C", "D", "E"]

```
Here, we are renaming the columns of the data to A, B, C, D, and E using pandas' columns attribute.

## 4- Computing the Sample Mean Vector and Sample Covariance Matrix
```python mu = np.mean(data, axis=0)
Sigma = np.cov(data.T)

```
Here, we are computing the sample mean vector mu and the sample covariance matrix Sigma using NumPy's mean() and cov() functions, respectively. We use the axis parameter to specify that we want to compute the mean along the rows (axis=0) and the covariance matrix along the columns (axis=1).

## 5- Printing the Sample Mean Vector and Sample Covariance Matrix
```python print("Sample Mean Vector:")
print(mu)
print("\nSample Covariance Matrix:")
print(Sigma)

```
Here, we are printing the sample mean vector mu and the sample covariance matrix Sigma using Python's print() function.

## 6- Computing the Correlation Matrix
```python R = np.corrcoef(data.T)

 ``` 
Here, we are computing the correlation matrix R using NumPy's corrcoef() function. We transpose the data using .T to make sure that the correlation matrix is calculated between pairs of stocks.

## 7- Printing the Correlation Matrix
```python print("\nCorrelation Matrix:")
print(R)

```
## 8- Plotting the Heat Map of the Correlation Matrix

```python sns.heatmap(R, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

```
Here, we are plotting the heat map of the correlation matrix R using Seaborn's heatmap() function. We set the annot parameter to True to show the correlation coefficients on the heat map, and we set the cmap parameter to "coolwarm" to use a color map that ranges from blue to red. We also add a title to the plot using Matplotlib's title() function and display the plot using show().

## 9- Finding the Pair of Stocks with the Highest Correlation
```python max_corr_idx = np.unravel_index(np.argmax(np.abs(R - np.identity(5))), R.shape)
print("\nPair of Stocks with the Highest Correlation: {} and {}".format(chr(max_corr_idx[0]+65), chr(max_corr_idx[1]+65)))

```
Here, we are finding the pair of stocks with the highest correlation by first subtracting the identity matrix from the absolute values of the correlation matrix using NumPy's identity() function and abs() method.

