# An-example-of-Stock-exchange-analysis-for-beginners-using-Python
The weekly rates of return for five stocks listed on the New York Stock Exchange are given in the file Stocks.dat. Call these stock column vectors: A, B, C, D, and E. we will approximate the joint distribution of the pair of stocks. Then we will find the covariance and correlation between each pair of stocks using the approximated probability distribution functions (pdfs) and directly over the data (sample covariance) too. The idea is to find out which two stocks have the highest correlation and how to use this information for investment.


#1 . Plot each column separately in a single plot (different color) and
observe. Which stocks do you think has the highest correlation ?

![image](https://user-images.githubusercontent.com/106637184/178302311-91b7e4c4-0f81-4b01-8826-8f0d596c0e46.png)

According to the plot shown above, which illustrates the correlation
between 5 stocks ( A,B,C,D,E) with respect to the time on the x-axis ,
which was 103 weeks , since the number of rows is 103 , and each row has
5 different values of ( A,B,C,D,and E). After looking into the plot, it seems
that the highest correlation was between stocks (E and D), as shown
below.

![image](https://user-images.githubusercontent.com/106637184/178302522-00f11d04-5fdc-4a6e-aa5d-efc7dd6927bd.png)

 #2. Perform statistical normalization: zero mean + unit variance
 
The code of standardizing 
ZA = zscore(X.A);
histogram(ZE,16);

![image](https://user-images.githubusercontent.com/106637184/178302772-27cadc74-85bd-428f-9209-08fcaf07c6a5.png)

After performing normalization process for each stock vector ( A, B , C ,D , E ) , it is
obvious that each column has shifted to have zero mean , and unit variance .

#3. Compute and plot the joint pdf

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data =pd.read_csv('PASTE THE STocks.dat file location Here',header=None,names=['Stock D','Stock E'])
sns.jointplot(data['Stock D'],data['Stock E'],
kind= 'kde',levels=20)
sns.jointplot(data['Stock D'],data['Stock E'],
kind= 'scatter')
plt.xlabel('Stock D')
plt.xlabel('Stock E')
plt.show()

![image](https://user-images.githubusercontent.com/106637184/178303273-b17e820b-784a-4245-a8e3-10f4d6b8cf4c.png)
![image](https://user-images.githubusercontent.com/106637184/178303293-83ce5ff0-14c8-403a-a056-bf04faf065bb.png)

#4. Estimate the Covariance from the joint pdf ( probabiltiy density function ) .

with open('PASTE THE STocks.csv file location Here','r') as f:
g=f.readlines()

# Each line is split based on commas, and the list of floats are formed
sep_length = [float(x.split(',')[0]) for x in
g[1:]]
sep_width = [float(x.split(',')[1]) for x in
g[1:]]

# Finding the mean of the series x and y
def covariance(x, y):
mean_x = sum(x)/float(len(x))
mean_y = sum(y)/float(len(y))

# Subtracting mean from the individual elements
sub_x = [i - mean_x for i in x]
sub_y = [i - mean_y for i in y]
numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
denominator = len(x)-1
cov = numerator/denominator
return cov
with open('PASTE THE STocks.csv file location Here', 'r') as f:
cov_func = covariance(sep_length, sep_width)
print("Covariance from the custom function:",cov_func)

#5. Estimate the correlation from the joint pdf ( probabiltiy density function ) 

def correlation(x, y):
# Finding the mean of the series x and y ( not for indvidual elements but for series of elements) 
mean_x = sum(x)/float(len(x))
mean_y = sum(y)/float(len(y))
# Subtracting mean from the individual elements
sub_x = [i-mean_x for i in x]
sub_y = [i-mean_y for i in y]

# covariance for x and y
numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
# Standard Deviation of x and y
std_deviation_x = sum([sub_x[i]**2.0 for i in range(len(sub_x))])
std_deviation_y = sum([sub_y[i]**2.0 for i in range(len(sub_y))])
# squaring by 0.5 to find the square root
denominator = (std_deviation_x*std_deviation_y)**0.5 # short but
equivalent to (std_deviation_x**0.5) * (std_deviation_y**0.5)
cor = numerator/denominator
return cor
with open('PASTE THE STocks.csv file location Here', 'r') as f:
cor_func = correlation(sep_length, sep_width)
print("Correlation from the custom function:", cor_func)

#Output Sample : 
Covericance and cor between AB
Covariance from the custom function: 0.0002794144478856378
Correlation from the custom function: 0.636158155633225

#6. Calculate sample Covariance/Correlation matrices
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
with open('PASTE THE STocks.dat file location Here','r') as f:
g=f.readlines()

# Each line is split based on commas, and
the list of floats are formed
A = [float(x.split(',')[0]) for x in g[1:]]
B = [float(x.split(',')[1]) for x in g[1:]]
C = [float(x.split(',')[2]) for x in g[1:]]
D = [float(x.split(',')[3]) for x in g[1:]]
E = [float(x.split(',')[4]) for x in g[1:]]
AB = np.corrcoef(A,B)
AC= np.corrcoef(A,C)
print("AB\n ", AB)
print("AC\n ", AC)

#Output Sample : 
AB
[[1      0.63615816]
[0.63615816     1 ]]
AC
[[1      0.51343318]
[0.51343318     1.]]
AD
[[1      0.12724268]
[0.12724268     1 ]]

![image](https://user-images.githubusercontent.com/106637184/178304256-74157a03-9a9a-4ff6-bea2-e174f978f248.png)

#Conclusions 
As we can see, the diagonal elements are the same , from left upper corner to
right lower corner , or vice versa . Furthermore, it is noticed that the highest
correlation is between Stocks E and D , as illustrated in the diagonal
elements of correlation matrix between E and D , which is 0.69560044 . By
comparing the two correlations, the one that we have obtained before by
estimation using joint pdf, and the one that has been obtained by covarianc/ correlation matrix, we can see that the correlation matrix was estimated
from the joint pdf. the highest correlation by joint pdf was
“0.6956004427835351”, which has been approximated to “0.69560044”,
after using the matrix method.
The correlation between stocks E & D is the highest, while the lowest
correlation was between stocks A & D.

![image](https://user-images.githubusercontent.com/106637184/178304450-4711c373-8cad-424f-98b7-68a0f554fe75.png)
'
![image](https://user-images.githubusercontent.com/106637184/178304539-e8ff76c5-9361-4de6-9c9f-0c87be4679bf.png)

#Critical thinking Question : how can you use the “stock correlation” information for investment (to reduce the risks-OR- maximize the profits) ?

After plotting the data between the stocks, and understanding what the correlation
between the stocks is, and specifying the highest and lowest correlation. I guess
that stock correlation is a very good indicator for the rising and falling of two
different stocks. For example, if we have company A and Company B, both
companies have a stock correlation, let us say about 0.9, which means that both
companies have a chance of 90% to rise or fall at the same time. After that, during
the next years, the company will refer to the old data, were it was having the
highest possible correlation, so that it can reduce the risks .

#Sources :
https://www.youtube.com/watch?v=TiADzIbeO38
https://pythonhosted.org/prob140/joint_tutorial.html
https://dlsun.github.io/symbulate/joint.html
https://stackabuse.com/covariance-and-correlation-in-python/
https://seaborn.pydata.org/generated/seaborn.jointplot.html
https://datatofish.com/correlation-matrix-pandas/
