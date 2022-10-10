#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re

#hämta url och decode i utf-8

with urllib.request.urlopen('https://php-web.edu.liu.se/nadla777/TDP001/') as response:
   html = response.read().decode("utf-8")


#hitta alla tags som passar regex 
#Regex [^/!] börja från första tecken tills slut  #\S* för att hämta allt inne i 3438<> eller fran < till slut av första tag.

match = re.findall("(<[^/!]\S*>|<[^/!]\S*)", html)

#fixa taggar sasom <a ....

for i, tag in enumerate(match):
    if not tag.endswith(">"):
        match[i] = tag + ">"

#count och utskrift av taggar

for tag in match:
    tag_count = match.count(tag)
    print(str(tag_count) + " " + tag)
    if tag_count > 1:
        for i in range(0, tag_count):
            match.remove(tag) #
