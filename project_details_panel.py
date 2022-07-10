# progress_tracker - project_details_panel.py
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


class ProjectDetailsPanel(wx.Panel):
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
        self.resetButton = wx.Button(self, label=stringsData['resetButton'])
        self.resetButton.SetFont(labelFont)
        self.resetButton.Bind(wx.EVT_BUTTON, self.onResetClicked)

        self.saveButton = wx.Button(self, label=stringsData['saveButton'])
        self.saveButton.SetFont(labelFont)
        self.saveButton.Bind(wx.EVT_BUTTON, self.onSaveClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.resetButton, 1)
        hbox.AddSpacer(hGap)
        hbox.Add(self.saveButton, 1)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(topPadding)

        self.exportButton = wx.Button(self, label=stringsData['exportButton'])
        self.exportButton.SetFont(labelFont)
        self.exportButton.Bind(wx.EVT_BUTTON, self.onExportClicked)

        self.closeButton = wx.Button(self, label=stringsData['closeButton'])
        self.closeButton.SetFont(labelFont)
        self.closeButton.Bind(wx.EVT_BUTTON, self.onCloseClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.exportButton, 1)
        hbox.AddSpacer(hGap)
        hbox.Add(self.closeButton, 1)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(topPadding)

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)

    def onResetClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print("onResetClicked")
        #TODO implement this

    def onSaveClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print("onSaveClicked")
        #TODO implement this

    def onExportClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print("onExportClicked")
        #TODO implement this

    def onCloseClicked(self, event):
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
