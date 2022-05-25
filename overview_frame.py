# progress_tracker - overview_frame.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# TODO: add description of this file

# Import external modules
import wx

# Import custom modules
import start_frame
import task_frame
from project import Project

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

        # Get project data
        self.project = Project(None, fileName)

        # Prepare frame
        super(OverviewFrame, self).__init__(parent, title=title, size=(800, 710))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add title
        self.titleLabel = wx.StaticText(panel, label='Title:')
        headingFont = self.titleLabel.GetFont()
        headingFont.PointSize = 13
        headingFont.Weight = wx.BOLD
        self.titleLabel.SetFont(headingFont)

        self.titleText = wx.TextCtrl(panel)

        self.titleResetButton = wx.Button(panel, label='Reset', style=wx.BU_EXACTFIT)
        buttonFont = self.titleResetButton.GetFont()
        buttonFont.PointSize = 10
        self.titleResetButton.SetFont(buttonFont)
        self.titleResetButton.Bind(wx.EVT_BUTTON, self.onTitleResetClicked)
        self.titleResetButton.SetToolTip('Reset title to last saved value')

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.titleLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.titleText, 1, wx.EXPAND)
        hbox.AddSpacer(hGap)
        hbox.Add(self.titleResetButton, 0)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add relative logo image filepath
        self.imageLabel = wx.StaticText(panel, label='Relative Image Filepath:')
        self.imageLabel.SetFont(headingFont)

        self.imageText = wx.TextCtrl(panel)

        self.imageResetButton = wx.Button(panel, label='Reset', style=wx.BU_EXACTFIT)
        self.imageResetButton.SetFont(buttonFont)
        self.imageResetButton.Bind(wx.EVT_BUTTON, self.onImageResetClicked)
        self.imageResetButton.SetToolTip('Reset filepath to last saved value')

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.imageLabel, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.imageText, 1, wx.EXPAND)
        hbox.AddSpacer(hGap)
        hbox.Add(self.imageResetButton)
        hbox.AddSpacer(sidePadding)
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add description
        self.descriptionLabel = wx.StaticText(panel, label='Description:')
        self.descriptionLabel.SetFont(headingFont)

        self.descriptionResetButton = wx.Button(panel, label='Reset', style=wx.BU_EXACTFIT)
        self.descriptionResetButton.SetFont(buttonFont)
        self.descriptionResetButton.Bind(wx.EVT_BUTTON, self.onDescriptionResetClicked)
        self.descriptionResetButton.SetToolTip('Reset description to last saved value')

        self.descriptionText = wx.TextCtrl(panel, size=(-1, 150), style=wx.TE_MULTILINE)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(self.descriptionLabel, 0, wx.ALIGN_LEFT)
        hbox.AddSpacer(hGap)
        hbox.Add(self.descriptionResetButton, 0)
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
        self.progressLabel.SetFont(headingFont)

        self.completedBar = wx.Panel(panel, size=(-1, 25))
        self.completedBar.SetBackgroundColour(wx.Colour(0, 204, 0))
        self.completedBar.SetToolTip('50.00% Completed Tasks')

        self.wipBar = wx.Panel(panel)
        self.wipBar.SetBackgroundColour(wx.Colour(204, 204, 0))
        self.wipBar.SetToolTip('25.00% In-Progress Tasks')

        # TODO: change below to ready to start bar
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

        # Add category list
        self.catListLabel = wx.StaticText(panel, label='Categories:')
        self.catListLabel.SetFont(headingFont)

        self.catListCtrl = wx.ListBox(panel, style=wx.LB_SINGLE, choices=['categories not yet loaded'], size=(-1, 200))
        self.catListCtrl.Bind(wx.EVT_LISTBOX_DCLICK, self.onCatListDClicked)

        self.catListAddButton = wx.Button(panel, label='+', style=wx.BU_EXACTFIT)
        buttonFont.Weight = wx.BOLD
        self.catListAddButton.SetFont(buttonFont)
        self.catListAddButton.SetToolTip('Create new category')

        # self.catListRemoveButton = wx.Button(panel, label='-', style=wx.BU_EXACTFIT)
        # self.catListRemoveButton.SetFont(buttonFont)

        self.catListUpButton = wx.Button(panel, label='▲', style=wx.BU_EXACTFIT)
        self.catListUpButton.SetFont(buttonFont)
        self.catListUpButton.SetToolTip('Shift selected category up')

        self.catListDownButton = wx.Button(panel, label='▼', style=wx.BU_EXACTFIT)
        self.catListDownButton.SetFont(buttonFont)
        self.catListDownButton.SetToolTip('Shift selected category down')

        tempButtonHolder = wx.BoxSizer(wx.HORIZONTAL)
        tempButtonHolder.Add(self.catListAddButton, 0)
        # tempButtonHolder.Add(self.catListRemoveButton, 0)
        tempButtonHolder.Add(self.catListUpButton, 0)
        tempButtonHolder.Add(self.catListDownButton, 0)

        temp = wx.BoxSizer(wx.VERTICAL)
        temp.Add(self.catListLabel, 0, wx.ALIGN_LEFT)
        temp.Add(self.catListCtrl, 1, wx.EXPAND)
        temp.Add(tempButtonHolder, 0, wx.ALIGN_RIGHT)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(temp, 1, wx.EXPAND)
        hbox.AddSpacer(hGap)

        # Add task list
        self.taskListLabel = wx.StaticText(panel, label='Tasks:')
        self.taskListLabel.SetFont(headingFont)

        self.taskListCtrl = wx.ListBox(panel, style=wx.LB_SINGLE, choices=['categories not yet loaded'], size=(-1, 200))
        self.taskListCtrl.Bind(wx.EVT_LISTBOX_DCLICK, self.onTaskListDClicked)

        self.taskListAddButton = wx.Button(panel, label='+', style=wx.BU_EXACTFIT)
        self.taskListAddButton.SetFont(buttonFont)
        self.taskListAddButton.SetToolTip('Create new task')

        # self.taskListRemoveButton = wx.Button(panel, label='-', style=wx.BU_EXACTFIT)
        # self.taskListRemoveButton.SetFont(buttonFont)

        self.taskListUpButton = wx.Button(panel, label='▲', style=wx.BU_EXACTFIT)
        self.taskListUpButton.SetFont(buttonFont)
        self.taskListUpButton.SetToolTip('Shift selected task up')

        self.taskListDownButton = wx.Button(panel, label='▼', style=wx.BU_EXACTFIT)
        self.taskListDownButton.SetFont(buttonFont)
        self.taskListDownButton.SetToolTip('Shift selected task down')

        tempButtonHolder = wx.BoxSizer(wx.HORIZONTAL)
        tempButtonHolder.Add(self.taskListAddButton, 0)
        # tempButtonHolder.Add(self.taskListRemoveButton, 0)
        tempButtonHolder.Add(self.taskListUpButton, 0)
        tempButtonHolder.Add(self.taskListDownButton, 0)

        temp = wx.BoxSizer(wx.VERTICAL)
        temp.Add(self.taskListLabel, 0, wx.ALIGN_LEFT)
        temp.Add(self.taskListCtrl, 1, wx.EXPAND)
        temp.Add(tempButtonHolder, 0, wx.ALIGN_RIGHT)

        hbox.Add(temp, 2, wx.EXPAND)
        hbox.AddSpacer(sidePadding)

        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add buttons
        self.saveButton = wx.Button(panel, label='Save')
        bottomButtonFont = self.saveButton.GetFont()
        bottomButtonFont.PointSize = 15
        bottomButtonFont.Weight = wx.BOLD
        self.saveButton.SetFont(bottomButtonFont)
        self.saveButton.Bind(wx.EVT_BUTTON, self.onSaveClicked)
        # self.saveButton.Enable(False)

        self.exportButton = wx.Button(panel, label='Export')
        self.exportButton.SetFont(bottomButtonFont)
        self.exportButton.Bind(wx.EVT_BUTTON, self.onExportClicked)

        self.exitButton = wx.Button(panel, label='Exit to Main Menu')
        self.exitButton.SetFont(bottomButtonFont)
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

        # Fill fields with current values
        self.titleText.SetValue(self.project.data['title'])
        self.imageText.SetValue(self.project.data['imageFilepath'])
        self.descriptionText.SetValue(self.project.data['description'])
        self.updateCatList()
        self.updateTaskList()

        # Add status bar
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.statusText = statusText

    def onTitleResetClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Reset Title button clicked')

        self.titleText.SetValue(self.project.data['title'])

    def onImageResetClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Reset Image button clicked')

        self.imageText.SetValue(self.project.data['imageFilepath'])

    def onDescriptionResetClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Reset Description button clicked')

        self.descriptionText.SetValue(self.project.data['description'])

    def updateCatList(self):
        """
        description

        :return:
        """

        categoryNames = []
        for i in sorted(self.project.data['categories'].keys()):
            # TODO: implement count/sum displays
            categoryNames.append(self.project.data['categories'][i]['title'])

        self.catListCtrl.Set(categoryNames)
        print('Category list updated')

    def updateTaskList(self):
        """
        description

        :return:
        """

        taskNames = []
        for i in sorted(self.project.data['tasks'].keys()):
            startText = ''
            if self.project.data['tasks'][i]['completed']:
                startText += '⬛'
            elif self.project.data['tasks'][i]['started']:
                startText += '◧'
            else:
                startText += '☐'
                # TODO: use above symbol for ready to start and empty space for not yet started
            startText += ' '

            taskNames.append(startText + self.project.data['tasks'][i]['title'])

        self.taskListCtrl.Set(taskNames)
        print('Task list updated')

    def onCatListDClicked(self, event):
        """
        description

        :param event:
        :return:
        """

        print('Category ' + str(event.GetSelection()) + ' double-clicked')

    def onTaskListDClicked(self, event):
        """
        descriptions

        :param event:
        :return:
        """

        print('Task ' + str(event.GetSelection()) + ' double-clicked')

        task_frame.TaskFrame(None, title='Progress Tracker', statusText=self.statusText, project=self.project,
                             taskIndex=event.GetSelection())
        self.Close()

    def onSaveClicked(self, event):
        """
        description
        
        :param event:
        :return:
        """

        print('Save button clicked')

        # Update project data
        self.project.data['title'] = self.titleText.GetValue()
        self.project.data['imageFilepath'] = self.imageText.GetValue()
        self.project.data['description'] = self.descriptionText.GetValue()

        self.project.saveData()
        # self.saveButton.Enable(False)

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
