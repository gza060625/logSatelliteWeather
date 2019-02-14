import os
import sys
#import six.moves.urllib.request
import wget
import time
import datetime
import wget

#Constants:

#Strings

TITLE="Diffraction Ltd. Boltwood cloud sensor measurements"

LOCATION="LOCATION: Athabasca, Alberta, Canada"

MODEL="MODEL: Boltwood I"

#LATITUDE="LATITUDE(GEO): 54.7136"

#LONGITUDE="LONGITUDE(GEO): -113.3141"

YEAR="YEAR: "

MONTH="MONTH: "

DAY="DAY: "

COLUMN_NAME="hour,minute,second,sky condition, dome condition, Cumulus wx"



#Paths

HOME="./autumndp"
SUBDIR="SATWEATHER"
DEVICE_NAME=""
bufferName="bufferWeb.txt"



outputPath='/home/gza060625/Desktop/AU/logSatelliteWeather/SATWEATHER'
siteName="GOES"

inputURL="https://weather.gc.ca/data/satellite/goes_wcan_visible_100.jpg"


#Constant Data

timeInterval=2

configDictionary ={

  "AUGO": "54.7436",

  "AUGSO": "54.6028",

  "DEFAULT":"NULL"

}











#Variables



oYear,oDay,oMonth,ip,latitude,longitude=None,None,None,None,None,None







'''

Adding Star before print, then start a new line

If input is integer, then print stars accordingly.

'''

def addStar(inputValue):

    if type(inputValue) is str:

        return ("# "+inputValue+"\n")

    elif type(inputValue) is int:

        return "#"*inputValue+"\n"






'''

generate file name

'''

def createFileName():
    return UTimeStr()+".jpeg"





'''
Create a folder with <year, month, day>
return a path to the folder created
'''
def createFolder(year, month,day):
    
    year=str(year)
    month=str(month)
    day=str(day)
    path=os.path.join(outputPath,siteName,year,month,day)
    print(path)
    os.makedirs(path, exist_ok=True) 
    return path

'''
Return Current UT time as String
'''
def UTimeStr():
    now=datetime.datetime.now()
    return now.strftime("%m_%d_%Y-%H:%M:%S")
    

'''
Return Current UT time as yead,month,year
'''
def UTime():
    now=datetime.datetime.now()
    return now.year,now.month,now.day



def pullInfo(url):     
    try:        
        wget.download(url)
    except:
        print("Invalid URL: {}".format(url))

def getFileType(url): 
    return url.split(".")[-1]
    



def initialSetup():

    global SITE

    if len(sys.argv)>1 and sys.argv[1] in latDict:

        SITE=sys.argv[1]

        print("SITE: '{}'".format(SITE))

    else:

        if len(sys.argv)<=1:

            print("Please Provide SITE name.")

        else:

            print("'{}' is not listed\n Abort".format(sys.argv[1]))

        sys.stdout.flush()

        os._exit(0)



    global ip,longitude,latitude

    ip=ipDict[SITE]

    longitude=lonDict[SITE]

    latitude=latDict[SITE]    





if __name__=="__main__":
    #print(createFileName())
    #url="https://weather.gc.ca/data/satellite/goes_wcan_visible_10099.jpg"
    #print(getFileType(url))
    
    createFolder(*UTime())
    
    






