#!/usr/bin/python3
import urllib.request
from datetime import date
from os import path
from os import system
import re
import json
import random

bgFinderPattern = re.compile("JSON\.parse\(\\\\'([^\)]+)\\\\'\)", re.IGNORECASE)


with urllib.request.urlopen('https://clients3.google.com/cast/chromecast/home/') as googleHangoutPage:
    match = bgFinderPattern.search(str(googleHangoutPage.read()))
    if match:
        ascii_json = match.group(1)
        ascii_json = eval("b\"%s\""% ascii_json).decode('utf-8')
        json_string = eval("b\"%s\""% ascii_json).decode('utf-8').replace('\\/', '/')
        json_value = json.loads(json_string)
        photo_url = random.choice(json_value[0])[0]
        print(photo_url)
        newBackgroundFile = path.expanduser('~') + '/Pictures/Google-Wallpapers/' + str(date.today()) + '.jpeg'
        result = urllib.request.urlretrieve(photo_url, newBackgroundFile)
        if result[0]:
            imagePath = path.abspath(newBackgroundFile)
            cmd = "gsettings set org.gnome.desktop.background picture-uri " + imagePath
            system(cmd)
    else:
        print("NO MATCH!!!")
