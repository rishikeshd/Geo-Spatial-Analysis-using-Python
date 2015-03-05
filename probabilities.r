#######################################################
#Script to find out probability matrix for twitter data
###Setting current directory
setwd('/Users/rishikeshdole/Documents/Py/Probabilities')
getwd()

##################################
#Loading multiple files from a folder
temp = list.files(pattern="*.csv")
#k=1
#################################
#For loop to extract all files in a folder and to find probability table for all
#It also includes how to write those tables into different files based on variable filename
for (i in 1:length(temp)) {
inp <- read.csv(file=temp[i], header=TRUE)
name <- sub(".csv","", temp[i])
assign( temp[i], inp)
rm(inp)
a<-temp[i]
tb<-table(get(a)$timecat,get(a)$cat)
tbd<-prop.table(tb)
write.table(tbd,file=paste("out", i, ".txt", sep = "\t"))
#k=k+1
}
