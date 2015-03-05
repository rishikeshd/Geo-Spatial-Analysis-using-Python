##############################################################
#Script is used to extract data from csv files and perform operations like
#Cleaning geo coordinates to lat, long
#Cleaning created_at to only time at which the user tweeted
#Convert coordinate system data in array from DD to DMS(Degree Minutes Seconds)
#Dividing lat,long into different squares of a geo-located matrix for city DC
#Categorizing time to different time categories like Morning, Evening and Night


import logging
import os, sys
import csv
import collections
import re
import string
import time

def ReadFromCsv():
    ####Used to read csv data into different arrays
    with open('all_use.csv', 'rU') as f:
        reader = csv.reader(f)
        csv.register_dialect('pipes', delimiter=',')
        reader.next()
        for line in reader:
            arr_id.append(line[0])
            arr_cr.append(line[1])
            arr_geo.append(line[2])
    print len(arr_id)
    print len(arr_cr)
    print len(arr_geo)
    return arr_id,arr_cr,arr_geo

def CleanCrGeo(arr_id,arr_cr,arr_geo):
    #Cleans created_at and geo coordinates
    for item,i in enumerate(arr_id):
        word=arr_cr[item]
        a,b,c,d,e,f=word.split(" ")
        arr_cr2.append(d)
        world=arr_geo[item]
        m,n=world.split(",")
        m=m.replace('[','')
        n=n.replace(']','')
        arr_lat.append(m)
        arr_long.append(n)
    #print len(arr_lat)
    return arr_cr2,arr_lat,arr_long
        
    

def DDToDMS(arr_id,arr_lat,arr_long):
    #converts coordinates of geo from DD to DMS(Degree Minutes Seconds)
    for i in arr_lat:
        i=float(i)
        mnt,sec = divmod(i*3600,60)
        deg,mnt = divmod(mnt,60)
        #print deg,mnt,sec
        dms_lat=str(int(deg))+"."+str(int(mnt))+str(int(round(float(sec))))
        arr_lat2.append(dms_lat)
        continue
    for j in arr_long:
        j=float(j)
        mnt,sec = divmod(j*3600,60)
        deg,mnt = divmod(mnt,60)
        #print deg,mnt,sec
        dms_long=str(int(deg))+"."+str(int(mnt))+str(int(round(float(sec))))
        arr_long2.append(dms_long)
        continue

    #print len(arr_lat2)
    #print len(arr_long2)
    return arr_lat2,arr_long2

def DivideTimeToCategory(arr_id,arr_cr2):
    #Categorizing time to different time categories like Morning, Evening and Night
    for i in arr_cr2:
        #print i
        h,m,s=i.split(":")
        h=int(h)
        if int(h)>=5 and int(h)<=11:
            arr_timecat.append("Morning")
        elif int(h)>=12 and int(h)<=17:
            arr_timecat.append("Evening")
        elif (int(h)>=18 and int(h)<=23) or (int(h)>=0 and int(h)<=4):
            arr_timecat.append("Night")
        continue
    return arr_timecat

