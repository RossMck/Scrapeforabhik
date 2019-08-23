# Ross Mckechnie
# Website scraper

class Website:
    def __init__(self, url, regexin):
        import re
        self.url = url
        self.regexin = regexin
        import requests
        print("getting " + url)
        self.data = requests.get(url).content
        self.data = re.search(self.regexin, self.data, flags=re.DOTALL)
        print("got "+url)
    def output(self, theregex, fileoutname):
        import re
        print("sorting data with regex"+theregex)
        indicators = re.findall(theregex, self.data.group(1))
        print("found "+str(indicators.len()))
        print("data sorted")
        print("writing "+fileoutname)
        fileout = open(fileoutname, 'a')
        fileout.write('\n'.join(indicators))
        fileout.write('\n')
        fileout.close()
        print("wrote " + fileoutname)
import csv
old = "old"
with open('websitestoscrape') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter='&')
   for row in csv_reader:
       if(old != row[0]):
           scrapedwebsite = Website(row[0], row[1])
           old = row[0]
       scrapedwebsite.output(row[2], row[3])
   print('done')
