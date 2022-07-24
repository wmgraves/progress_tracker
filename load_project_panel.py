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
from project import Project

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
        self.list.InsertColumn(0, 'Project Title', width=300)
        self.list.InsertColumn(1, 'Last Modified On', width=125)
        self.list.InsertColumn(2, 'Progress', width=60)
        self.list.InsertColumn(3, '# Tasks', width=50)
        self.list.InsertColumn(4, '# Completed', width=85)
        self.list.InsertColumn(5, '# In Progress', width=85)
        self.list.InsertColumn(6, '# Overdue', width=70)
        self.list.InsertColumn(7, '# Available', width=75)
        self.list.InsertColumn(8, '# Not Ready', width=80)
        vbox.Add(self.list, 1, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Populate list
        self.files = list(filter(os.path.isfile, glob.glob("data/*.json")))
        self.files.sort(key=lambda x: os.path.getmtime(x)) # sort by last modified time

        for i in range(len(self.files)):
            # Get data
            fileNum = len(self.files) - i - 1
            file = open(self.files[fileNum], 'r')

            for junk in range(2):
                file.readline()
            title = file.readline()[18:-3]

            for junk in range(6):
                file.readline()
            numTasks = file.readline()[17:-2]
            numCompleted = file.readline()[26:-2]
            numInProgress = file.readline()[27:-2]
            numOverdue = file.readline()[24:-2]
            numAvailable = file.readline()[26:-2]
            numNotReady = file.readline()[25:-1]

            file.close()

            progress = "0.0%"
            if numTasks != "0":
                progress = str(round(100.0 * int(numCompleted) / int(numTasks), 1)) + '%'

            # Add data to list
            self.list.InsertItem(i, title)
            self.list.SetItem(i, 1, datetime.datetime.fromtimestamp(int(os.path.getmtime(self.files[fileNum])))
                              .strftime('%m/%d/%Y %I:%M %p'))
            self.list.SetItem(i, 2, progress)
            self.list.SetItem(i, 3, numTasks)
            self.list.SetItem(i, 4, numCompleted)
            self.list.SetItem(i, 5, numInProgress)
            self.list.SetItem(i, 6, numOverdue)
            self.list.SetItem(i, 7, numAvailable)
            self.list.SetItem(i, 8, numNotReady)

        self.list.Select(0)

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

        fileNum = len(self.files) - self.list.GetFirstSelected() - 1
        self.panelManager.projectData = Project(self.files[fileNum])

        # Display project data
        panelList = {
            'project_details_panel': {
                'className': 'ProjectDetailsPanel',
                'size': 1
            },
            'tasks_preview_panel': {
                'className': 'TasksPreviewPanel',
                'size': 2
            }
        }
        self.panelManager.showPanels(panelList)

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
