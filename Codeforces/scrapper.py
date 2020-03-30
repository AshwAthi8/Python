from bs4 import BeautifulSoup
import requests
import json

url = 'https://my.monsterindia.com/find-companies.html?l=A'
response = requests.get(url, timeout=15)
content = BeautifulSoup(response.content)
# print("bhanu1")
#print(content)
tweetArr = []
i = 0
for tweet in content.findAll('div', attrs = {"class":"col-xs-8"}):
  # print("bhanu")
  tweetObject = {
        "Name": tweet.find("span", attrs = {"class":"cmpname"}),
        "Jobs": tweet.find("a", attrs = {"class":"mn-lnk1"})
    }
  tweetArr.append(str(tweetObject))
  urlArr = []
print(tweetArr)

  for a in range(0,len(tweetArr)):
    if(a == i):
      i1 = tweetArr[a].index('href')
      i2 = tweetArr[a].index('target')
      link = tweetArr[a]
      m = link[i1+6:i2-2]
      m = 'https:' + m
      print(m)
      urlArr.append(m)
  i = i + 1

'''
linkresp = requests.get(xurl,timeout=30)
linkcont = BeautifulSoup(response.content)
# for x in linkcont.findAll()
# print(linkcont)
arr = []
for x in linkcont.findAll('div', attrs = {"class":"job-wrap"}):
  xObject = {
    "Job Desc": x.find('a', attrs = {"class":"title_in"}),
    "Keyskills and Summary": x.findAll('div', attrs = {"class":"jtxt"}),
    "Location": x.find('div', attrs = {"class":"jtxt jico ico1"}),
    "Exp": x.find('div', attrs = {"class":"jtxt jico ico2"})
  }
  arr.append(str(xObject))
print(arr)
'''