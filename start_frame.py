# progress_tracker - start_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# Handles the main menu.

# Import external modules
import json
import wx

# Import custom modules
from create_frame import CreateFrame
from load_frame import LoadFrame
from settings_frame import SettingsFrame


class StartFrame(wx.Frame):
    """
    The frame used for the app's main menu.
    """

    def __init__(self, parent, title, statusText):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(StartFrame, self).__init__(parent, title=title, size=(550, 550))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(20)

        # Add the logo
        logo = wx.Image('resources/title_image.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.logoImage = wx.StaticBitmap(panel, -1, logo)
        vbox.Add(self.logoImage, 0, wx.ALIGN_CENTER)

        # Add create project button
        vbox.AddSpacer(80)
        self.createButton = wx.Button(panel, -1, 'Create Project')
        font = self.createButton.GetFont()
        font.PointSize = 25
        font.Weight = wx.BOLD
        self.createButton.SetFont(font)

        vbox.Add(self.createButton, 0, wx.ALIGN_CENTER)
        self.createButton.Bind(wx.EVT_BUTTON, self.onCreateClicked)

        # Add load project button
        vbox.AddSpacer(20)
        self.loadButton = wx.Button(panel, -1, 'Load Project')
        self.loadButton.SetFont(font)

        vbox.Add(self.loadButton, 0, wx.ALIGN_CENTER)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadClicked)

        # Check whether the load button should be disabled
        filePath = 'data/settings.json'
        with open(filePath, 'r') as settingsFile:
            settings = json.load(settingsFile)

            # Handle when there are no projects
            if len(settings['projects']) < 1:
                self.loadButton.Enable(False)

            # Handle when there are no visible projects
            else:
                visibleProjects = False
                for value in settings['projects'].values():
                    if value:
                        visibleProjects = True
                        break

                if not visibleProjects:
                    self.loadButton.Enable(False)

        settingsFile.close()

        # Add settings button (true delete, data file location, other stuff)
        vbox.AddSpacer(20)
        self.settingsButton = wx.Button(panel, -1, 'Settings')
        self.settingsButton.SetFont(font)

        vbox.Add(self.settingsButton, 0, wx.ALIGN_CENTER)
        self.settingsButton.Bind(wx.EVT_BUTTON, self.onSettingsClicked)

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

        print('Create Project button clicked')
        CreateFrame(None, title='Progress Tracker', statusText=self.statusText)
        self.Close(True)

    def onSettingsClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Settings button clicked')
        SettingsFrame(None, title='Progress Tracker', statusText=self.statusText)
        self.Close(True)

    def onLoadClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Load Project button clicked')
        LoadFrame(None, title='Progress Tracker', statusText=self.statusText)
        self.Close(True)
