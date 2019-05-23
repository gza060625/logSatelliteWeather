import os
import sys
import wget
import time
import datetime
import wget


'''
Test Command
python3 '/home/gza060625/Desktop/AU/logSatelliteWeather/SATWEATHER' "GOES" "https://weather.gc.ca/data/satellite/goes_wcan_visible_100.jpg"
'''



#Constant Data

configList=[('/home/gza060625/Desktop/AU/logSatelliteWeather/SATWEATHER',\
             "GOES",\
             
             
             
             
             "https://weather.gc.ca/data/satellite/goes_wcan_visible_100.jpg"\
            ),\
            ('/home/gza060625/Desktop/AU/logSatelliteWeather/SATWEATHER',\
             "AUGO",\
             "http://www.cleardarksky.com/c/AUGOABcsk.gif"\
            ),\
           ]



'''
generate file name
'''
def createFileName(url):
    return UTimeStr()+getFileType(url)


'''
Create a folder with <year, month, day>
return a path to the folder created
'''
def createFolder(outputPath,siteName,year, month,day):
    
    year=str(year)
    month=str(month)
    day=str(day)
    
    path=os.path.join(outputPath,siteName,year,month,day)
    #print(path)
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


def pullInfo(url,filePath):     
    try:        
        wget.download(url,filePath)
    except:
        print("Invalid URL: {}".format(url))

def getFileType(url): 
    return url.split(".")[-1]
    

def fetchFile(outputPath,siteName,url):
    folderPath=createFolder(outputPath,siteName,*UTime())
    fileName=createFileName(url)
    filePath=os.path.join(folderPath,fileName)    
    pullInfo(url,filePath)
    

def main():
    
    global configList
    
    if len(sys.argv)==1:
        for ele in configList:
            fetchFile(*ele)
        
    elif len(sys.argv)==4:
        fetchFile(*sys.argv[1:4])
    else:
        print("3 arguments required, {} provided.".format(len(sys.argv)-1))
        print(sys.argv)  
        os._exit(0)



if __name__=="__main__":
    main()

    
    






