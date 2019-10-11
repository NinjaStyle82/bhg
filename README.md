# BetterHeaderGetter
Get HTTP security headers and make them look good.

Usage example:
bhg.py -t gmail.com

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
                        User Agent for request
```
