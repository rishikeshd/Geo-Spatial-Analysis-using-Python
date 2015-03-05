#################################################
#Script to find count of tweets from unique 328 users
#################################################
###Setting current directory
setwd('/Users/rishikeshdole/Documents/Py/AllFiles3')
getwd()
###Reading file
task4<-read.csv("file3.csv")
###Calculating unique id v/s count
FileCount <- data.frame(table(task4$id))
####writing and reading again
write.csv(file="FileCount2.csv",FileCount)
FileCount2<-read.csv("FileCount2.csv")
######################################
###Plotting unique id v/s count
library(ggplot2)
a<-ggplot(FileCount2)+aes(FileCount2$srno,FileCount2$Freq)+geom_bar(stat="identity")
 # geom_text(label=text,vjust=1)
a<-a+xlab("id")+ylab("Count")
a+scale_x_discrete(breaks=c("0","50","100","150","200","250","300"))
