# progress_tracker - project.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/22/2022

# Description:
# TODO: add description of this file

# Import external modules
import json


# Import custom modules


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
        with open(self.fileName, 'w') as projectFile:
            projectFile.write(json.dumps(self.data, indent=4))
        projectFile.close()

        print('Saved project data to file (' + self.fileName + ')')
