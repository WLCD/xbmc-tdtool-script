#based off work from eldo (xbmc forums)

import xbmc,xbmcgui
import subprocess,os

#control over player features    
class MyPlayer(xbmc.Player) :

        def __init__ (self):
            xbmc.Player.__init__(self)

        def onPlayBackStarted(self):
            if xbmc.Player().isPlayingVideo():
                #here you can input any command that tdtool would take like "tdtool -v 0 -d 1" to put a dimmable switch to off state
				os.system("tdtool -f 1")

        def onPlayBackEnded(self):
            if (VIDEO == 1):
                os.system("tdtool -n 1")

        def onPlayBackStopped(self):
            if (VIDEO == 1):
                os.system("tdtool -n 1")

        def onPlayBackPaused(self):
            if xbmc.Player().isPlayingVideo():
                os.system("tdtool -n 1")

        def onPlayBackResumed(self):
            if xbmc.Player().isPlayingVideo():
                os.system("tdtool -f 1")

player=MyPlayer()

VIDEO = 0

while(1):
    if xbmc.Player().isPlaying():
      if xbmc.Player().isPlayingVideo():
        VIDEO = 1

      else:
        VIDEO = 0

    xbmc.sleep(1000)