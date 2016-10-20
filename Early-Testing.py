#!/usr/bin/env python

import requests, re

tokenRegex = "token=([a-zA-Z0-9]{32})"
deprecatedTokenRegex = r"name='token' value='([a-zA-Z0-9]{32})'"

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'kid' : "", 'login': "newspaperman57", 'pass': '21011996', 'uni' : 's134-en.ogame.gameforge.com'}

session = requests.Session()

overviewTab = session.post('https://en.ogame.gameforge.com:443/main/login',headers=headers,data=payload) #Login and get overview

resourcesTab = session.get("https://s134-en.ogame.gameforge.com/game/index.php", headers=headers, params={'page' : 'resources'}) #Get resources tab
# resourceToken = re.search(tokenRegex, resourcesTab.text).group(1) # Find token for building resources

#defenceTab = session.get("https://s134-en.ogame.gameforge.com/game/index.php", headers=headers, params={'page' : 'defense'}) #Get defence tab
print resourcesTab.text.encode('utf-8')

DeprecatedDefenceToken = re.search(deprecatedTokenRegex, resourcesTab.text).group(1) # Find deprecated token for building shipyard and defence 

payload = {'token' : DeprecatedDefenceToken, 'modus' : '1', 'type' : '401', 'menge' : '1'}
session.post('https://s134-en.ogame.gameforge.com/game/index.php?deprecated=1&page=defense', headers=headers,data=payload)

print "DeprecatedToken:", DeprecatedDefenceToken