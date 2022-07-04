# progress_tracker - panel_manager.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/03/2022

# Description:
# TODO: add description of this file

# Import external modules
import wx
import json
import importlib

# Import custom modules
# TODO: imports


class PanelManager(wx.Frame):
    """
    Text
    """

    def __init__(self, parent):
        """
        text

        :param parent:
        """

        self.projectData = None

        # Load strings resource file
        with open('resources/strings.json', 'r') as stringsFile:
            self.stringsData = json.load(stringsFile)
        stringsFile.close()

        # Create the main frame
        wx.Frame.__init__(self, None, title=self.stringsData['panel_manager']['title'])
        self.CreateStatusBar()
        self.SetStatusText(self.stringsData['panel_manager']['statusText'])

        # Preload panels that take a while to load
        panelList = {
            'project_preview_panel': {
                'className': 'ProjectPreviewPanel',
                'size': 1
            }
        }
        self.showPanels(panelList)

        # Display the main menu
        panelList = {
            'main_menu_panel': {
                'className': 'MainMenuPanel',
                'size': 1
            }
        }
        self.showPanels(panelList)

    def showPanels(self, panelList):
        """
        text

        :param panelList:
        :return:
        """

        # Remove existing panels, if any
        if self.GetSizer() is not None:
            self.GetSizer().Clear(True)

        # Create sizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Add panels
        for moduleName, frameData in panelList.items():
            # Check whether panel already exists
            currentModule = importlib.import_module(moduleName)
            currentClass = getattr(currentModule, frameData['className'])
            currentPanel = currentClass(parent=self, stringsData=self.stringsData[moduleName])

            # Add panel to sizer
            hbox.Add(currentPanel, frameData['size'], wx.EXPAND)

        # Show sizer
        self.SetSizer(hbox)
        self.Layout()
        self.Update()
