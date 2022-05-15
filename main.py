# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# TODO: add description of this file

# Import external libraries
import wx

# Import custom modules
from start_frame import *
from create_frame import *

# Create and start app
app = wx.App()
StartFrame(None, title='Progress Tracker')
app.MainLoop()
