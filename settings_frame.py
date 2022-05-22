# progress_tracker - settings_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# Handles modifying general app settings.

# Import external modules
import wx

# Import custom modules
import start_frame

# Initialize variables
topPadding = 10
sidePadding = 5
vGap = 20
hGap = 10


class SettingsFrame(wx.Frame):
    """
    Allows the user to modify general settings for the app.
    """

    def __init__(self, parent, title, statusText):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(SettingsFrame, self).__init__(parent, title=title, size=(550, 650))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # TODO: add stuff here

        # Display frame
        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.statusText = statusText
