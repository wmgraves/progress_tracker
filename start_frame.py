# progress_tracker - start_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# Handles the main menu.

# Import external libraries
import wx

# Import custom modules
import create_frame

class StartFrame(wx.Frame):
    """
    The frame used for the app's main menu.
    """
    
    def __init__(self, parent, title):
        """
        Creates the frame.

        :param parent:
        :param title:
        """
        
        # Prepare frame
        super(StartFrame, self).__init__(parent, title = title, size = (550, 500))
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
        
        # Display frame
        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()
        
        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(
            'This app is still in development. Visit https://github.com/wmgraves/progress_tracker for more information.')
    
    def onCreateClicked(self, event):
        """
        description

        :param event:
        :return:
        """
        
        print('Create Project button clicked')
        create_frame.CreateFrame(None, title = 'Progress Tracker')
        self.Close(True)
    
    def onLoadClicked(self, event):
        """
        description

        :param event:
        :return:
        """
        
        print('Load Project button clicked')
