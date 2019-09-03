import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

osWin = xbmc.getCondVisibility('system.platform.windows')
osOsx = xbmc.getCondVisibility('system.platform.osx')
osLinux = xbmc.getCondVisibility('system.platform.linux')
osAndroid = xbmc.getCondVisibility('System.Platform.Android')


def openbrowser(url):
    if osOsx:
        # ___ Open the url with the default web browser
        xbmc.executebuiltin("System.Exec(open "+urlConfig+")")
    elif osWin:
        # ___ Open the url with the default web browser
        xbmc.executebuiltin("System.Exec(cmd.exe /c start "+urlConfig+")")
    elif osLinux and not osAndroid:
        # ___ Need the xdk-utils package
        xbmc.executebuiltin("System.Exec(xdg-open "+urlConfig+")")
    elif osAndroid:
        # ___ Open media with configured web browser in addon settings
        xbmc.executebuiltin("StartAndroidActivity("+browserApp+",android.intent.action.VIEW,,"+urlConfig+")")
        

#Config Variables
urlConfig = addon.getSetting("url")
browserApp = addon.getSetting("app")

#Check if urlConfig is set
if urlConfig == "https://":
    xbmcaddon.Addon().openSettings()

#Start processing
#Check if configured url returns a redirect
import requests
response_text = requests.get(urlConfig).text
import re
urls = re.findall(r"URL=(.*)'>", response_text)
if not urls:
    openbrowser(urlConfig)
else:
    #In case returns a redirect
    url = urls[0]
    #Search for Youtube ID
    regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
    match_youtube_id = regex.match(url)
    if not match_youtube_id:
        openbrowser(url)
    else:
        youtube_id = match_youtube_id.group('id')
        xbmc.Player().play("plugin://plugin.video.youtube/play/?video_id="+youtube_id)




        
