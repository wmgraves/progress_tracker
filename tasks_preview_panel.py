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
        project = self.panelManager.projectData

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
        self.completedLabel = wx.StaticText(self, label=stringsData['barCompleted'] + ": " + str(project.countCompleted))
        textFont = self.completedLabel.GetFont()
        textFont.PointSize = 13
        self.completedLabel.SetFont(textFont)
        vbox.Add(self.completedLabel, 0, wx.EXPAND)

        self.inProgressLabel = wx.StaticText(self, label=stringsData['barInProgress'] + ": " + str(project.countInProgress))
        self.inProgressLabel.SetFont(textFont)
        vbox.Add(self.inProgressLabel, 0, wx.EXPAND)

        self.overdueLabel = wx.StaticText(self, label=stringsData['barOverdue'] + ": " + str(project.countOverdue))
        self.overdueLabel.SetFont(textFont)
        vbox.Add(self.overdueLabel, 0, wx.EXPAND)

        self.availableLabel = wx.StaticText(self, label=stringsData['barAvailable'] + ": " + str(project.countAvailable))
        self.availableLabel.SetFont(textFont)
        vbox.Add(self.availableLabel, 0, wx.EXPAND)

        self.notReadyLabel = wx.StaticText(self, label=stringsData['barNotReady'] + ": " + str(project.countNotReady))
        self.notReadyLabel.SetFont(textFont)
        vbox.Add(self.notReadyLabel, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add progress bar
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        if project.countCompleted > 0:
            self.barCompleted = wx.Panel(self, size=(-1, 25))
            self.barCompleted.SetBackgroundColour(wx.Colour(int(stringsData['colorCompleted'])))
            hbox.Add(self.barCompleted, project.countCompleted, wx.EXPAND)

        if project.countInProgress > 0:
            self.barInProgress = wx.Panel(self, size=(-1, 25))
            self.barInProgress.SetBackgroundColour(wx.Colour(int(stringsData['colorInProgress'])))
            hbox.Add(self.barInProgress, project.countInProgress, wx.EXPAND)

        if project.countOverdue > 0:
            self.barOverdue = wx.Panel(self, size=(-1, 25))
            self.barOverdue.SetBackgroundColour(wx.Colour(int(stringsData['colorOverdue'])))
            hbox.Add(self.barOverdue, project.countOverdue, wx.EXPAND)

        if project.countAvailable > 0:
            self.barAvailable = wx.Panel(self, size=(-1, 25))
            self.barAvailable.SetBackgroundColour(wx.Colour(int(stringsData['colorAvailable'])))
            hbox.Add(self.barAvailable, project.countAvailable, wx.EXPAND)

        if project.countNotReady > 0 or project.count == 0:
            self.barNotReady = wx.Panel(self, size=(-1, 25))
            self.barNotReady.SetBackgroundColour(wx.Colour(int(stringsData['colorNotReady'])))
            hbox.Add(self.barNotReady, project.countNotReady, wx.EXPAND)

        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add task list
        self.listLabel = wx.StaticText(self, label=stringsData['listLabel'])
        self.listLabel.SetFont(labelFont)
        vbox.Add(self.listLabel)

        self.list = wx.ListCtrl(self, style=wx.LC_REPORT, size=(-1, 303))
        self.list.InsertColumn(0, 'Title', width=400)
        self.list.InsertColumn(1, 'Status', width=80)
        self.list.InsertColumn(2, 'Due Date', width=75)
        vbox.Add(self.list, 1, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Populate list
        for i in range(len(project.tasks)):
            task = project.tasks[i]
            self.list.InsertItem(i, task.title)
            self.list.SetItem(i, 1, task.getStatus())
            self.list.SetItem(i, 2, '00/00/0000')

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)