# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# TODO: add description of this file

import wx

defaultStatusText = 'Welcome to progress Tracker! (NOTE: This app is still in development. Visit https://github.com/wmgraves for more information.) '

class MainMenuFrame(wx.Frame):
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
        super(MainMenuFrame, self).__init__(parent, title=title, size=(550, 600))
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
        # self.createButton.Bind(wx.EVT_MOUSE_EVENTS, self.onCreateMouseEvents)
        
        # Add load project button
        vbox.AddSpacer(20)
        self.loadButton = wx.Button(panel, -1, 'Load Project')
        self.loadButton.SetFont(font)
        
        vbox.Add(self.loadButton, 0, wx.ALIGN_CENTER)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadClicked)
        # self.loadButton.Bind(wx.EVT_MOUSE_EVENTS, self.onLoadMouseEvents)
        
        # Display frame
        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()
        
        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(defaultStatusText)
    
    def onCreateMouseEvents(self, event):
        """
        description
        
        :param event:
        :return:
        """
        
        if event.Entering():
            self.SetStatusText('Opens the dialog for creating a new project.')
        elif event.Leaving():
            self.SetStatusText(defaultStatusText)
    
    def onCreateClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """
        
        print('Create Project button clicked')

    def onLoadMouseEvents(self, event):
        """
        description

        :param event:
        :return:
        """
    
        if event.Entering():
            self.SetStatusText('Displays a list of existing projects that can be loaded.')
        elif event.Leaving():
            self.SetStatusText(defaultStatusText)
    
    def onLoadClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """
        
        print('Load Project button clicked')

app = wx.App()
MainMenuFrame(None, title='Progress Tracker')
app.MainLoop()
