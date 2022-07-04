# progress_tracker - project_preview_panel.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/03/2022

# Description:
# TODO: add description of this file

# Import external modules
import matplotlib

matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx

# Import custom modules
# TODO: imports

# Initialize variables
topPadding = 20
sidePadding = 5
vGap = 20
hGap = 10


class ProjectPreviewPanel(wx.Panel):
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
        self.stringsData = stringsData

        # Create panel
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(topPadding)

        # Add project title
        self.titleLabel = wx.StaticText(self, label=stringsData['titleLabel'])
        labelFont = self.titleLabel.GetFont()
        labelFont.PointSize = 15
        labelFont.Weight = wx.BOLD
        self.titleLabel.SetFont(labelFont)
        vbox.Add(self.titleLabel)

        self.titleText = wx.TextCtrl(self, value="PROJECT TITLE GOES HERE")  # , style=wx.TE_READONLY)
        self.titleText.Disable()
        textFont = self.titleText.GetFont()
        textFont.PointSize = 13
        self.titleText.SetFont(textFont)
        vbox.Add(self.titleText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add project description
        self.descriptionLabel = wx.StaticText(self, label=stringsData['descriptionLabel'])
        self.descriptionLabel.SetFont(labelFont)
        vbox.Add(self.descriptionLabel)

        self.descriptionText = wx.TextCtrl(self, value="PROJECT DESCRIPTION GOES HERE", size=(-1, 150),
                                           style=wx.TE_MULTILINE)  # | wx.TE_READONLY)
        self.descriptionText.Disable()
        self.descriptionText.SetFont(textFont)
        vbox.Add(self.descriptionText, 0, wx.EXPAND)
        vbox.AddSpacer(vGap)

        # Add pie chart
        pieChartFigure = Figure()
        self.pieChartAxes = pieChartFigure.add_subplot(111)
        pieChartCanvas = FigureCanvas(self, -1, pieChartFigure)
        pieChartCanvas.SetMinSize(wx.Size(200, 200))
        pieSizer = wx.BoxSizer(wx.VERTICAL)
        pieSizer.Add(pieChartCanvas, 1, wx.GROW)
        vbox.Add(pieSizer, 1, wx.EXPAND)
        vbox.AddSpacer(topPadding)

        self.updatePieChart()

        # Add side padding
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(sidePadding)
        hbox.Add(vbox, 1, wx.EXPAND)
        hbox.AddSpacer(sidePadding)
        self.SetSizer(hbox)

    def updatePieChart(self):
        """
        text

        :return:
        """

        if self.panelManager.projectData is None:
            return

        # Calculate new values
        completedNum = 11
        inProgressNum = 3
        overdueNum = 3
        availableNum = 4
        notReadyNum = 17

        # Plot new values
        values = [completedNum, inProgressNum, overdueNum, availableNum, notReadyNum]
        labels = [self.stringsData['pieCompleted'], self.stringsData['pieInProgress'], self.stringsData['pieOverdue'],
                  self.stringsData['pieAvailable'], self.stringsData['pieNotReady']]

        self.pieChartAxes.pie(values, labels=labels)
        self.pieChartAxes.axis('equal')
