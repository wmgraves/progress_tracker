# progress_tracker - create_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# Handles creating new projects.

# Import external modules
import json
import os
import wx

# Import custom modules
import start_frame
import overview_frame

# Initialize variables
topPadding = 10
sidePadding = 5
vGap = 20
hGap = 10


class CreateFrame(wx.Frame):
    """
    Allows the user to enter information for creating a new project.
    """

    def __init__(self, parent, title, statusText):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(CreateFrame, self).__init__(parent, title=title, size=(550, 650))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add prompts for project title
        self.titleLabel = wx.StaticText(panel, label='Project Title:*')
        labelFont = self.titleLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.titleLabel.SetFont(labelFont)

        self.titleText = wx.TextCtrl(panel)
        textFont = self.titleText.GetFont()
        textFont.PointSize = 13
        self.titleText.SetFont(textFont)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.titleLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.titleText, 1)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prompts for project description
        self.descriptionLabel = wx.StaticText(panel, label='Description:*')
        self.descriptionLabel.SetFont(labelFont)

        self.descriptionText = wx.TextCtrl(panel, size=(-1, 150), style=wx.TE_MULTILINE)
        self.descriptionText.SetFont(textFont)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.descriptionLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.descriptionText, 1)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add buttons
        self.createButton = wx.Button(panel, label='Create')
        self.createButton.SetFont(labelFont)
        self.createButton.Bind(wx.EVT_BUTTON, self.onCreateClicked)

        self.cancelButton = wx.Button(panel, label='Cancel')
        self.cancelButton.SetFont(labelFont)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.onCancelClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.createButton, 0)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.cancelButton, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.ALIGN_RIGHT)

        # Display frame
        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.statusText = statusText

    def onCreateClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Create button clicked')

        # Validate all information
        # TODO: add validation stuff

        # Create new project file
        fileStart = 'data/project_'
        fileEnd = '.json'
        projectNum = 1
        while True:
            if not os.path.isfile(fileStart + str(projectNum) + fileEnd):
                break

            projectNum += 1

        projectData = {
            'title': self.titleText.GetValue(),
            'imageFilepath': '',
            'description': self.descriptionText.GetValue(),
            'tasks': {}
        }

        fileName = fileStart + str(projectNum) + fileEnd
        with open(fileName, 'w') as projectFile:
            projectFile.write(json.dumps(projectData, indent=4))
        projectFile.close()
        print('Created new project data file (' + fileName + ')')

        # Add project file to the settings file
        with open('data/settings.json', 'r+') as settingsFile:
            settingsData = json.load(settingsFile)
            settingsData['projects'][fileName] = True
            settingsFile.seek(0)
            settingsFile.write(json.dumps(settingsData, indent=4))
            settingsFile.truncate()
        settingsFile.close()

        overview_frame.OverviewFrame(None, title='Progress Tracker', statusText=self.statusText, fileName=fileName)
        self.Close(True)

    def onCancelClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Cancel button clicked')
        start_frame.StartFrame(None, title='Progress Tracker', statusText=self.statusText)
        self.Close(True)
