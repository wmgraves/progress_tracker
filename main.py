# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# Starts the app.

# Import external modules
import json
import os
import wx

# Import custom modules
from start_frame import StartFrame

# Create a config file if it does not already exist
filePath = 'data/settings.json'
if not (os.path.isfile(filePath) and os.access(filePath, os.R_OK)):
    print(filePath + ' does not exist, creating file now...')

    defaultData = {
        'projects': {}
    }

    with open(filePath, 'w') as settingsFile:
        settingsFile.write(json.dumps(defaultData, indent=4))
    settingsFile.close()

# Create and start the app
app = wx.App()
StartFrame(None, title='Progress Tracker', statusText='This app is still in development. Visit '
                                                      'https://github.com/wmgraves/progress_tracker for more '
                                                      'information')
app.MainLoop()
