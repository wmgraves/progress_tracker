# progress_tracker - project.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/10/2022

# Description:
# TODO: add description of this file

# Import external modules
import json

# Import custom modules
# TODO: imports

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

        self.tasks = []
        #TODO figure out how to fill this list

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
                "requirements": self.requirements
            },
            "stats": {
                "count": 0,
                "countCompleted": 0,
                "countInProgress": 0,
                "countOverdue": 0,
                "countAvailable": 0,
                "countNotReady": 0
            },
            "tasks": {
            }
        }

        # Save data
        dataFile = open(self.projectFilepath, 'w')
        json.dump(data, dataFile, indent=4)
        dataFile.close()
