# Made By Hdaw @2021
#Stock-exchange-analysis-for-beginners-using-Python
# See the Requirements before Compiling this code .
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
Stocks_file="Paste File location Here !"
#The Code For determing joint pdf ( probability density function ) between Stocks D & E
# You can apply the same code between stocks A and B , or any other two indpendent stocks .
data =pd.read_csv(Stocks_file,header=None,names=['Stock D','Stock E'])
sns.jointplot(data['Stock D'],data['Stock E'],kind= 'kde',levels=20)
sns.jointplot(data['Stock D'],data['Stock E'],kind= 'scatter')
plt.xlabel('Stock D')
plt.xlabel('Stock E')
plt.show()
#Estimate the Covariance/Correlation from the joint pdf.
with open(Stocks_file,'r') as f:
                       g=f.readlines()
                       # Each line is split based on commas, and the list of floats are formed
                       sep_length = [float(x.split(',')[0]) for x in g[1:]]
                       sep_width = [float(x.split(',')[1]) for x in g[1:]]
def covariance(x, y):
            # Finding the mean of the series x and y
            mean_x = sum(x)/float(len(x))
            mean_y = sum(y)/float(len(y))
            # Subtracting mean from the individual elements
            sub_x = [i - mean_x for i in x]
            sub_y = [i - mean_y for i in y]
            numerator = sum([sub_x[i]*sub_y[i] for i in
            range(len(sub_x))])
            denominator = len(x)-1
            cov = numerator/denominator
            return cov
with open(Stocks_file, 'r') as f:
           cov_func = covariance(sep_length, sep_width)
           print("Covariance from the custom function:",cov_func)
def correlation(x, y):
       # Finding the mean of the series x and y
       mean_x = sum(x)/float(len(x))
       mean_y = sum(y)/float(len(y))
       # Subtracting mean from the individual elements
       sub_x = [i-mean_x for i in x]
       sub_y = [i-mean_y for i in y]
       # covariance for x and y
       numerator = sum([sub_x[i] * sub_y[i] for i in range(len(sub_x))])
       # Standard Deviation of x and y
       std_deviation_x = sum([sub_x[i] ** 2.0 for i in range(len(sub_x))])
       std_deviation_y = sum([sub_y[i] ** 2.0 for i in range(len(sub_y))])
       # squaring by 0.5 to find the square root
       denominator = (std_deviation_x * std_deviation_y) ** 0.5  # short but equivalent to(std_deviation_x ** 0.5) * (std_deviation_y ** 0.5)
       cor = numerator / denominator
       return cor
with open(Stocks_file, 'r') as f:
           cor_func = correlation(sep_length, sep_width)
           print("Correlation from the custom function:",cor_func)
with open(Stocks_file,'r') as f:
                        g=f.readlines()
                        # Each line is split based on commas, and the list of floats are formed
                        A = [float(x.split(',')[0]) for x in g[1:]]
                        B = [float(x.split(',')[1]) for x in g[1:]]
                        C = [float(x.split(',')[2]) for x in g[1:]]
                        D = [float(x.split(',')[3]) for x in g[1:]]
                        E = [float(x.split(',')[4]) for x in g[1:]]
AB = np.corrcoef(A,B)
AC= np.corrcoef(A,C)
AD=np.corrcoef(A,D)
AE=np.corrcoef(A,E)
BC=np.corrcoef(B,C)
BD=np.corrcoef(B,D)
BE=np.corrcoef(B,E)
CD=np.corrcoef(C,D)
CE=np.corrcoef(C,E)
DE=np.corrcoef(D,E)
print("AB\n ", AB)
print("AC\n ", AC)
print("AD\n ", AD)
print("AE\n ", AE)
print("BC\n ", BC)
print("BD\n ", BD)
print("BE\n ", BE)
print("CD\n ", CD)
print("CE\n ", CE)
print("DE\n ", DE)
