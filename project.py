# progress_tracker - project.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/22/2022

# Description:
# TODO: add description of this file

# Import external modules
from datetime import datetime
import json


class Project():
    """
    Handles all interactions with a project data file
    """

    def __init__(self, parent, fileName):
        """
        Create the Project object and load data from the provided file

        :param parent:
        :param fileName:
        """

        # Load project data file
        self.fileName = fileName
        with open(fileName, 'r') as projectFile:
            self.data = json.load(projectFile)
        projectFile.close()

        print('Loaded project data from ' + fileName)

    def saveData(self):
        """
        description

        :return:
        """

        # Save project data
        self.data['lastModified'] = str(datetime.now())
        with open(self.fileName, 'w') as projectFile:
            projectFile.write(json.dumps(self.data, indent=4))
        projectFile.close()

        print('Saved project data to file (' + self.fileName + ')')

    def createTask(self):
        """
        description

        :return:
        """

        # Create new task with default data
        taskIndex = str(len(self.data['tasks']))
        taskData = {}
        self.data['tasks'][taskIndex] = taskData

        taskData['id'] = self.data['nextID']
        self.data['nextID'] = self.data['nextID'] + 1

        taskData['title'] = 'Enter a title for the task here'
        taskData['description'] = 'Enter a description for the task here'
        taskData['showInRoadmap'] = False
        taskData['started'] = False
        taskData['completed'] = False
        taskData['completionDate'] = ''
        taskData['prereqTaskIDs'] = []

        print('Task (id=' + taskData['id'] + ') created')
        return int(taskIndex)

    def deleteTask(self, taskIndex):
        """
        description

        :return:
        """

        # Create a new task list with new indices
        newTaskList = {}

        for i in range(len(self.data['tasks'])):
            if i < taskIndex:
                newTaskList[str(i)] = self.data['tasks'][str(i)]
            elif i > taskIndex:
                newTaskList[str(i - 1)] = self.data['tasks'][str(i - 1)]

        print('Task (id=' + self.data['tasks'][str(taskIndex)]['id'] + ') deleted')
        self.data['tasks'] = newTaskList

    def shiftTaskUp(self, taskIndex):
        """
        description

        :param taskIndex:
        :return:
        """

        if taskIndex > 0:
            temp = self.data['tasks'][str(taskIndex)]
            self.data['tasks'][str(taskIndex)] = self.data['tasks'][str(taskIndex - 1)]
            self.data['tasks'][str(taskIndex - 1)] = temp

            self.saveData()
            print('Swapped positions of tasks (id=' + str(self.data['tasks'][str(taskIndex)]['id']) + ') and (id=' +
                  str(self.data['tasks'][str(taskIndex)]['id']) + ')')
        else:
            print('Selected task cannot be shifted up - it is already at the top of the list')

    def shiftTaskDown(self, taskIndex):
        """
        description

        :param taskIndex:
        :return:
        """

        if taskIndex < len(self.data['tasks']) - 1:
            self.shiftTaskUp(taskIndex + 1)
        else:
            print('Selected task cannot be shifted down - it is already at the bottom of the list')
