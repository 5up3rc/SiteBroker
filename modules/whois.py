"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def whoIS(website):
	website = "http://api.whoapi.com/?apikey=66ca3039356c0287ff63ed472f528478&r=whois&domain={url}&ip=".format(url=website)
	req = Request(website, _timeout=8, _encode=True)
	js = json.loads(req)
	whois = js['whois_raw']
	for result in whois.split("\n"):
		if len(result) != 0:
			write(var="~", color=c, data=result)