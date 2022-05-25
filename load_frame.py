# progress_tracker - load_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# Handles loading an existing project.

# Import external modules
from datetime import datetime
import json
import wx

# Import custom modules
import start_frame
import overview_frame

# Initialize variables
topPadding = 10
sidePadding = 5
vGap = 20
hGap = 10


class LoadFrame(wx.Frame):
    """
    Allows the user to select an existing project to load and edit.
    """

    def __init__(self, parent, title, statusText):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(LoadFrame, self).__init__(parent, title=title, size=(550, 650))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add label
        self.instructionLabel = wx.StaticText(panel, label='Select a project from the list below.')
        labelFont = self.instructionLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.instructionLabel.SetFont(labelFont)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.instructionLabel, 0, wx.ALIGN_LEFT)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0)
        vbox.AddSpacer(vGap)

        # Create list of existing projects
        self.projects = []
        filePath = 'data/settings.json'

        with open(filePath, 'r') as settingsFile:
            settings = json.load(settingsFile)

            # Iterate over all projects
            for fileName, visible in settings['projects'].items():
                # Check whether the project should be shown
                if not visible:
                    continue

                # Add the project to the list
                with open(fileName, 'r') as projectFile:
                    projectData = json.load(projectFile)
                    projectData['fileName'] = fileName
                    self.projects.append(projectData)
                    projectData['lastModified'] = datetime.strptime(projectData['lastModified'], '%Y-%m-%d %H:%M:%S.%f')
                projectFile.close()

        settingsFile.close()

        # Sort list in reverse order of last modified times
        self.projects.sort(key=lambda item: item['lastModified'], reverse=True)
        projectList = []
        for project in self.projects:
            projectList.append(project['title'])

        # Display project list
        self.projectList = wx.ListBox(panel, 0, style=wx.LB_SINGLE, choices=projectList)
        textFont = self.projectList.GetFont()
        textFont.PointSize = 13
        self.projectList.SetFont(textFont)
        self.projectList.Select(0)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.projectList, 1)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add buttons
        self.loadButton = wx.Button(panel, label='Load')
        self.loadButton.SetFont(labelFont)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadClicked)

        self.cancelButton = wx.Button(panel, label='Cancel')
        self.cancelButton.SetFont(labelFont)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.onCancelClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.loadButton, 0)
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

    def onLoadClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Load button clicked')

        selectionNum = self.projectList.GetSelection()
        if selectionNum == -1:
            print('No element was selected')
            return
        print('Element ' + str(selectionNum) + ' was selected')

        overview_frame.OverviewFrame(None, title='Progress Tracker', statusText=self.statusText,
                                     fileName=self.projects[selectionNum]['fileName'])
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
