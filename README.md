# Stock Exchange Analysis 

The file **Stocks.dat** contains the ``weekly rates of return`` for **five stocks** listed on **the New York Stock Exchange**, denoted as column vectors A, B, C, D, and E. Our objective is to ``estimate the joint distribution`` of the stock pairs and calculate their **covariance** and **correlation**. Our goal is to identify the  pair of stocks with **the highest correlation** and use this information for **investment** purposes.

## 1- Importing Required Libraries

```python 
import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

```
Here, we are importing the required libraries, including NumPy for numerical computations, pandas for data manipulation, seaborn for data visualization, and matplotlib for plotting.

## 2- Loading the Data

```python 
data = pd.read_csv("Stocks.dat", sep="\s+", header=None)

```
Here, we are reading the data from the "Stocks.dat" file using pandas' read_csv() function. We use the sep parameter to specify that the data is separated by one or more whitespace characters, and the header parameter to specify that the data does not have a header row.

## 3- Renaming the Columns

```python 
data.columns = ["A", "B", "C", "D", "E"]

```
Here, we are renaming the columns of the data to A, B, C, D, and E using pandas' columns attribute.

## 4- Computing the Sample Mean Vector and Sample Covariance Matrix
```python 
mu = np.mean(data, axis=0)
Sigma = np.cov(data.T)

```
Here, we are computing the sample mean vector mu and the sample covariance matrix Sigma using NumPy's mean() and cov() functions, respectively. We use the axis parameter to specify that we want to compute the mean along the rows (axis=0) and the covariance matrix along the columns (axis=1).

![image](https://user-images.githubusercontent.com/106637184/225050233-1016dd29-b39b-4e11-86c4-14bb3929c83c.png)


## 5- Printing the Sample Mean Vector and Sample Covariance Matrix
```python 
print("Sample Mean Vector:")
print(mu)
print("\nSample Covariance Matrix:")
print(Sigma)

```
Here, we are printing the sample mean vector mu and the sample covariance matrix Sigma using Python's print() function.

![image](https://user-images.githubusercontent.com/106637184/225050385-d002ee53-51ed-4419-be87-50ed4cab7c0f.png)

## 6- Computing the Correlation Matrix
```python
R = np.corrcoef(data.T)

 ``` 
Here, we are computing the correlation matrix R using NumPy's corrcoef() function. We transpose the data using .T to make sure that the correlation matrix is calculated between pairs of stocks.

![image](https://user-images.githubusercontent.com/106637184/225050504-3b4104ef-0b9e-4326-9996-3c6a8b708302.png)

## 7- Printing the Correlation Matrix
```python
print("\nCorrelation Matrix:")
print(R)

```
## 8- Plotting the Heat Map of the Correlation Matrix

```python
sns.heatmap(R, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

```
Here, we are plotting the heat map of the correlation matrix R using Seaborn's heatmap() function. We set the annot parameter to True to show the correlation coefficients on the heat map, and we set the cmap parameter to "coolwarm" to use a color map that ranges from blue to red. We also add a title to the plot using Matplotlib's title() function and display the plot using show().

![image](https://user-images.githubusercontent.com/106637184/225050025-cfcbff55-3811-435a-96b7-59bc7a9d3f37.png)


## 9- Finding the Pair of Stocks with the Highest Correlation
```python 
max_corr_idx = np.unravel_index(np.argmax(np.abs(R - np.identity(5))), R.shape)
print("\nPair of Stocks with the Highest Correlation: {} and {}".format(chr(max_corr_idx[0]+65), chr(max_corr_idx[1]+65)))

```
Here, we are finding the pair of stocks with the highest correlation by first subtracting the identity matrix from the absolute values of the correlation matrix using NumPy's identity() function and abs() method.

![image](https://user-images.githubusercontent.com/106637184/225050610-64158e8b-8448-4e15-a48b-5a1cd519db87.png)


The **highest correlation between 2 stocks** can be used for investment purposes in many ways. Here are some possibilities:


**1- Diversify your investment portfolio:**
If the two stocks with the highest correlation are positively correlated, they tend to move in the same direction. This means that investing in both stocks will not diversify portfolio risk. In this case, investors may consider investing in less correlated stocks to diversify their portfolio and reduce overall risk.

**2- Pair trading:**
If the two stocks with the highest correlation are positively correlated, an investor can engage in a pair trading strategy, which involves buying one stock and simultaneously selling the other. This strategy takes advantage of the fact that two stocks tend to move in the same direction and tries to capture the price difference.

## Note : 
It is important to note that these strategies are examples only and investors should carefully consider their investment objectives, risk tolerance and other factors before making an investment decision. . It's important to remember that past performance is no guarantee of future results, and correlations between stocks can change over time. 
