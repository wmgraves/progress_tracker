# progress_tracker - task_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/25/2022

# Description:
# TODO: add description of this file

# Import external modules
from datetime import datetime
import wx

# Import custom modules
import overview_frame

# Initialize variables
topPadding = 10
sidePadding = 5
vGap = 20
hGap = 10


class TaskFrame(wx.Frame):
    """
    Allows the user to enter information for creating a new project.
    """

    def __init__(self, parent, title, statusText, project, taskIndex):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(TaskFrame, self).__init__(parent, title=title, size=(800, 650))
        self.project = project
        self.taskIndex = taskIndex
        panel = wx.Panel(self)

        vboxLeft = wx.BoxSizer(wx.VERTICAL)
        # vboxLeft.AddSpacer(topPadding)

        # Add title
        self.titleLabel = wx.StaticText(panel, label='Title:')
        headingFont = self.titleLabel.GetFont()
        headingFont.PointSize = 13
        headingFont.Weight = wx.BOLD
        self.titleLabel.SetFont(headingFont)

        self.titleText = wx.TextCtrl(panel)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.titleLabel, 0)
        # hbox.AddSpacer(hGap)
        # hbox.Add(self.titleResetButton, 0)
        vboxLeft.Add(hbox, 0, wx.EXPAND)
        vboxLeft.Add(self.titleText, 0, wx.EXPAND)
        vboxLeft.AddSpacer(vGap)

        # Add description
        self.descriptionLabel = wx.StaticText(panel, label='Description:')
        self.descriptionLabel.SetFont(headingFont)

        self.descriptionText = wx.TextCtrl(panel, size=(-1, 150), style=wx.TE_MULTILINE)

        vboxLeft.Add(self.descriptionLabel, 0)
        vboxLeft.Add(self.descriptionText, 1, wx.EXPAND)
        # vboxLeft.AddSpacer(vGap)

        # Add prereq list
        self.prereqLabel = wx.StaticText(panel, label='Prerequisite Task Selections:')
        self.prereqLabel.SetFont(headingFont)

        # TODO: add logic for adding tasks to this list
        taskNames = []
        for i, taskData in project.data['tasks'].items():
            # Skip this task (a task cannot be a prerequisite to itself)
            if int(i) == taskIndex:
                continue

            # Format task label
            startText = ''
            if project.data['tasks'][i]['completed']:
                startText += '⬛'
            elif project.data['tasks'][i]['started']:
                startText += '◧'
            else:
                startText += '☐'
            startText += ' '
            taskNames.append(startText + project.data['tasks'][i]['title'])

        self.prereqList = wx.ListBox(panel, style=wx.LB_MULTIPLE, choices=taskNames)

        vboxRight = wx.BoxSizer(wx.VERTICAL)
        vboxRight.Add(self.prereqLabel, 0)
        vboxRight.Add(self.prereqList, 1, wx.EXPAND)

        # Create main BoxSizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vboxLeft, 1, wx.EXPAND)
        hbox.AddSpacer(hGap)
        hbox.Add(vboxRight, 1, wx.EXPAND)
        hbox.AddSpacer(sidePadding)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add buttons
        self.saveButton = wx.Button(panel, label='Save')
        bottomButtonFont = self.saveButton.GetFont()
        bottomButtonFont.PointSize = 15
        bottomButtonFont.Weight = wx.BOLD
        self.saveButton.SetFont(bottomButtonFont)
        self.saveButton.Bind(wx.EVT_BUTTON, self.onSaveClicked)

        self.deleteButton = wx.Button(panel, label='Delete')
        self.deleteButton.SetFont(bottomButtonFont)
        self.deleteButton.Bind(wx.EVT_BUTTON, self.onDeleteClicked)

        self.exitButton = wx.Button(panel, label='Cancel')
        self.exitButton.SetFont(bottomButtonFont)
        self.exitButton.Bind(wx.EVT_BUTTON, self.onExitClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.saveButton, 0)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.deleteButton, 0)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.exitButton, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.ALIGN_RIGHT)

        # Display frame
        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()

        # Fill fields with current values
        task = project.data['tasks'][str(taskIndex)]
        self.titleText.SetValue(task['title'])
        self.descriptionText.SetValue(task['description'])

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.statusText = statusText

    def onSaveClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Save button clicked')

        # Update task data
        task = self.project.data['tasks'][str(self.taskIndex)]
        task['title'] = self.titleText.GetValue()
        task['description'] = self.descriptionText.GetValue()
        # TODO: finish implementing this

        self.project.saveData()
        overview_frame.OverviewFrame(None, title='Progress Tracker', statusText=self.statusText,
                                     fileName=self.project.fileName)
        self.Close(True)

    def onDeleteClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Delete button clicked')

        # TODO: implement this

    def onExitClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Cancel button clicked')
        overview_frame.OverviewFrame(None, title='Progress Tracker', statusText=self.statusText,
                                     fileName=self.project.fileName)
        self.Close(True)