def DivideLatLongIntoCategory(arr_id,arr_lat2,arr_long2):
    #dividing lat,long into 64 squares of a geolocated matrix for city DC
    for item,i in enumerate(arr_id):
        #print arr_long[item]
        latit=float(arr_lat2[item])
        longit=float(arr_long2[item])
        longit=longit*(-1)
        if latit>=38.5750 and latit<=38.5900 and longit<=77.10 and longit>=77.08:
            arr_cat.append("1")
        elif latit>=38.5750 and latit<=38.5900 and longit<=77.08 and longit>=77.06:
            arr_cat.append("2")
        elif latit>=38.5750 and latit<=38.5900 and longit<=77.06 and longit>=77.04:
            arr_cat.append("3")
        elif latit>=38.5750 and latit<=38.5900 and longit<=77.04 and longit>=77.02:
            arr_cat.append("4")
        elif latit>=38.5750 and latit<=38.5900 and longit<=77.02 and longit>=77.00:
            arr_cat.append("5")
        elif latit>=38.5750 and latit<=38.5900 and longit<=77.00 and longit>=76.58:
            arr_cat.append("6")
        elif latit>=38.5750 and latit<=38.5900 and longit<=76.58 and longit>=76.56:
            arr_cat.append("7")
        elif latit>=38.5750 and latit<=38.5900 and longit<=76.56 and longit>=76.54:
            arr_cat.append("8")
        elif latit>=38.5600 and latit<=38.5750 and longit<=77.10 and longit>=77.08:
            arr_cat.append("9")
        elif latit>=38.5600 and latit<=38.5750 and longit<=77.08 and longit>=77.06:
            arr_cat.append("10")
        elif latit>=38.5600 and latit<=38.5750 and longit<=77.06 and longit>=77.04:
            arr_cat.append("11")
        elif latit>=38.5600 and latit<=38.5750 and longit<=77.04 and longit>=77.02:
            arr_cat.append("12")
        elif latit>=38.5600 and latit<=38.5750 and longit<=77.02 and longit>=77.00:
            arr_cat.append("13")
        elif latit>=38.5600 and latit<=38.5750 and longit<=77.00 and longit>=76.58:
            arr_cat.append("14")
        elif latit>=38.5600 and latit<=38.5750 and longit<=76.58 and longit>=76.56:
            arr_cat.append("15")
        elif latit>=38.5600 and latit<=38.5750 and longit<=76.56 and longit>=77.54:
            arr_cat.append("16")
        elif latit>=38.5450 and latit<=38.5600 and longit<=77.10 and longit>=77.08:
            arr_cat.append("17")
        elif latit>=38.5450 and latit<=38.5600 and longit<=77.08 and longit>=77.06:
            arr_cat.append("18")
        elif latit>=38.5450 and latit<=38.5600 and longit<=77.06 and longit>=77.04:
            arr_cat.append("19")
        elif latit>=38.5450 and latit<=38.5600 and longit<=77.04 and longit>=77.02:
            arr_cat.append("20")
        elif latit>=38.5450 and latit<=38.5600 and longit<=77.02 and longit>=77.00:
            arr_cat.append("21")
        elif latit>=38.5450 and latit<=38.5600 and longit<=77.00 and longit>=76.58:
            arr_cat.append("22")
        elif latit>=38.5450 and latit<=38.5600 and longit<=76.58 and longit>=76.56:
            arr_cat.append("23")
        elif latit>=38.5450 and latit<=38.5600 and longit<=76.56 and longit>=76.54:
            arr_cat.append("24")
        elif latit>=38.5300 and latit<=38.5450 and longit<=77.10 and longit>=77.08:
            arr_cat.append("25")
        elif latit>=38.5300 and latit<=38.5450 and longit<=77.08 and longit>=77.06:
            arr_cat.append("26")
        elif latit>=38.5300 and latit<=38.5450 and longit<=77.06 and longit>=77.04:
            arr_cat.append("27")
        elif latit>=38.5300 and latit<=38.5450 and longit<=77.04 and longit>=77.02:
            arr_cat.append("28")
        elif latit>=38.5300 and latit<=38.5450 and longit<=77.02 and longit>=77.00:
            arr_cat.append("29")
        elif latit>=38.5300 and latit<=38.5450 and longit<=77.00 and longit>=76.58:
            arr_cat.append("30")
        elif latit>=38.5300 and latit<=38.5450 and longit<=76.58 and longit>=76.56:
            arr_cat.append("31")
        elif latit>=38.5300 and latit<=38.5450 and longit<=76.56 and longit>=76.54:
            arr_cat.append("32")
        elif latit>=38.5150 and latit<=38.5300 and longit<=77.10 and longit>=77.08:
            arr_cat.append("33")
        elif latit>=38.5150 and latit<=38.5300 and longit<=77.08 and longit>=77.06:
            arr_cat.append("34")
        elif latit>=38.5150 and latit<=38.5300 and longit<=77.06 and longit>=77.04:
            arr_cat.append("35")
        elif latit>=38.5150 and latit<=38.5300 and longit<=77.04 and longit>=77.02:
            arr_cat.append("36")
        elif latit>=38.5150 and latit<=38.5300 and longit<=77.02 and longit>=77.00:
            arr_cat.append("37")
        elif latit>=38.5150 and latit<=38.5300 and longit<=77.00 and longit>=76.58:
            arr_cat.append("38")
        elif latit>=38.5150 and latit<=38.5300 and longit<=76.58 and longit>=76.56:
            arr_cat.append("39")
        elif latit>=38.5150 and latit<=38.5300 and longit<=76.56 and longit>=76.54:
            arr_cat.append("40")
        elif latit>=38.5000 and latit<=38.5150 and longit<=77.10 and longit>=77.08:
            arr_cat.append("41")
        elif latit>=38.5000 and latit<=38.5150 and longit<=77.08 and longit>=77.06:
            arr_cat.append("42")
        elif latit>=38.5000 and latit<=38.5150 and longit<=77.06 and longit>=77.04:
            arr_cat.append("43")
        elif latit>=38.5000 and latit<=38.5150 and longit<=77.04 and longit>=77.02:
            arr_cat.append("44")
        elif latit>=38.5000 and latit<=38.5150 and longit<=77.02 and longit>=77.00:
            arr_cat.append("45")
        elif latit>=38.5000 and latit<=38.5150 and longit<=77.00 and longit>=76.58:
            arr_cat.append("46")
        elif latit>=38.5000 and latit<=38.5150 and longit<=76.58 and longit>=76.56:
            arr_cat.append("47")
        elif latit>=38.5000 and latit<=38.5150 and longit<=76.56 and longit>=76.54:
            arr_cat.append("48")
        elif latit>=38.4850 and latit<=38.5000 and longit<=77.10 and longit>=77.08:
            arr_cat.append("49")
        elif latit>=38.4850 and latit<=38.5000 and longit<=77.08 and longit>=77.06:
            arr_cat.append("50")
        elif latit>=38.4850 and latit<=38.5000 and longit<=77.06 and longit>=77.04:
            arr_cat.append("51")
        elif latit>=38.4850 and latit<=38.5000 and longit<=77.04 and longit>=77.02:
            arr_cat.append("52")
        elif latit>=38.4850 and latit<=38.5000 and longit<=77.02 and longit>=77.00:
            arr_cat.append("53")
        elif latit>=38.4850 and latit<=38.5000 and longit<=77.00 and longit>=76.58:
            arr_cat.append("54")
        elif latit>=38.4850 and latit<=38.5000 and longit<=76.58 and longit>=76.56:
            arr_cat.append("55")
        elif latit>=38.4850 and latit<=38.5000 and longit<=76.56 and longit>=76.54:
            arr_cat.append("56")
        elif latit>=38.4700 and latit<=38.4850 and longit<=77.10 and longit>=77.08:
            arr_cat.append("57")
        elif latit>=38.4700 and latit<=38.4850 and longit<=77.08 and longit>=77.06:
            arr_cat.append("58")
        elif latit>=38.4700 and latit<=38.4850 and longit<=77.06 and longit>=77.04:
            arr_cat.append("59")
        elif latit>=38.4700 and latit<=38.4850 and longit<=77.04 and longit>=77.02:
            arr_cat.append("60")
        elif latit>=38.4700 and latit<=38.4850 and longit<=77.02 and longit>=77.00:
            arr_cat.append("61")
        elif latit>=38.4700 and latit<=38.4850 and longit<=77.00 and longit>=76.58:
            arr_cat.append("62")
        elif latit>=38.4700 and latit<=38.4850 and longit<=76.58 and longit>=76.56:
            arr_cat.append("63")
        elif latit>=38.4700 and latit<=38.4850 and longit<=76.56 and longit>=76.54:
            arr_cat.append("64")
        else:
            arr_cat.append("0")
    return arr_cat
        

