# BetterHeaderGetter
Get HTTP security headers and make them look good.

Usage
```
usage: bhg.py [-h] [-t TARGET] [-i] [-u USERNAME] [-p PASSWORD] [-a AGENT]

Check headers for target web site.

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target
  -i, --insecure        Make insecure requests
  -u USERNAME, --username USERNAME
                        Username for HTTP Basic authentication
  -p PASSWORD, --password PASSWORD
                        Password for HTTP Basic authentication
  -a AGENT, --user-agent AGENT
                        User Agent for request (Default: Mozilla/5.0 (Windows
                        NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
                        Gecko) Chrome/72.0.3626.121 Safari/537.36)
```

Output Example
```
$ python bhg.py -t https://www.gmail.com
Getting Headers for: https://www.gmail.com

[-] Not following redirect to: https://www.google.com/gmail/
[-] Not following redirect to: https://mail.google.com/mail/
[-] Not following redirect to: https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#

[+] X-Frame-Options: SAMEORIGIN (OK)
[-] Content-Security-Policy: (Missing)
[-] Strict-Transport-Security: (Missing)
[+] X-Content-Type-Options: nosniff (OK)
[+] X-XSS-Protection: 1; mode=block (OK)
[-] Referrer-Policy: (Missing)

Done.
```
