## StockExchangeAnalysisPython
#### The weekly rates of return for five stocks listed on the New York Stock Exchange are given in the file Stocks.dat.<br> Call these stock column vectors: A, B, C, D, and E. we will approximate the joint distribution of the pair of stocks.</br>  Then we will find the covariance and correlation between each pair of stocks using the approximated probability distribution functions (pdfs) and directly over the data (sample covariance) too.</br> The idea is to find out which two stocks have the highest correlation and how to use this information for investment.


## 1 . Plot each column separately in a single plot (different color) and observe. ***Which stocks do you think has the highest correlation ?***

![image](https://user-images.githubusercontent.com/106637184/178302311-91b7e4c4-0f81-4b01-8826-8f0d596c0e46.png)

**According to the plot shown above, which illustrates the correlation 
between 5 stocks ( A,B,C,D,E) with respect to the time on the x-axis ,
which was 103 weeks , since the number of rows is 103 , and each row has
5 different values of ( A,B,C,D,and E). After looking into the plot, it seems
that the highest correlation was between stocks (E and D), as shown
below.**

![image](https://user-images.githubusercontent.com/106637184/178302522-00f11d04-5fdc-4a6e-aa5d-efc7dd6927bd.png)

 ## 2. Perform statistical normalization: zero mean + unit variance .
 
**ZA = zscore(X.A);**
<br>**histogram(ZE,16);**</br>

![image](https://user-images.githubusercontent.com/106637184/178302772-27cadc74-85bd-428f-9209-08fcaf07c6a5.png)

**After performing normalization process for each stock vector ( A, B , C ,D , E ) , it is
obvious that each column has shifted to have zero mean , and unit variance .**

## 3. Compute and plot the joint pdf .

<br>**import numpy as np</br>
import matplotlib.pyplot as plt</br>
import seaborn as sns</br>
import pandas as pd</br>
data =pd.read_csv('PASTE THE STocks.dat file location Here',header=None,names=['Stock D','Stock E'])</br>
sns.jointplot(data['Stock D'],data['Stock E'],kind= 'kde',levels=20)</br>
sns.jointplot(data['Stock D'],data['Stock E'],kind= 'scatter')</br>
plt.xlabel('Stock D')</br>
plt.xlabel('Stock E')</br>
plt.show()**</br>

![image](https://user-images.githubusercontent.com/106637184/178303273-b17e820b-784a-4245-a8e3-10f4d6b8cf4c.png)
![image](https://user-images.githubusercontent.com/106637184/178303293-83ce5ff0-14c8-403a-a056-bf04faf065bb.png)

## 4. Estimate the Covariance from the joint pdf ( probabiltiy density function ) .

<br>**with open('PASTE THE STocks.csv file location Here','r') as f**:</br>
**g=f.readlines()**</br>

## Each line is split based on commas, and the list of floats are formed .
<br>**sep_length = [float(x.split(',')[0]) for x in g[1:]]**</br>
**sep_width = [float(x.split(',')[1]) for x in g[1:]]**</br>

## Finding the mean of the series x and y .
<br>**def covariance(x, y):**</br>
**mean_x = sum(x)/float(len(x))**</br>
**mean_y = sum(y)/float(len(y))**</br>

## Subtracting mean from the individual elements.
<br>**sub_x = [i - mean_x for i in x]**</br>
**sub_y = [i - mean_y for i in y]**</br>
**numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])**</br>
**denominator = len(x)-1**</br>
**cov = numerator/denominator**</br>
**return cov**</br>
**with open('PASTE THE STocks.csv file location Here', 'r') as f:**</br>
**cov_func = covariance(sep_length, sep_width)**</br>
**print("Covariance from the custom function:",cov_func)**</br>

## 5. Estimate the correlation from the joint pdf ( probabiltiy density function ) 

<br>**def correlation(x, y):**</br>
## Finding the mean of the series x and y ( not for indvidual elements but for series of elements) .
<br>**mean_ x = sum(x)/float(len(x))**</br>
**mean_ y = sum(y)/float(len(y))**</br>
## Subtracting mean from the individual elements.
<br>**sub_x = [i-mean_x for i in x]</br>
sub_y = [i-mean_y for i in y]**</br>

## covariance for x and y.
<br>**numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))]).**</br>

