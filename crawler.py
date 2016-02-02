import sys, urllib, urllib2, cookielib, unirest
#Get Glassdoor companyId by company name
criteria = 'Google'
companyId = 0
urlSurfix = '&userip=128.42.86.120&useragent=Chrome/47.0.2526.106'
companyInfo = unirest.get('http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=52727&t.k=b3Xn1dQJDme&action=employers&q='
                          +criteria
                          + urlSurfix)
response = companyInfo.body['response']
#response includes: stats, total number of pages, attributionURL first 10 search results; we may want total no. of reviews on a specific company
#Future optimization: user enter a company name, we do the search
for company in response['employers']: #each company name
    if company['name'] == criteria:
        companyId = company['id']

storageStrPros = ""; #store "Pros" section of all reviews
storageStrCons = ""; #store "Cons" section of all reviews

#Hack regular expression of URLs for reviews
# First page: https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm
# Second page and on: https://www.glassdoor.com/Reviews/Target-Reviews-E194_P5.htm?filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME&filter.employmentStatus=UNKNOWN

urlPrefix = 'https://www.glassdoor.com/Reviews/'
urlMiddle =  '-Reviews-E'
urlSurfix = '?filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME&filter.employmentStatus=UNKNOWN'
url = urlPrefix + criteria + urlMiddle + str(companyId) + '.htm'

def makeUrl(_criteria, _companId, _pageNumber):
    global urlPrefix;
    global urlMiddle;
    global urlSurfix;
    return urlPrefix + _criteria + urlMiddle + _companId + "_P" + _pageNumber + '.htm' + urlSurfix;


def extractReviews(_url, _searchMarker, _firstEntryNum, flag):
    newStart= 0
    global storageStrPros;
    global storageStrCons;

    if url is not None:
        content = urllib2.urlopen(_url)
        page1 = content.read()
        #print "full content: " + page1
        page2 = content.read()
        tt=open('temp.txt','w')
        tt.write(page1)
        while (page1.find(_searchMarker)>=0):
            #print "1 " + str(page1.find(target))
            newStart = page1.find(_searchMarker) + len(_searchMarker)
            #print "2 " + str(len(page1))
            page1 = page1[newStart:] #found out because the next string was too short?
            #print "3 " + str(len(page1))
            review = page1[: page1.find('</div>')]
            page1 = page1[page1.find('</div>') : ]
            if (flag == "positive"):
                storageStrPros = storageStrPros + "review" + str(_firstEntryNum) + ": "+ review + "\n";
            else:
                storageStrCons = storageStrCons + "review" + str(_firstEntryNum) + ": "+ review + "\n";
            # print "printing pros: " + storageStrPros;
            # print "printing cons: " + storageStrCons;

            #print "4 " + str(len(page1))
            #print _firstEntryNum
            _firstEntryNum += 1;


#read the first URL
responseHtml = urllib2.Request(url, headers={'User-Agent' : "Chrome/47.0.2526.106"})
# had 403 forbidden problem initially because I didn't include proper header
# always Google with the error message first before guessing the reason of the error & google for that solution
#'cause my guess could be wrong!

#if not null, parse the HTML for 'pros' & 'cons'; if true, return
#read the next URL, repeat
pageNumber = 0;
startEntryNumPros = 1;
startEntryNumCons = 1;
count=0
targetPros = "pros noMargVert notranslate truncateThis wrapToggleStr'>";
targetCons = "cons noMargVert notranslate truncateThis wrapToggleStr'>";

storefilePros = open("pros_trial.txt", 'w');
storefileCons = open("cons_trial.txt", 'w');

#Future fix: doesn't stop at the last page because Glassdoor returns an error message page when there is no more result
#so responseHtml will never be None!
while (responseHtml is not None):
    extractReviews(responseHtml, targetPros, startEntryNumPros + count, "positive");
    extractReviews(responseHtml, targetCons, startEntryNumCons + count, "");
    count += 9; #Future: think about a proper increment function
    # print ("count=",count,storageStrPros)
    storefilePros.write(storageStrPros);
    storefileCons.write(storageStrCons);
    storageStrPros = "";
    storageStrCons = "";
    print "\r";
    print count;
    pageNumber += 1; # Should use "click the nextPage button" technique. Loading speed is the same. Look it up!!!
    #Read: http://docs.python-guide.org/en/latest/scenarios/scrape/
    #Google scraper: https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en
    url = makeUrl(criteria, str(companyId), str(pageNumber));
    responseHtml = urllib2.Request(url, headers={'User-Agent' : "Chrome/47.0.2526.106"})

print startEntryNumPros
print startEntryNumCons
storefilePros.close();
storefileCons.close();

#Signifies the program has finished correctly
print 'end'


