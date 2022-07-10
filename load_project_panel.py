# progress_tracker - load_project_panel.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/03/2022

# Description:
# TODO: add description of this file

# Import external modules
import datetime
import glob
import os
import wx

# Import custom modules
# TODO: imports

# Initialize variables
topPadding = 20
sidePadding = 5
vGap = 20
hGap = 10


class LoadProjectPanel(wx.Panel):
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

        # Add list label
        self.listLabel = wx.StaticText(self, label=stringsData['listLabel'])
        labelFont = self.listLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.listLabel.SetFont(labelFont)
        vbox.Add(self.listLabel)

        # Add list
        self.list = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'Data File Name', width=135)
        self.list.InsertColumn(1, 'Last Modified On', width=125)
        self.list.InsertColumn(2, 'Progress', width=60)
        vbox.Add(self.list, 1, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Populate list
        files = list(filter(os.path.isfile, glob.glob("data/*.json")))
        files.sort(key=lambda x: os.path.getmtime(x)) # sort by last modified time

        for i in range(len(files)):
            fileNum = len(files) - i - 1
            self.list.InsertItem(i, files[fileNum][5:-5])
            self.list.SetItem(i, 1, datetime.datetime.fromtimestamp(int(os.path.getmtime(files[fileNum]))).strftime(
                '%m/%d/%Y %H:%M %p'))
            self.list.SetItem(i, 2, '???')

        # Add buttons
        self.loadButton = wx.Button(self, label=stringsData['loadButton'])
        self.loadButton.SetFont(labelFont)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadClicked)

        self.cancelButton = wx.Button(self, label=stringsData['cancelButton'])
        self.cancelButton.SetFont(labelFont)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.onCancelClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.loadButton, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.cancelButton, 0)
        vbox.Add(hbox, 0, wx.ALIGN_RIGHT)
        vbox.AddSpacer(topPadding)

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1, wx.EXPAND)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)

    def onLoadClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print('onLoadClicked')
        #TODO implement this

    def onCancelClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        # Show the new panel
        panelList = {
            'main_menu_panel': {
                'className': 'MainMenuPanel',
                'size': 1
            }
        }
        self.panelManager.showPanels(panelList)