## Standard Deviation of x and y.
<br>**std_deviation_x = sum([sub_x[i]* *2.0 for i in range(len(sub_x))])**</br>
**std_deviation_y = sum([sub_y[i]* *2.0 for i in range(len(sub_y))])**</br>

## squaring by 0.5 to find the square root
<br>**denominator = (std_deviation_x*std_deviation_y)* *0.5  (# short but equivalent to (std_deviation_x* *0.5) * (std_deviation_y* *0.5) )**</br> 
**cor = numerator/denominator**</br>
**return cor**</br>
**with open('PASTE THE STocks.csv file location Here', 'r') as f:**</br>
**cor_func = correlation(sep_length, sep_width)**</br>
**print("Correlation from the custom function:", cor_func)**</br>

## Output Sample : 
<br>**Covericance and cor between AB**</br>
**Covariance from the custom function: 0.0002794144478856378**</br>
**Correlation from the custom function: 0.636158155633225**</br>

## 6. Calculate sample Covariance/Correlation matrices
<br>**import numpy as np**</br>
**import seaborn as sns**</br>
**import matplotlib.pyplot as plt**</br>
**with open('PASTE THE STocks.dat file location Here','r') as f:**</br>
**g=f.readlines()**</br>

## Each line is split based on commas, and the list of floats are formed
<br>**A = [float(x.split(',')[0]) for x in g[1:]]**</br>
**B = [float(x.split(',')[1]) for x in g[1:]]**</br>
**C = [float(x.split(',')[2]) for x in g[1:]]**</br>
**D = [float(x.split(',')[3]) for x in g[1:]]**</br>
**E = [float(x.split(',')[4]) for x in g[1:]]**</br>
**AB = np.corrcoef(A,B)**</br>
**AC= np.corrcoef(A,C)**</br>
**print("AB\n ", AB)**</br>
**print("AC\n ", AC)**</br>

# Output Sample : 
<br>**AB</br>
[[1       0.63615816]</br>
[0.63615816      1 ]]</br>
AC</br>
[[1      0.51343318]</br>
[0.51343318     1.]]</br>
AD</br>
[[1      0.12724268]</br>
[0.12724268     1 ]]**</br>

![image](https://user-images.githubusercontent.com/106637184/178304256-74157a03-9a9a-4ff6-bea2-e174f978f248.png)

## Conclusions 
**As we can see, the diagonal elements are the same , from left upper corner to
right lower corner , or vice versa . Furthermore, it is noticed that the highest
correlation is between Stocks E and D , as illustrated in the diagonal
elements of correlation matrix between E and D , which is 0.69560044 . By
comparing the two correlations, the one that we have obtained before by
estimation using joint pdf, and the one that has been obtained by covarianc/ correlation matrix, we can see that the correlation matrix was estimated
from the joint pdf. the highest correlation by joint pdf was
“0.6956004427835351”, which has been approximated to “0.69560044”,
after using the matrix method.**
***The correlation between stocks E & D is the highest, while the lowest correlation was between stocks A & D.***

![image](https://user-images.githubusercontent.com/106637184/178304450-4711c373-8cad-424f-98b7-68a0f554fe75.png)
'
![image](https://user-images.githubusercontent.com/106637184/178304539-e8ff76c5-9361-4de6-9c9f-0c87be4679bf.png)

## Critical thinking Question : how can you use the “stock correlation” information for investment (to reduce the risks-OR- maximize the profits) ?

**After plotting the data between the stocks, and understanding what the correlation
between the stocks is, and specifying the highest and lowest correlation. I guess
that stock correlation is a very good indicator for the rising and falling of two
different stocks. For example, if we have company A and Company B, both
companies have a stock correlation, let us say about 0.9, which means that both
companies have a chance of 90% to rise or fall at the same time. After that, during
the next years, the company will refer to the old data, were it was having the
highest possible correlation, so that it can reduce the risks .**

## Sources :
<br>https://www.youtube.com/watch?v=TiADzIbeO38</br>
https://pythonhosted.org/prob140/joint_tutorial.html</br>
https://dlsun.github.io/symbulate/joint.html</br>
https://stackabuse.com/covariance-and-correlation-in-python/</br>
https://seaborn.pydata.org/generated/seaborn.jointplot.html</br>
https://datatofish.com/correlation-matrix-pandas/</br>
