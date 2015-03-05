############################################
#Script to find CDF for Washington DC
##Setting current directory
setwd('/Users/rishikeshdole/Documents/Py/Plots/final plots/')
getwd()
######Reading File
file1<-read.csv("Wash1.csv")
library(ggplot2)
###Adding column names
colnames(file1) <- c("srno","id", "Count")
###Finding qplot for DC
q<-qplot(log10(file1$srno),file1$Count,ylab='Count',xlab='srno',main='DC xy plot')
q
################Cumulative Distributive Function
#DC cdf
library(ggplot2)
Count.cdf<-ecdf(log10(file1$Count))
#Count.cdf
r1<-plot(Count.cdf)

