import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

array = [5,7,3,9,6,2,8,1,4,5,12,28,39,17,25,62,48,57,32,85,94,77,62,43]
ArrayMedianResult = np.median(array)#Median is a value means mid value of data collection which is sorted from smallest value to biggest value.  
ArrayMeanResult = np.mean(array)#Mean value means average 
ArrayModeResult = stats.mode(array)#Mode means most repeated value in data collection.
ArrayVarianceResult = np.var(array) #Variance is a value corresponding to in a data collection summary of all datas squared diffrences from mean of data collection. 
ArraySTD_Result= np.std(array) #std(Standart Deviation) is a value that square root of Variance value. Standart Deviation gives us knowledge about data distribution
                          #Low std means datas close to the mean value of data collection. High value is meaning opposite of it which Distribution of values are on wider area.
ArrayPercentile = np.percentile(array,50)#Percentile gives us key value that means all datas having LOWER value than this key value are providing wanted percentage of data collection  

print("median:",ArrayMedianResult)
print("mean:",ArrayMeanResult)
print("Mode:",ArrayModeResult)
print("Variance:",ArrayVarianceResult)
print("Standart Deviation",ArraySTD_Result)
print("Percentile:",ArrayPercentile)

#FORMING AND PRESENTING DATA SETS

#Pure Data Set 
Formed_Float_DataSet = np.random.uniform(0.0 , 10.0 , 100000) #We created a dataset which has 100000 float values between 0 and 10
plt.hist(Formed_Float_DataSet, 100)#We draw a histogram with our created dataset (Histogram Graph gave us frequency of dataset) the second input means column number of graph
plt.show()

#Normal Data Distribution
Formed_Float_Normal_DataSet = np.random.normal(5.0 , 1.0, 100)#Normal Data Distribution is a data distribution theory belongs to Carl Friedrich Gauss which is included datas distributed around the mean value according to Standart Deviation Value
plt.hist(Formed_Float_Normal_DataSet, 5)
plt.show()

#Scatter Plot

ScatterDataSet1 = [5,7,9,6,3,8,4,2,5,7]#Scatter Plot is a histogram that gives us data set presentation with dots. Doing peer to peer scaling for getting united histogram from two diffrent histograms.
ScatterDataSet2 = [55,94,36,17,24,85,64,37,62,58]#Datasets must have same length so scatter function can put one of them to x-axis and the other to y-axis.  
plt.scatter(ScatterDataSet1,ScatterDataSet2)
plt.show()

#REGRESSION

#Linear Regression


