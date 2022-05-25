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

    def __init__(self, parent, title, statusText, project):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(TaskFrame, self).__init__(parent, title=title, size=(800, 650))
        self.project = project
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add title
        self.titleLabel = wx.StaticText(panel, label='Title:')
        headingFont = self.titleLabel.GetFont()
        headingFont.PointSize = 13
        headingFont.Weight = wx.BOLD
        self.titleLabel.SetFont(headingFont)

        self.titleText = wx.TextCtrl(panel, value=self.project.data['title'])
        self.titleText.SetInsertionPoint(0)

        self.titleResetButton = wx.Button(panel, label='Reset', style=wx.BU_EXACTFIT)
        buttonFont = self.titleResetButton.GetFont()
        buttonFont.PointSize = 10
        self.titleResetButton.SetFont(buttonFont)
        # self.titleResetButton.Bind(wx.EVT_BUTTON, self.onTitleResetClicked)
        self.titleResetButton.SetToolTip('Reset title to last saved value')

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.titleLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.titleText, 1)
        hbox.AddSpacer(hGap)
        hbox.Add(self.titleResetButton, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)

        # Display frame
        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.statusText = statusText
