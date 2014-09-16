#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RAHULPANT
#
# Created:     12-09-2014
# Copyright:   (c) RAHULPANT 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
import json
url="http://www.youtube.com/watch?v=9Xt2e9x4xwQ"
req=urllib2.Request(url)
opener=urllib2.build_opener()
f=opener.open(req)
json=json.load(f)
for item in json:
        print item.get('created_at')
        print item.get('text')

