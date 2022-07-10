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

        # Add progress bar text
        self.barLabel = wx.StaticText(self, label=stringsData['barLabel'])
        labelFont = self.barLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.barLabel.SetFont(labelFont)
        vbox.Add(self.barLabel)

        #TODO add counters for each type
        self.completedLabel = wx.StaticText(self, label=stringsData['barCompleted'] + ": 0")
        textFont = self.completedLabel.GetFont()
        textFont.PointSize = 13
        self.completedLabel.SetFont(textFont)
        vbox.Add(self.completedLabel, 0, wx.EXPAND)

        self.inProgressLabel = wx.StaticText(self, label=stringsData['barInProgress'] + ": 0")
        self.inProgressLabel.SetFont(textFont)
        vbox.Add(self.inProgressLabel, 0, wx.EXPAND)

        self.overdueLabel = wx.StaticText(self, label=stringsData['barOverdue'] + ": 0")
        self.overdueLabel.SetFont(textFont)
        vbox.Add(self.overdueLabel, 0, wx.EXPAND)

        self.availableLabel = wx.StaticText(self, label=stringsData['barAvailable'] + ": 0")
        self.availableLabel.SetFont(textFont)
        vbox.Add(self.availableLabel, 0, wx.EXPAND)

        self.notReadyLabel = wx.StaticText(self, label=stringsData['barNotReady'] + ": 0")
        self.notReadyLabel.SetFont(textFont)
        vbox.Add(self.notReadyLabel, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add progress bar
        self.barCompleted = wx.Panel(self, size=(-1, 25))
        self.barCompleted.SetBackgroundColour(wx.Colour(int(stringsData['colorCompleted'])))

        self.barInProgress = wx.Panel(self)
        self.barInProgress.SetBackgroundColour(wx.Colour(int(stringsData['colorInProgress'])))

        self.barOverdue = wx.Panel(self)
        self.barOverdue.SetBackgroundColour(wx.Colour(int(stringsData['colorOverdue'])))

        self.barAvailable = wx.Panel(self)
        self.barAvailable.SetBackgroundColour(wx.Colour(int(stringsData['colorAvailable'])))

        self.barNotReady = wx.Panel(self)
        self.barNotReady.SetBackgroundColour(wx.Colour(int(stringsData['colorNotReady'])))

        #TODO add correct size calculation stuff (just set integer to counts)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.barCompleted, 1, wx.EXPAND)
        hbox.Add(self.barInProgress, 2, wx.EXPAND)
        hbox.Add(self.barOverdue, 3, wx.EXPAND)
        hbox.Add(self.barAvailable, 4, wx.EXPAND)
        hbox.Add(self.barNotReady, 5, wx.EXPAND)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add task list
        self.listLabel = wx.StaticText(self, label=stringsData['listLabel'])
        self.listLabel.SetFont(labelFont)
        vbox.Add(self.listLabel)

        self.list = wx.ListCtrl(self, style=wx.LC_REPORT, size=(-1, 360))
        self.list.InsertColumn(0, 'Title', width=300)
        self.list.InsertColumn(1, 'Status', width=100)
        self.list.InsertColumn(2, '???', width=100)
        vbox.Add(self.list, 1, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Populate list
        for i in range(10):
            self.list.InsertItem(i, "Project Title " + str(i))
            self.list.SetItem(i, 1, 'In Progress')
            self.list.SetItem(i, 2, 'Figure out what else should be shown here')

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)