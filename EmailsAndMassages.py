__author__ = 'Soheil'

import re
import collections
with open("EmailBox201411.mbox" , "r") as my_text:
    text = my_text.read()
    domains = re.findall("\@[\w\.]+\.[c|o][o|r][m|g]", text)
    domainsNr = [(item, count) for item, count in collections.Counter(domains).items()]
    messages = text.split("From bookkeeper")
    #print domains
    msgTitle = re.findall("From [\w\.\-\=\ ]+\@[\w\.]+\.[c|o][o|r][m|g]  \w+", text)
    #recMsg = re.findall("Received: from ")
    #sentMsg = re.findall("Delivered-To: ")
    #print msgTitle
    #print len(msgTitle)
    #print len(messages)

    print"+----+-----Domain--------------------------------+--Msg-+-Percentage-+"
    """
    c = 1
    for i in domainsNr:
        print "%d | %s                             %d" %(c,i[0],i[1])
        c += 1
    domainCounter = 0
    """

    c ,domainCounter = 1, 0
    for domain in set(domains):
        for msg in messages:
            if domain in msg:
                domainCounter += 1
        print "%d | %s                             %d | %.2f" % (c, domain, domainCounter, 100 * float(domainCounter)/len(messages)) + "%"
        c += 1
        domainCounter = 0


        #recMsg = re.findall("Received: from ", )