def ExtractUniqueId(arr_id,arr_cr2,arr_lat,arr_long,arr_lat2,arr_long2,arr_timecat,arr_cat):
    #Extracting the unique ids from a large array of twitter and putting them into a dictionary
    my_dict={}
    for (ind,elem) in enumerate(arr_id):
        if elem in my_dict:
            my_dict[elem].append(ind)
        else:
            my_dict.update({elem:[ind]})
    for key,value in my_dict.iteritems():
        #print "key(%s) has indices (%s)" %(key,value)
        for j in value:
            dict1[str(key)].append([arr_cr2[j],arr_lat[j],arr_long[j],arr_lat2[j],arr_long2[j],arr_timecat[j],arr_cat[j]])
            continue
        continue
    #print len(dict1)
    return dict1

def WriteIntoCsv(dict1):
    #Writing dictionary to csv file
    i=1
    print len(dict1.keys())
    for key,value in dict1.iteritems():
        #print value
        filename="file"+str(i)+".csv"
        with open(str(filename), 'wb') as fin:
            fieldnames = ['id', 'created','lat','long', 'lat2' , 'long2','timecat','cat']
            writer = csv.DictWriter(fin, fieldnames=fieldnames)
            writer.writeheader()
            for k in range(1,len(value)):
                writer.writerow({'id': key , 'created': value[k][0] , 'lat' : value[k][1] , 'long' : value[k][2] , 'lat2' : value[k][3] , 'long2' : value[k][4],'timecat' : value[k][5], 'cat' : value[k][6]})
            fin.close()
        i=i+1
        if i>328:
            break
        continue

    
def main():
    try:
        global arr_id,arr_cr,arr_geo,dict2,arr_filename,dict1,arr_cr2,arr_lat,arr_long,arr_lat2,arr_long2,arr_timecat,arr_cat
        dict1=collections.defaultdict(list)
        arr_id=[]
        arr_cr=[]
        arr_cr2=[]
        arr_timecat=[]
        arr_geo=[]
        arr_lat=[]
        arr_long=[]
        arr_lat2=[]
        arr_long2=[]
        arr_filename=[]
        arr_cat=[]
        dict2={}
        logging.basicConfig(filename='LOG_total.log', level=logging.DEBUG )
        arr_id,arr_cr,arr_geo=ReadFromCsv()
        arr_cr2,arr_lat,arr_long=CleanCrGeo(arr_id,arr_cr,arr_geo)
        arr_lat2,arr_long2=DDToDMS(arr_id,arr_lat,arr_long)
        arr_timecat=DivideTimeToCategory(arr_id,arr_cr2)
        arr_cat=DivideLatLongIntoCategory(arr_id,arr_lat2,arr_long2)
        dict1=ExtractUniqueId(arr_id,arr_cr2,arr_lat,arr_long,arr_lat2,arr_long2,arr_timecat,arr_cat)
        WriteIntoCsv(dict1)
        logging.info(arr_cat)
    except Exception,e:
        logging.error('An error has ocurred with description %s' ,e)
        sys.exit(1)
    print "end"

if __name__=="__main__":
    main()
