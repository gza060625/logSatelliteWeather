#import urllib.request


#response = urllib.request.urlopen('http://www.example.com/')
#html = response.read()



import wget
url="https://weather.gc.ca/data/satellite/goes_wcan_visible_100.jpg"
wget.download(url)