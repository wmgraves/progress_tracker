# progress_tracker - overview_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# TODO: add description of this file

# Import external libraries
import wx

# Import custom modules
import start_frame

# Initialize variables
topPadding = 10
sidePadding = 5
vGap = 20
hGap = 15

class OverviewFrame(wx.Frame):
    """
    Displays an overview of a project's data.
    """
    
    def __init__(self, parent, title, statusText):
        """
        Creates the frame.

        :param parent:
        :param title:
        """
        
        # Prepare frame
        super(OverviewFrame, self).__init__(parent, title = title, size = (800, 700))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)
        
        # Add title
        self.titleLabel = wx.StaticText(panel, label = 'Project title goes here')
        labelFont = self.titleLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.titleLabel.SetFont(labelFont)
        
        self.titleButton = wx.Button(panel, label = 'Edit')
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
        
        # Add description
        self.descriptionLabel = wx.StaticText(panel, label = 'Description:')
        descriptionFont = self.descriptionLabel.GetFont()
        descriptionFont.PointSize = 13
        descriptionFont.Weight = wx.BOLD
        self.descriptionLabel.SetFont(descriptionFont)
        
        self.descriptionButton = wx.Button(panel, label = 'Edit')
        self.descriptionButton.SetFont(editFont)
        
        self.descriptionText = wx.TextCtrl(panel, value = 'Project description goes here', size = (-1, 150),
                                           style = wx.TE_MULTILINE)
        
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
        
        print('Exit to Main menu button clicked')
        start_frame.StartFrame(None, title = 'ProgressTracker', statusText = self.statusText)
        self.Close(True)
