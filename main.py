# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# Starts the app.

# Import external modules
from pathlib import Path
import wx

# Import custom modules
from panel_manager import PanelManager

# Create a data directory if it does not already exist
Path('data').mkdir(parents=True, exist_ok=True)

# Create and start the app
app = wx.App(False)
frame = PanelManager(None)
frame.Maximize()
frame.Show()
app.MainLoop()
