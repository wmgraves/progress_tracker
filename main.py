# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# Starts the app.

# Import external libraries
import wx

# Import custom modules
import start_frame

# Create and start app
app = wx.App()
start_frame.StartFrame(None, title='Progress Tracker')
app.MainLoop()
