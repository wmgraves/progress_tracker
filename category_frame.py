# progress_tracker - category_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/30/2022

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


class CategoryFrame(wx.Frame):
    """
    Allows the user to enter information for creating a new project.
    """

    def __init__(self, parent, title, statusText, project, categoryIndex):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(CategoryFrame, self).__init__(parent, title=title, size=(800, 480))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add title
        self.titleLabel = wx.StaticText(panel, label='Title:')
        headingFont = self.titleLabel.GetFont()
        headingFont.PointSize = 13
        headingFont.Weight = wx.BOLD
        self.titleLabel.SetFont(headingFont)

        self.titleText = wx.TextCtrl(panel)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.titleLabel, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.titleText, 1)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prereq list
        self.taskListLabel = wx.StaticText(panel, label='Related Tasks:')
        self.taskListLabel.SetFont(headingFont)

        taskNames = []
        selectionIndices = []

        for i, taskData in project.data['tasks'].items():
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

            # Select task if it is already associated with this category
            if project.data['tasks'][i]['id'] in project.data['categories'][str(categoryIndex)]['taskIDs']:
                selectionIndices.append(int(i))

        self.taskListCtrl = wx.ListBox(panel, style=wx.LB_MULTIPLE, choices=taskNames, size=(-1, 250))
        for i in selectionIndices:
            self.taskListCtrl.Select(i)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.taskListLabel, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.taskListCtrl, 1)
        hbox.AddSpacer(sidePadding)
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
        self.titleText.SetValue(project.data['categories'][str(categoryIndex)]['title'])

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.project = project
        self.categoryIndex = categoryIndex
        self.statusText = statusText

    def onSaveClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Save button clicked')

        # Update task data
        category = self.project.data['categories'][str(self.categoryIndex)]

        category['title'] = self.titleText.GetValue()

        taskIDs = []
        for i in self.taskListCtrl.GetSelections():
            taskIDs.append(self.project.data['tasks'][str(i)]['id'])
        category['taskIDs'] = taskIDs

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

        self.project.deleteCategory(self.categoryIndex)
        self.project.saveData()
        overview_frame.OverviewFrame(None, title='Progress Tracker', statusText=self.statusText,
                                     fileName=self.project.fileName)
        self.Close(True)

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
