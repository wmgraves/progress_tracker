# progress_tracker - create_project_panel.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/03/2022

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

        self.logoText = wx.TextCtrl(self)
        self.logoText.SetFont(textFont)
        vbox.Add(self.logoText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prompt for project description
        self.descriptionLabel = wx.StaticText(self, label=stringsData['descriptionLabel'])
        self.descriptionLabel.SetFont(labelFont)
        vbox.Add(self.descriptionLabel)

        self.descriptionText = wx.TextCtrl(self, size=(-1, 150), style=wx.TE_MULTILINE)
        self.descriptionText.SetFont(textFont)
        vbox.Add(self.descriptionText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add prompt for project description
        self.requirementsLabel = wx.StaticText(self, label=stringsData['requirementsLabel'])
        self.requirementsLabel.SetFont(labelFont)
        vbox.Add(self.requirementsLabel)

        self.requirementsText = wx.TextCtrl(self)#, size=(-1, 150), style=wx.TE_MULTILINE)
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

        print('onCreateClicked')

    def onCancelClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print('onCancelClicked')

        # Show the new panel
        panelList = {
            'main_menu_panel': {
                'className': 'MainMenuPanel',
                'size': 1
            }
        }
        self.panelManager.showPanels(panelList)
