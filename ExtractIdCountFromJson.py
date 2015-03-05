###############################################
#Script is used to extract ID,count from json twitter data
import json , glob
import os, re
from collections import Counter
import collections
import csv

data=[]
result=[]
result2=[]
result3=[]
i='.json'

regexstring= '*' + i
filename = glob.glob(regexstring)
for j in filename:
    with open(str(j)) as in_file:
        for line in in_file:
            #print len(data)
            data.append(json.loads(line))
            continue
                
print len(data)
for i in range(0,len(data)):
    result.append(data[i]['text'])
    result2.append(data[i]['user']['name'])
    result3.append(data[i]['user']['id'])
    continue
a=Counter(result3)
#print a
#print type(a)
b=sorted(a.iteritems())
#print type(b)
myfile = open("out.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerows(b)

