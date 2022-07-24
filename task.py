# progress_tracker - task.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 07/18/2022

# Description:
# TODO: add description of this file

# Import external modules
# TODO: imports

# Import custom modules
# TODO: imports

class Task():
    """
    text
    """

    def __init__(self, taskData):
        """
        text

        :param taskData:
        """

        # Initialize variables
        self.taskID = taskData['id']
        self.title = taskData['title']
        self.description = taskData['description']
        self.notes = taskData['notes']
        self.completed = taskData['completed']
        self.inProgress = taskData['inProgress']
        self.dueDate = taskData['dueDate']
        self.prereqIDs = taskData['prereqIDs']

    def getPackagedData(self):
        """
        text

        :return:
        """

        # Prepare data
        return {
            "id": self.taskID,
            "title": self.title,
            "description": self.description,
            "notes": self.notes,
            "completed": self.completed,
            "inProgress": self.inProgress,
            "dueDate": self.dueDate,
            "prereqIDs": self.prereqIDs
        }

    def getStatus(self):
        """
        text

        :return:
        """

        # Figure out and return status
        if self.completed:
            return "Completed"
        elif self.inProgress:
            return "In Progress"
        #TODO add overdue
        #TODO add available

        return "Not Ready"
