#!/usr/bin/python3
import urllib.request
from datetime import date
from os import path
from os import system
import re

bgFinderPattern = re.compile('src=\"([^\"]+gstatic.com/chat/hangouts/bg/[^\"]+(.jpg|.png|.jpeg))\"', re.IGNORECASE)
with urllib.request.urlopen('https://hangouts.google.com/') as googleHangoutPage:
    match = bgFinderPattern.search(str(googleHangoutPage.read()))
    if match:
        print(match.group(1))
        newBackgroundFile = path.expanduser('~') + '/Pictures/Google-Wallpapers/' + str(date.today()) + match.group(2)
        result = urllib.request.urlretrieve(match.group(1), newBackgroundFile)
        if result[0]:
            imagePath = path.abspath(newBackgroundFile)
            cmd = "gsettings set org.gnome.desktop.background picture-uri " + imagePath
            system(cmd)
    else:
        print("NO MATCH!!!")
