# progress_tracker - create_project_panel.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/03/2022

# Description:
# TODO: add description of this file

# Import external modules
import json
import os.path
import re
import wx

# Import custom modules
import project

# Initialize variables
topPadding = 20
sidePadding = 5
vGap = 20
hGap = 10


class CreateProjectPanel(wx.Panel):
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

        # Add prompt for project title
        self.titleLabel = wx.StaticText(self, label=stringsData['titleLabel'])
        labelFont = self.titleLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.titleLabel.SetFont(labelFont)
        vbox.Add(self.titleLabel)

        self.titleInstruction = wx.StaticText(self, label=stringsData['titleInstruction'])
        instructionFont = self.titleInstruction.GetFont()
        instructionFont.PointSize = 10
        self.titleInstruction.SetFont(instructionFont)
        vbox.Add(self.titleInstruction)

        self.titleText = wx.TextCtrl(self)
        textFont = self.titleText.GetFont()
        textFont.PointSize = 13
        self.titleText.SetFont(textFont)
        vbox.Add(self.titleText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prompt for project logo
        self.logoLabel = wx.StaticText(self, label=stringsData['logoLabel'])
        self.logoLabel.SetFont(labelFont)
        vbox.Add(self.logoLabel)

        self.logoInstruction = wx.StaticText(self, label=stringsData['logoInstruction'])
        self.logoInstruction.SetFont(instructionFont)
        vbox.Add(self.logoInstruction)

        self.logoText = wx.TextCtrl(self)
        self.logoText.SetFont(textFont)
        vbox.Add(self.logoText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prompt for project description
        self.descriptionLabel = wx.StaticText(self, label=stringsData['descriptionLabel'])
        self.descriptionLabel.SetFont(labelFont)
        vbox.Add(self.descriptionLabel)

        self.descriptionInstruction = wx.StaticText(self, label=stringsData['descriptionInstruction'])
        self.descriptionInstruction.SetFont(instructionFont)
        vbox.Add(self.descriptionInstruction)

        self.descriptionText = wx.TextCtrl(self, size=(-1, 150), style=wx.TE_MULTILINE)
        self.descriptionText.SetFont(textFont)
        vbox.Add(self.descriptionText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prompt for project requirements
        self.requirementsLabel = wx.StaticText(self, label=stringsData['requirementsLabel'])
        self.requirementsLabel.SetFont(labelFont)
        vbox.Add(self.requirementsLabel)

        self.requirementsInstruction = wx.StaticText(self, label=stringsData['requirementsInstruction'])
        self.requirementsInstruction.SetFont(instructionFont)
        vbox.Add(self.requirementsInstruction)

        self.requirementsText = wx.TextCtrl(self)
        self.requirementsText.SetFont(textFont)
        vbox.Add(self.requirementsText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add buttons
        self.createButton = wx.Button(self, label=stringsData['createButton'])
        self.createButton.SetFont(labelFont)
        self.createButton.Bind(wx.EVT_BUTTON, self.onCreateClicked)

        self.cancelButton = wx.Button(self, label=stringsData['cancelButton'])
        self.cancelButton.SetFont(labelFont)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.onCancelClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.createButton, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.cancelButton, 0)
        vbox.Add(hbox, 0, wx.ALIGN_RIGHT)
        vbox.AddSpacer(topPadding)

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)

    def onCreateClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        # Validate inputs
        if not self.titleText.GetValue():
            errorMessage = wx.MessageDialog(None, "ERROR: Invalid Input\n\nTitle must not be blank.",
                                            style=wx.OK | wx.ICON_ERROR)
            errorMessage.ShowModal()
            return

        fileName = re.sub(r'\W+', '', self.titleText.GetValue())
        if len(fileName) < 1:
            errorMessage = wx.MessageDialog(None, "ERROR: Invalid Input\n\nTitle must contain at least one "
                                                  "alpha-numeric character.  Alpha-numeric characters are used to determine "
                                                  "the name of the project's data file.",
                                            style=wx.OK | wx.ICON_ERROR)
            errorMessage.ShowModal()
            return

        if len(fileName) > 20:
            fileName = fileName[:20]

        if os.path.isfile('data/' + fileName + '.json'):
            errorMessage = wx.MessageDialog(None, "ERROR: Invalid Input\n\nTitle is too similar to another project's "
                                                  "title, which resulted in a duplicate project data file name.",
                                            style=wx.OK | wx.ICON_ERROR)
            errorMessage.ShowModal()
            errorMessage.Destroy()
            return

        # Create project data file
        data = {
            "general": {
                "title": self.titleText.GetValue(),
                "description": self.descriptionText.GetValue(),
                "logoFilePath": self.logoText.GetValue(),
                "requirements": self.requirementsText.GetValue(),
                "nextTaskID": 2
            },
            "stats": {
                "count": 2,
                "countCompleted": 0,
                "countInProgress": 1,
                "countOverdue": 0,
                "countAvailable": 1,
                "countNotReady": 0
            },
            "tasks": {
                "0": {
                    "id": 0,
                    "title": "This is an example task. Open me to learn more!",
                    "description": "Enter a description for a task in this text box.",
                    "notes": "Enter notes for a task in this text box.",
                    "completed": False,
                    "inProgress": True,
                    "dueDate": None,
                    "prereqIDs": [1]
                },
                "1": {
                    "id": 1,
                    "title": "Create, rearrange, categorize, or delete tasks using the buttons below.",
                    "description": "Enter a description for a task in this text box.",
                    "notes": "Enter notes for a task in this text box.",
                    "completed": False,
                    "inProgress": False,
                    "dueDate": None,
                    "prereqIDs": []
                }
            }
        }

        dataFile = open('data/' + fileName + '.json', 'w')
        json.dump(data, dataFile, indent=4)
        dataFile.close()

        # Prepare project
        self.panelManager.projectData = project.Project('data/' + fileName + '.json')

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
