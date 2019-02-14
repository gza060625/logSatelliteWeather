import os

import sys

import six.moves.urllib.request

import time



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





DEVICE_NAME="CLOUDSENSOR"

#Paths

HOME="./autumndp"

SUBDIR="/cloudsensor"

bufferName="bufferWeb.txt"





#Constant Data

timeInterval=2

latDict ={

  "AUGO": "54.7436",

  "AUGSO": "54.6028",

  "DEFAULT":"NULL"

}



lonDict ={

  "AUGO": "-113.3141",

  "AUGSO": "-113.6442",

  "DEFAULT":"NULL"

}



ipDict ={

  "AUGO": "http://131.232.13.37:27510/",

  "AUGSO": "http://131.232.13.120:27510/",

  "DEFAULT":"http://131.232.13.37:27510/"

}





#Variables

SITE=None

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

Create file Title information

'''

def createTitle(fileName,openMode,year,month,day):
    

    file = open(fileName, openMode)

    lengthDivider=75

    file.write(addStar(lengthDivider))

    file.write(addStar(TITLE))

    file.write(addStar("SITE: "+SITE))

    file.write(addStar(LOCATION))

    file.write(addStar(MODEL))

    file.write(addStar("LATITUDE(GEO): "+latitude))

    file.write(addStar("LONGITUDE(GEO): "+longitude))





    file.write(addStar(YEAR+year))

    file.write(addStar(MONTH+month))

    file.write(addStar(DAY+day))

    file.write(addStar(1))

    file.write(addStar(COLUMN_NAME))

    file.write(addStar(lengthDivider))    

    

    return file





'''

generate file name

'''

def createFileName(year,month,day):

    return ".".join([DEVICE_NAME,SITE,year,month,day,"txt"])





'''

Check if a file exist, if not create one

then write title info.

'''

def createFile(year, month,day):


    path=os.path.join(HOME,DEVICE_NAME,SITE,year,month,day)

    os.makedirs(path, exist_ok=True)    



    fileName=createFileName(year,month,day)

    path=os.path.join(path,fileName)

    

    if os.path.isfile(path):

        print("File {} exists".format(fileName))

        file=open(path,'a')

    else:

        print("Create File {}".format(fileName))

        file=createTitle(path,"w",year,month,day)

    return file

    





def pullInfo():    

    contents = six.moves.urllib.request.urlopen(ip).read().decode(encoding="utf-8")

    contents=contents.replace("\n",",")

    contents=contents.split(",")

    _,year,month,day,hour,minute,second,_,DOMECondition,_,skyCondition=contents[:11]

    if len(contents)>12:

        cumulus=contents[12]

    else:

        cumulus="Null"

    return year,month,day,hour,minute,second,DOMECondition,skyCondition,cumulus

       



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







def logging(): 

    global oYear,oMonth,oDay

    global file   

    

    while True:  

        

        year,month,day,hour,minute,second,DOMECondition,skyCondition,cumulus=pullInfo()

        

        if not (year==oYear and month==oMonth and day==oDay):

            oYear,oMonth,oDay=year,month,day

            file=createFile(oYear,oMonth,oDay)



        

        entry=",".join([hour,minute,second,skyCondition,DOMECondition,cumulus])+"\n"

        file.write(entry)

        file.flush()

        #print(entry,end="")

        oYear,oMonth,oDay=year,month,day

        

        time.sleep(timeInterval)  



if __name__=="__main__":

    

    initialSetup()

    logging()





