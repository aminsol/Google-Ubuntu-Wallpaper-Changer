#!/usr/bin/python3
import urllib.request
from datetime import date
from os import path
from os import system
import re
import json
import random

if __name__ == '__main__':
    bgFinderPattern = re.compile("JSON\.parse\(\\\\'([^\)]+)\\\\'\)", re.IGNORECASE)
    with urllib.request.urlopen('https://clients3.google.com/cast/chromecast/home/') as googleHangoutPage:
        match = bgFinderPattern.search(str(googleHangoutPage.read()))
        if match:
            byte_json = match.group(1).replace('\\\\', '\\')
            ascii_json = eval("b\"%s\"" % byte_json).decode('utf-8')
            json_string = ascii_json.replace('\\/', '/').replace('\\n', '')
            json_value = json.loads(json_string)
            photo_url = random.choice(json_value[0])[0]
            photo_url = photo_url.replace('1920', '2160')
            print(photo_url)
            newBackgroundFile = path.expanduser('~') + '/Pictures/Google-Wallpapers/' + str(date.today()) + '.jpeg'
            result = urllib.request.urlretrieve(photo_url, newBackgroundFile)
            if result[0]:
                imagePath = path.abspath(newBackgroundFile)
                cmd = "gsettings set org.gnome.desktop.background picture-uri " + imagePath
                system(cmd)
        else:
            print("NO MATCH!!!")
