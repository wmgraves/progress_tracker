# progress_tracker - tasks_preview_panel.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/04/2022

# Description:
# TODO: add description of this file

# Import external modules
import wx

# Import custom modules
# TODO: imports

# Initialize variables
topPadding = 20
sidePadding = 5
vGap = 20
hGap = 10


class TasksPreviewPanel(wx.Panel):
    """
    text
    """

    def __init__(self, parent, stringsData):
        """
        text

        :param parent:
        :param stringsData:
        """

        self.panelManager = parent

        # Create panel
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        #TODO
        temp = wx.StaticText(self, label="Add UI elements to this")
        vbox.Add(temp)

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)