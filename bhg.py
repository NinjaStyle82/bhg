#!/usr/bin/env python3

import argparse
import urllib3
import requests

searchlist = [\
'X-Frame-Options',\
'Content-Security-Policy',\
'Strict-Transport-Security',\
'X-Content-Type-Options',\
'X-XSS-Protection','Referrer-Policy'\
]

def CheckHeader(headers,search):
    if search.lower() in (h.lower() for h in headers):
        return search+": "+headers[search]
    return False

def RetrieveHeaders(target):
	urllib3.disable_warnings()
	requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
	try:
    		requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
	except AttributeError:
    		# no pyopenssl support used / needed / available
    		pass
	headers = requests.get(target, verify=False).headers
	return headers

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Check headers for target web site.')
	parser.add_argument('-t','--target',dest='target',type=str,help='target', required=True)
	args = parser.parse_args()

	try:
		print("Getting Headers for: "+args.target+"\n")
		headers = RetrieveHeaders(args.target)
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

