#Name: Feng, Ke
#DePaul ID: 1927931
#Date:03/04/2019
#HW2, Problem 2
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Import Libraries
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
import re
import ssl

#Allow universified SSL (SSL certificate)
ssl._create_default_https_context = ssl._create_unverified_context

#Define homepage and host
hostName = 'www.cdm.depaul.edu'
homeUrl = 'https://www.cdm.depaul.edu/Pages/default.aspx'

#Define a page number
visitLimit=22000

#Skipping non-textual html tags
skipHtmlTag = ['head', 'meta', 'script', 'style']

#Save scrawled page into a list
visitedUrls = []

#Save appeared words
collectWords={}

class WordCollector(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        # whether to skip current tag
        self.skipTag = 0
        
    def handle_data(self, data):
        if self.skipTag == 1:
            return
        if not data:
            return
        string = data.strip()
        if len(string) == 0:
            return
        # print(string)
        # expression
        finds = re.findall('[A-Za-z\']+(?:[\`|\’][A-Za-z]+)?', string)
        for find in finds:
            collectWords[find] = collectWords.get(find, 0) + 1

    def handle_starttag(self, tag, attrs):
        self.skipTag = 0
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    result = urlparse(absolute, allow_fragments=True)
                    # remove anchors
                    if len(result[5]) > 0:
                        absolute = absolute[:-(len(result[5]) + 1)]
                    #if its host name and http url, add to the list 
                    if result[1] == hostName and result[0] == 'https' and (not absolute.endswith('.pdf')):
                        if not (absolute in visitedUrls):
                            self.links.append(absolute)
        if tag in skipHtmlTag:
            self.skipTag = 1

    def handle_endtag(self, tag):
        self.skipTag = 0


def parseUrl(url):
    if len(visitedUrls) >= visitLimit:
        return
    try:
        print(url)
        visitedUrls.append(url)
        response = urlopen(url)
        html = response.read()
        html = html.decode()
        parser = WordCollector(url)
        parser.feed(html)
        for link in parser.links:
            if link in visitedUrls:
                continue
            else:
                parseUrl(link)
    except:
        pass

# get context 
parseUrl(homeUrl)

# sort word by value 
collectWords = sorted(collectWords.items(), key=lambda d: d[1], reverse=True)

# print(parser.words)
f = open('r.txt', 'w')
# print how many pages calcualted
print('\n' + 'Note: the scrawler will (1)Show page links we parsed (2)show 25 most commmon words and their counts'+'\n') 
print('Parse page count:' + str(len(visitedUrls)) + '\n')
print('The 25 most common words on the CDM website are:\n')
f.write('The 25 most common words on the CDM website are: \n')
# print first 25 words 
for w in collectWords[:25]:
    line = 'word:' + w[0] + '\t'+'count:' + str(w[1]) + '\n'
    print(line)
    f.write(line)

# write everything into a file 
f.write('\n\nAll parsed page: \n')
for page in visitedUrls:
    f.write(page + '\n')

f.close()
print('Detail result save in r.txt')

####25 Most Common Words 
##The 25 most common words on the CDM website are: 
##word:and	count:318717
##word:the	count:253462
##word:Strongly	count:215588
##word:disagree	count:195843
##word:agree	count:195843
##word:Admission	count:158536
##word:of	count:136600
##word:CDM	count:129164
##word:course	count:111486
##word:to	count:100152
##word:Resources	count:97489
##word:than	count:94933
##word:About	count:94588
##word:The	count:94250
##word:was	count:89010
##word:A	count:88138
##word:Agree	count:88049
##word:Neither	count:88049
##word:nor	count:88049
##word:Disagree	count:88049
##word:average	count:81289
##word:DePaul	count:78141
##word:Graduate	count:75084
##word:Programs	count:74777
##word:Academic	count:74333


