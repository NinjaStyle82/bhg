#!/usr/bin/env python2
import argparse
import requests

parser = argparse.ArgumentParser(description='Check headers for target web site.')
parser.add_argument('-t','--target',dest='target',type=str,help='target')
args = parser.parse_args()

def CheckHeader(headers,search):
    if search.lower() in (h.lower() for h in headers):
        return search+": "+headers[search]
    return False

def RetrieveHeaders(target):
    headers = requests.get(target).headers
    return headers
    
searchlist = [\
'X-Frame-Options',\
'Content-Security-Policy',\
'Strict-Transport-Security',\
'X-Content-Type-Options',\
'X-XSS-Protection','Referrer-Policy',\
'Public-Key-Pins'
]
try:
    headers = RetrieveHeaders(args.target)
    print "Getting Headers for: "+args.target+"\n"
except Exception as e:
    print e
    exit()

for search in searchlist:
    c = CheckHeader(headers,search)
    if c:
        print "\033[1m\033[32m[+] \033[0m"+c.strip()+"\033[1m\033[32m (OK)"
    else:
        print "\033[1m\033[31m[-] \033[0m"+search+":\033[1m\033[31m (NOT OK)"

print "\n\033[0mDone."
