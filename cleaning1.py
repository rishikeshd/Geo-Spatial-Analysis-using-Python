#############################
#Script to read JSON file extracted from Twitter API and to extract
#user id, created date of the tweet and geo coordinates of the tweet
#And writing this to csv file

import json,logging
import os,sys
import glob,re
import csv
import unicodedata
import string


def ReadJsonIntoDict():
    try:
        a=0
        var='var'+str(a)
        i='.json'
        regexstring='*'+ i
        filename=glob.glob(regexstring)
        for f in filename:
            with open(str(f), "r+") as in_file:
                print f
                for line in in_file:
                    x=json.loads(line)
                    array.update({str(var):x})
                    a=a+1
                    var='var'+str(a)
                    continue
            in_file.close()
            continue
        print len(array)
    except Exception,e:
        logging.error(e)
    return array

def ExtractJsonIntoDict(array):
    for p in range(0,len(array)):
        try:
            q='var'+str(p)
            #print str(q)
            #print q
            if 'geo' not in array[q] or array[q]['geo']==None or 'user' not in array[q]:
                #print "fail"
                array_userid.update({str(q):"0"})
                array_username.update({str(q):"0"})
                array_coord.update({ str(q):"0"})
                array_created_at.update({str(q):"0"})
            else:
                #print "1"
                array_userid.update({str(q):array[q]['user']['id']})
                array_username.update({str(q):array[q]['user']['name']})
                array_created_at.update({str(q):array[q]['created_at']})
                array_coord.update({str(q):array[q]['geo']['coordinates']})
        except KeyError,e:
            logging.error('An error has occured with desription %s' ,e)
        continue
    return array_userid,array_username,array_created_at,array_coord

def WriteIntoCsv():
    dicts=array_userid,array_created_at,array_coord
    with open('all_files.csv', 'wb') as in_file:
        writer = csv.writer(in_file, delimiter=',')
        writer.writerow(['Srno','Userid','created_at','Coord'])
        for key in array_userid.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])


def main():
    try:
        global array,array_userid,array_username,array_coord,array_created_at
        array={}
        array_userid={}
        array_username={}
        array_coord={}
        array_created_at={}
        logging.basicConfig(filename='LOG_total.log', level=logging.DEBUG )
        array=ReadJsonIntoDict()
        #print array['var61992']
        #print array['var61993']
        array_userid,array_username,array_created_at,array_coord=ExtractJsonIntoDict(array)
        logging.info("Lengths are %s,%s,%s,%s",len(array_userid),len(array_username),len(array_coord),len(array_created_at))
        WriteIntoCsv()
        print "end"
    except Exception,e:
        logging.error('An error has ocurred with description %s' ,e)
        sys.exit(1)

if __name__=="__main__":
    main()
        
        
