# progress_tracker - data_handler.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 05/15/2022

# Description:
# Handles loading, modifying, and saving project data.

class DataHandler():
    """
    description
    """
    
    def __init__(self):
        """
        description
        
        params
        """
        
        print('init')
    
    def loadData(self):
        """
        description
        - required?  could incorporate into init
        - could keep separate incase user needs to refresh during runtime for some reason
        
        :return:
        """
        
        print('loadData')
        return True  # success status
    
    def saveData(self):
        """
        description
        
        :return:
        """
        
        print('saveData')
        return True  # success status
    
    def createProject(self, projectTitle, projectDescription, projectImageFilepath):
        """
        description
        
        :param projectTitle:
        :param projectDescription:
        :param projectImageFilepath:
        :return:
        """
        
        print('createProject')
        return -1  # project object
    
    def deleteProject(self, projectID):
        """
        description
        - only hide project from lists, do not actually delete data for safety reasons
        
        :param projectID:
        :return:
        """
        
        print('deleteProject')
        return True  # success status
    
    def editTitle(self, projectID, newTitle):
        """
        description
        
        :param projectID:
        :param newTitle:
        :return:
        """
        
        print('editTitle')
        return -1  # new project object
    
    def editDescription(self, projectID, newDescription):
        """
        description
        
        :param projectID:
        :param newDescription:
        :return:
        """
        
        print('editDescription')
        return -1  # new project object
    
    def editImageFilepath(self, projectID, newImageFilepath):
        """
        description
        - no filepath means no image - just display title in place of logo when exporting
        
        :param projectID:
        :param newImageFilepath:
        :return:
        """
        
        print('editImageFilepath')
        return -1  # new project object
    
    def addTask(self, projectID, taskName, taskDescription, taskStartDate, taskDueDate, taskPrereqs, taskComplete,
                taskDifficulty):
        """
        description
        
        :param projectID:
        :param taskName:
        :param taskDescription:
        :param taskStartDate:
        :param taskDueDate:
        :param taskPrereqs:
        :param taskComplete:
        :param taskDifficulty:
        :return:
        """
        
        print('addTask')
        return -1  # new project object
    
    def editTask(self, projectID, taskID, taskName, taskDescription, taskStartDate, taskDueDate, taskPrereqs,
                 taskComplete, taskDifficulty):
        """
        description
        
        :param projectID:
        :param taskID:
        :param taskName:
        :param taskDescription:
        :param taskStartDate:
        :param taskDueDate:
        :param taskPrereqs:
        :param taskComplete:
        :param taskDifficulty:
        :return:
        """
        
        print('editTask')
        return -1  # new project object
    
    def completedTask(self, projectID, taskID, taskCompleted):
        """
        description
        
        :param projectID:
        :param taskID:
        :param taskCompleted:
        :return:
        """
        
        print('completedTask')
        return True  # success status
    
    def deleteTask(self, projectID, taskID):
        """
        description
        
        :param projectID:
        :param taskID:
        :return:
        """
        
        print('deleteTask')
        return -1  # new project object
