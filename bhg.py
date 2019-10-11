#!/usr/bin/env python3
import argparse
import requests
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser(description='Check headers for target web site.')
parser.add_argument('-t','--target', dest='target', type=str, help='Target')
parser.add_argument('-i','--insecure', dest='verify', action="store_false", default=True, help='Make insecure requests')
parser.add_argument('-u','--username', dest='username', type=str, required=False, help='Username for HTTP Basic authentication')
parser.add_argument('-p','--password', dest='password', type=str, required=False, help='Password for HTTP Basic authentication')
parser.add_argument('-a','--user-agent', dest='agent', type=str, required=False, help='User Agent for request',default='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
args = parser.parse_args()

def CheckHeader(headers,search):
    if search.lower() in (h.lower() for h in headers):
        return search+": "+headers[search]
    return False

def RetrieveHeaders(target, verify, username, password, agent):
    headers = {'User-Agent': agent}
    print("Getting Headers for: "+args.target+"\n")
    if username and password:
        r = requests.get(target, auth=HTTPBasicAuth(username, password), allow_redirects=True, verify=verify, headers=headers)
    else:
        r = requests.get(target, verify=verify, allow_redirects=True, headers=headers)
    if not r.history:
        return r.headers
    for h in range(len(r.history)):
        if (target not in r.history[h].headers["Location"]) and (r.history[h].headers["Location"].startswith("/"))==False:
            print("\033[1m\033[31m[-] \033[0mNot following redirect to: "+r.history[h].headers["Location"])
            ret = r.history[h].headers
        else:
            print("\033[1m\033[32m[+] \033[0mFollowed redirect to: "+r.history[h].headers["Location"])
            ret = r.headers
    print("")
    return ret

searchlist = [\
'X-Frame-Options',\
'Content-Security-Policy',\
'Strict-Transport-Security',\
'X-Content-Type-Options',\
'X-XSS-Protection','Referrer-Policy'\
]
try:
    if args.username and args.password:
        headers = RetrieveHeaders(args.target, args.verify, args.username, args.password, args.agent)
    else:
        headers = RetrieveHeaders(args.target, args.verify, False, False, args.agent)
except Exception as e:
    print(e)
    exit()

for search in searchlist:
    c = CheckHeader(headers,search)
    if c:
        print("\033[1m\033[32m[+] \033[0m"+c.strip()+"\033[1m\033[32m (OK)")
    else:
        print("\033[1m\033[31m[-] \033[0m"+search+":\033[1m\033[31m (Missing)")

print("\n\033[0mDone.")
