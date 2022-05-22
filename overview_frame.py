# progress_tracker - overview_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# TODO: add description of this file

# Import external modules
import wx

# Import custom modules
import start_frame

# Initialize variables
topPadding = 10
sidePadding = 5
vGap = 20
hGap = 10


class OverviewFrame(wx.Frame):
    """
    Displays an overview of a project's data.
    """

    def __init__(self, parent, title, statusText, fileName):
        """
        Creates the frame.

        :param parent:
        :param title:
        """

        # Prepare frame
        super(OverviewFrame, self).__init__(parent, title=title, size=(800, 700))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add title
        self.titleLabel = wx.StaticText(panel, label='Project title goes here')
        heading1Font = self.titleLabel.GetFont()
        heading1Font.PointSize = 20
        heading1Font.Weight = wx.BOLD
        self.titleLabel.SetFont(heading1Font)

        self.titleButton = wx.Button(panel, label='Edit')
        editFont = self.titleButton.GetFont()
        editFont.PointSize = 10
        self.titleButton.SetFont(editFont)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.titleLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.titleButton, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add relative logo image filepath
        self.imageLabel = wx.StaticText(panel, label='Relative Image Filepath:')
        heading2Font = self.imageLabel.GetFont()
        heading2Font.PointSize = 13
        heading2Font.Weight = wx.BOLD
        self.imageLabel.SetFont(heading2Font)

        self.imageText = wx.TextCtrl(panel, value='Relative filepath goes here')
        self.imageText.Enable(False)

        self.imageButton = wx.Button(panel, label='Edit')
        self.imageButton.SetFont(editFont)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.imageLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.imageText, 1, wx.EXPAND)
        hbox.AddSpacer(hGap)
        hbox.Add(self.imageButton)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add description
        self.descriptionLabel = wx.StaticText(panel, label='Description:')
        self.descriptionLabel.SetFont(heading2Font)

        self.descriptionButton = wx.Button(panel, label='Edit')
        self.descriptionButton.SetFont(editFont)

        self.descriptionText = wx.TextCtrl(panel, value='Project description goes here', size=(-1, 150),
                                           style=wx.TE_MULTILINE)
        self.descriptionText.Enable(False)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.descriptionLabel, 0, wx.ALIGN_LEFT)
        hbox.AddSpacer(hGap)
        hbox.Add(self.descriptionButton, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.descriptionText, 1)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add progress display
        self.progressLabel = wx.StaticText(panel, label='Progress:')
        self.progressLabel.SetFont(heading2Font)

        self.completedBar = wx.Panel(panel, size=(-1, 25))
        self.completedBar.SetBackgroundColour(wx.Colour(0, 204, 0))
        self.completedBar.SetToolTip('50.00% Completed Tasks')

        self.wipBar = wx.Panel(panel)
        self.wipBar.SetBackgroundColour(wx.Colour(204, 204, 0))
        self.wipBar.SetToolTip('25.00% In-Progress Tasks')

        self.overdueBar = wx.Panel(panel)
        self.overdueBar.SetBackgroundColour(wx.Colour(204, 0, 0))
        self.overdueBar.SetToolTip('12.50% Overdue Tasks')

        self.otherBar = wx.Panel(panel)
        self.otherBar.SetBackgroundColour(wx.Colour(160, 160, 160))
        self.otherBar.SetToolTip('12.50% Other Tasks')

        self.progressBox = wx.BoxSizer(wx.HORIZONTAL)
        self.progressBox.Add(self.completedBar, 4, wx.EXPAND)
        self.progressBox.Add(self.wipBar, 2, wx.EXPAND)
        self.progressBox.Add(self.overdueBar, 1, wx.EXPAND)
        self.progressBox.Add(self.otherBar, 1, wx.EXPAND)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.progressLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.progressBox, 1)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add task overview stuff
        self.taskListLabel = wx.StaticText(panel, label='Task List:')
        self.taskListLabel.SetFont(heading2Font)

        self.taskListCtrl = wx.ListCtrl(panel, style=wx.LB_SINGLE)
        # TODO figure out how to handle per-line formatting stuff

        temp = wx.BoxSizer(wx.VERTICAL)
        temp.Add(self.taskListLabel, 0, wx.ALIGN_LEFT)
        temp.Add(self.taskListCtrl, 0, wx.EXPAND)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(temp, 1, wx.EXPAND)
        hbox.AddSpacer(hGap)

        self.taskDetailsLabel = wx.StaticText(panel, label='Task Details:')
        self.taskDetailsLabel.SetFont(heading2Font)

        # TODO add task detail stuff here

        temp = wx.BoxSizer(wx.VERTICAL)
        temp.Add(self.taskDetailsLabel, 0, wx.ALIGN_LEFT)
        hbox.Add(temp, 2, wx.EXPAND)
        hbox.AddSpacer(sidePadding)

        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add buttons
        self.saveButton = wx.Button(panel, label='Save')
        buttonFont = self.saveButton.GetFont()
        buttonFont.PointSize = 15
        buttonFont.Weight = wx.BOLD
        self.saveButton.SetFont(buttonFont)
        self.saveButton.Bind(wx.EVT_BUTTON, self.onSaveClicked)

        self.exportButton = wx.Button(panel, label='Export')
        self.exportButton.SetFont(buttonFont)
        self.exportButton.Bind(wx.EVT_BUTTON, self.onExportClicked)

        self.exitButton = wx.Button(panel, label='Exit to Main Menu')
        self.exitButton.SetFont(buttonFont)
        self.exitButton.Bind(wx.EVT_BUTTON, self.onExitClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.saveButton, 0)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.exportButton, 0)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.exitButton, 0)
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

    def onSaveClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Save button clicked')

    def onExportClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Export button clicked')

    def onExitClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Exit to Main Menu button clicked')
        start_frame.StartFrame(None, title='Progress Tracker', statusText=self.statusText)
        self.Close(True)
