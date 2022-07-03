# progress_tracker - load_project_panel.py
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


class LoadProjectPanel(wx.Panel):
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

        # Add list label
        self.listLabel = wx.StaticText(self, label=stringsData['listLabel'])
        labelFont = self.listLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.listLabel.SetFont(labelFont)
        vbox.Add(self.listLabel)

        # Add list
        self.list = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'Project Title', width=150)
        self.list.InsertColumn(1, 'Last Modified On', width=110)
        self.list.InsertColumn(2, 'Progress', width=60)
        vbox.Add(self.list, 1, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Populate list
        for i in range(10):
            self.list.InsertItem(i, "Project Title " + str(i))
            self.list.SetItem(i, 1, '0' + str(i) + '/0' + str(i) + '/202' + str(i))
            self.list.SetItem(i, 2, str(i) + '.00%')

        # Add buttons
        self.loadButton = wx.Button(self, label=stringsData['loadButton'])
        self.loadButton.SetFont(labelFont)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadClicked)

        self.cancelButton = wx.Button(self, label=stringsData['cancelButton'])
        self.cancelButton.SetFont(labelFont)
        self.cancelButton.Bind(wx.EVT_BUTTON, self.onCancelClicked)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.loadButton, 0)
        hbox.AddSpacer(hGap)
        hbox.Add(self.cancelButton, 0)
        vbox.Add(hbox, 0, wx.ALIGN_RIGHT)
        vbox.AddSpacer(topPadding)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1, wx.EXPAND)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)

    def onLoadClicked(self, event):
        """
        text

        :param event:
        :return:
        """

        print('onLoadClicked')

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
