# progress_tracker - project.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/10/2022

# Description:
# TODO: add description of this file

# Import external modules
import json

# Import custom modules
from task import Task

class Project():
    """
    text
    """

    def __init__(self, projectFilePath):
        """
        text

        :param projectFilePath:
        """

        self.projectFilepath = projectFilePath

        # Load data from file
        dataFile = open(projectFilePath, 'r')
        data = json.load(dataFile)
        dataFile.close()

        # Set up project variables
        self.title = data['general']['title']
        self.description = data['general']['description']
        self.logoFilePath = data['general']['logoFilePath']
        self.requirements = data['general']['requirements']
        self.nextTaskID = data['general']['nextTaskID']

        self.tasks = []
        for taskData in data['tasks'].values():
            self.tasks.append(Task(taskData))

        # Calculate progress counts
        self.count = 0
        self.countCompleted = 0
        self.countInProgress = 0
        self.countOverdue = 0
        self.countAvailable = 0
        self.countNotReady = 0
        self.updateTaskCounts()

    def updateTaskCounts(self):
        """
        text

        :return:
        """

        # Reset counts
        self.count = 0
        self.countCompleted = 0
        self.countInProgress = 0
        self.countOverdue = 0
        self.countAvailable = 0
        self.countNotReady = 0

        # Update counts
        for taskData in self.tasks:
            self.count += 1

            status = taskData.getStatus()
            if status == "Completed":
                self.countCompleted += 1
            elif status == "In Progress":
                self.countInProgress += 1
            elif status == "Overdue":
                self.countOverdue += 1
            elif status == "Available":
                self.countAvailable += 1
            else:
                self.countNotReady += 1

    def saveData(self):
        """
        text

        :return:
        """

        # Prepare data
        data = {
            "general": {
                "title": self.title,
                "description": self.description,
                "logoFilePath": self.logoFilePath,
                "requirements": self.requirements,
                "nextTaskID": self.nextTaskID
            },
            "stats": {},
            "tasks": {}
        }

        data['stats']['count'] = self.count
        data['stats']['countCompleted'] = self.countCompleted
        data['stats']['countInProgress'] = self.countInProgress
        data['stats']['countOverdue'] = self.countOverdue
        data['stats']['countAvailable'] = self.countAvailable
        data['stats']['countNotReady'] = self.countNotReady

        for task in self.tasks:
            taskData = task.getPackagedData()
            data['tasks'][str(taskData['id'])] = taskData

        # Save data
        dataFile = open(self.projectFilepath, 'w')
        json.dump(data, dataFile, indent=4)
        dataFile.close()
