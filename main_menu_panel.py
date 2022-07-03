# progress_tracker - main_menu_panel.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/03/2022

# Description:
# TODO: add description of this file

# Import external modules
import wx


# Import custom modules
# TODO: imports


class MainMenuPanel(wx.Panel):
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
        self.SetSizer(vbox)
        vbox.AddSpacer(50)

        # Add the logo
        logo = wx.Image('resources/logo.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.logoImage = wx.StaticBitmap(self, -1, logo)
        vbox.Add(self.logoImage, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(80)

        # Add buttons
        self.createButton = wx.Button(self, -1, stringsData['createButton'])
        buttonFont = self.createButton.GetFont()
        buttonFont.PointSize = 25
        buttonFont.Weight = wx.BOLD
        self.createButton.SetFont(buttonFont)
        self.createButton.Bind(wx.EVT_BUTTON, self.onCreateClicked)
        vbox.Add(self.createButton, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(20)

        self.loadButton = wx.Button(self, -1, stringsData['loadButton'])
        self.loadButton.SetFont(buttonFont)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadClicked)
        vbox.Add(self.loadButton, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(20)

        self.settingsButton = wx.Button(self, -1, stringsData['settingsButton'])
        self.settingsButton.SetFont(buttonFont)
        self.settingsButton.Bind(wx.EVT_BUTTON, self.onSettingsClicked)
        vbox.Add(self.settingsButton, 0, wx.ALIGN_CENTER)

    def onCreateClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print('onCreateClicked')

        # Show the new panel
        panelList = {
            'create_project_panel': {
                'className': 'CreateProjectPanel',
                'size': 1
            }
        }
        self.panelManager.showPanels(panelList)

    def onLoadClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print('onLoadClicked')

        # Show the new panel
        panelList = {
            'load_project_panel': {
                'className': 'LoadProjectPanel',
                'size': 1
            }
        }
        self.panelManager.showPanels(panelList)

    def onSettingsClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print('onSettingsClicked')
