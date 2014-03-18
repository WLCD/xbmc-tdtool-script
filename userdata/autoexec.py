#based off work from eldo (xbmc forums)

import os, xbmc
#turn on device 1
os.system("tdtool -n 1")
xbmc.sleep(1000)

#call playback related script
xbmc.executescript('special://home/scripts/playeractions.py')
xbmc.sleep(1000)

#call idle script
xbmc.executescript('special://home/scripts/idletime.py')