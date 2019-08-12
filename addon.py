import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
osWin = xbmc.getCondVisibility('system.platform.windows')
osOsx = xbmc.getCondVisibility('system.platform.osx')
osLinux = xbmc.getCondVisibility('system.platform.linux')
osAndroid = xbmc.getCondVisibility('System.Platform.Android')
url = addon.getSetting("url")

if osOsx:    
    # ___ Open the url with the default web browser
    xbmc.executebuiltin("System.Exec(open "+url+")")
elif osWin:
    # ___ Open the url with the default web browser
    xbmc.executebuiltin("System.Exec(cmd.exe /c start "+url+")")
elif osLinux and not osAndroid:
    # ___ Need the xdk-utils package
    xbmc.executebuiltin("System.Exec(xdg-open "+url+")") 
elif osAndroid:
    # ___ Open media with standard android web browser
    xbmc.executebuiltin("StartAndroidActivity(com.android.browser,android.intent.action.VIEW,,"+url+")")
    
    # ___ Open media with Mozilla Firefox
    xbmc.executebuiltin("StartAndroidActivity(org.mozilla.firefox,android.intent.action.VIEW,,"+url+")")                    
    
    # ___ Open media with Chrome
    xbmc.executebuiltin("StartAndroidActivity(com.android.chrome,,,"+url+")") 
