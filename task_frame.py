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
        super(TaskFrame, self).__init__(parent, title=title, size=(800, 480))
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
        vboxLeft.AddSpacer(vGap)

        # Add status checkboxes
        self.checkBoxLabel = wx.StaticText(panel, label='Task Status:')
        self.checkBoxLabel.SetFont(headingFont)

        self.checkBoxStarted = wx.CheckBox(panel, label='In-Progress')
        checkBoxFont = self.checkBoxStarted.GetFont()
        checkBoxFont.PointSize = 12
        # checkBoxFont.Weight = wx.BOLD
        self.checkBoxStarted.SetFont(checkBoxFont)
        self.checkBoxStarted.Bind(wx.EVT_CHECKBOX, self.onStartedChecked)

        self.checkBoxCompleted = wx.CheckBox(panel, label='Completed')
        self.checkBoxCompleted.SetFont(checkBoxFont)
        self.checkBoxCompleted.Bind(wx.EVT_CHECKBOX, self.onCompletedChecked)

        self.checkBoxRoadmap = wx.CheckBox(panel, label='Show in Roadmap')
        self.checkBoxRoadmap.SetFont(checkBoxFont)

        vboxLeft.Add(self.checkBoxLabel, 0)
        vboxLeft.Add(self.checkBoxStarted, 0)
        vboxLeft.Add(self.checkBoxCompleted, 0)
        vboxLeft.Add(self.checkBoxRoadmap, 0)

        # Add prereq list
        self.prereqLabel = wx.StaticText(panel, label='Prerequisite Tasks:')
        self.prereqLabel.SetFont(headingFont)

        taskNames = []
        selectionIndices = []

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

            # Select task if it is a prerequisite
            if project.data['tasks'][i]['id'] in project.data['tasks'][str(taskIndex)]['prereqTaskIDs']:
                if int(i) < taskIndex:
                    selectionIndices.append(int(i))
                else:
                    selectionIndices.append(int(i) - 1)

        self.prereqList = wx.ListBox(panel, style=wx.LB_MULTIPLE, choices=taskNames)
        for i in selectionIndices:
            self.prereqList.Select(i)

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
        self.checkBoxStarted.SetValue(task['started'] or task['completed'])
        self.checkBoxCompleted.SetValue(task['completed'])
        self.checkBoxRoadmap.SetValue(task['showInRoadmap'])

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.project = project
        self.taskIndex = taskIndex
        self.statusText = statusText

    def onStartedChecked(self, event):
        """
        description

        :param event:
        :return:
        """

        if not self.checkBoxStarted.GetValue():
            self.checkBoxCompleted.SetValue(False)

    def onCompletedChecked(self, event):
        """
        description

        :param event:
        :return:
        """

        if self.checkBoxCompleted.GetValue():
            self.checkBoxStarted.SetValue(True)

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

        if self.checkBoxCompleted.GetValue():
            if not task['completed']:
                task['completionDate'] = str(datetime.now())
        else:
            task['completionDate'] = ''

        task['started'] = self.checkBoxStarted.GetValue() or self.checkBoxCompleted.GetValue()
        task['completed'] = self.checkBoxCompleted.GetValue()
        task['showInRoadmap'] = self.checkBoxRoadmap.GetValue()

        prereqIDs = []
        for i in self.prereqList.GetSelections():
            if i < self.taskIndex:
                prereqIDs.append(self.project.data['tasks'][str(i)]['id'])
            else:
                prereqIDs.append(self.project.data['tasks'][str(i + 1)]['id'])
        task['prereqTaskIDs'] = prereqIDs
        # TODO: add started date to create_frame and this one - could be a nice thing to visualize when exporting data

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
