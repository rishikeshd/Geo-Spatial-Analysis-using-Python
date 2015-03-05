############################################
#Script is used to extract only those users which we need to extract from JSON data
#and also to remove empty or non-valid rows and to extract id, created,geo

import csv
import json

arr_users=[]
arr_id=[]
arr_id2=[]
arr_cr=[]
arr_cr2=[]
arr_geo=[]
arr_geo2=[]

with open('ids2.txt','r+') as in_file:
    for line in in_file:
        line=line.strip('\n')
        arr_users.append(line)



with open('all_files.csv', 'rU') as f:
    reader = csv.reader(f)
    csv.register_dialect('pipes', delimiter=',')
    reader.next()
    for line in reader:
        arr_id.append(line[1])
        arr_cr.append(line[2])
        arr_geo.append(line[3])

for i in arr_users:
    for item,j in enumerate(arr_id):
        if j==i:
            #print i
            arr_id2.append(arr_id[item])
            arr_cr2.append(arr_cr[item])
            arr_geo2.append(arr_geo[item])
        continue
    continue
"""
print arr_id2[1000]
print arr_cr2[1000]
print arr_geo2[1000]
"""
print len(arr_id2)
print len(arr_cr2)
print len(arr_geo2)

result = zip(arr_id2,arr_cr2, arr_geo2)
with open('file2.csv', 'wb') as fin:
    writer = csv.writer(fin, delimiter = ',')
    writer.writerows(result)
#print result[0]

            
            
