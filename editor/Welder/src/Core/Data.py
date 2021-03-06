'''
Created on Jan 18, 2011

'''
import os
import sys

import ConfigParser

import wx

from Boot import WelderImport

Kernel = WelderImport('Kernel')
KM = Kernel.Manager

def NewProject(mainwindow):
    #handle an already open project
    if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen")) and Kernel.GlobalObjects.has_key("PROJECT"):
        current_project = Kernel.GlobalObjects.get_value("PROJECT")
        if current_project.hasDataChanged() or current_project.hasInfoChanged():
            message = "There are unsaved changes in the currently open project Do you want to save these chagnes?"
        else:
            message = "Do you want to save the currently open project?"
        caption = "There is already an open project"
        dlg = wx.MessageDialog(mainwindow, message, caption, style=wx.YES_NO |
                               wx.YES_DEFAULT)
        result = dlg.ShowModal()
        if result == wx.YES:
            KM.get_component("SaveProjectHandler").object()
    #pull the dialog for the newproject
    dlg = KM.get_component("NewProjectDialog").object(mainwindow)
    result = dlg.ShowModal()
    if result == wx.ID_OK:
        #lets create the project
        template, name, folder = dlg.getdata()
        path = os.path.join(folder, "%s.arcproj" % os.path.basename(folder))
        projectcreator = KM.get_component("ARCProjectCreator").object()
        Kernel.StatusBar.BeginTask(2, "Creating Project")
        projectcreator.Create(path, name, template)
        Kernel.StatusBar.UpdateTask(1, "Finished Creating Project")
        #place the project in the global namespace
        if Kernel.GlobalObjects.has_key("PROJECT"):
            Kernel.GlobalObjects.set_value("PROJECT", projectcreator.getProject())
        else:
            Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectcreator.getProject())
        #set the project title
        if Kernel.GlobalObjects.has_key("Title"):
            Kernel.GlobalObjects.set_value("Title", name)
        else:
            Kernel.GlobalObjects.request_new_key("Title", "CORE", name)
        #set the current project directory
        if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
            Kernel.GlobalObjects.set_value("CurrentProjectDir", path)
        else:
            Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", path)
        #set that there is an open project
        if Kernel.GlobalObjects.has_key("ProjectOpen"):
            Kernel.GlobalObjects.set_value("ProjectOpen", True)
        else:
            Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)
        #refresh the interface on project data change
        Kernel.StatusBar.UpdateTask(1, "Refreshing Interface")
        KM.raise_event("CoreEventRefreshProject")
        Kernel.StatusBar.EndTask()
    dlg.Destroy()

def OpenProject(mainwindow, filehistory, path=""):
    KM.raise_event("CoreEventOpenProject")
    #handle an already open project
    if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen")) and Kernel.GlobalObjects.has_key("PROJECT"):
        current_project = Kernel.GlobalObjects.get_value("PROJECT")
        if current_project.hasDataChanged() or current_project.hasInfoChanged():
            message = "There are unsaved changes in the currently open project Do you want to save these changes?"
        else:
            message = "Do you want to save the currently open project?"
        caption = "There is already an open project"
        dlg = wx.MessageDialog(mainwindow, message, caption, style=wx.YES_NO |
                               wx.YES_DEFAULT)
        result = dlg.ShowModal()
        if result == wx.YES:
            KM.get_component("SaveProjectHandler").object()
    #now lets open a project
    if path == "":
        #if we open the project through file history we alrady have a path 
        #otherwise lets get a path to a project file
        wildcard = "Welder Project File (*.arcproj)|*.arcproj"
        defaultpath = (os.path.join(wx.StandardPaths.Get().GetDocumentsDir(),
                                    "ARC"))
        dlg = wx.FileDialog(mainwindow, message="Choose a file",
            defaultDir=defaultpath,
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            #we got a path lets save it
            path = os.path.normpath(dlg.GetPath())
            #and add it to the file history
            filehistory.AddFileToHistory(path)
        else:
            #they pressed cancel on the dialog? then lets exit with out loading a project
            return
         
    if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
        Kernel.GlobalObjects.set_value("CurrentProjectDir", path)
    #get a project loader
    projectloader = KM.get_component("ARCProjectLoader").object()
    #this might take a while lets say we busy
    Kernel.StatusBar.BeginTask(2, "Loading Project")
    projectloader.load(path)
    #ok done loading, that was the longest part of it
    Kernel.StatusBar.UpdateTask(1, "Finished Loading Project")
    #place the project in the global namespace
    if Kernel.GlobalObjects.has_key("PROJECT"):
        Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
    else:
        Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
    #set the Project Title
    if Kernel.GlobalObjects.has_key("Title"):
        Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
    else:
        Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
    #set the current project directory
    if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
        Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(path))
    else:
        Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(path))
    #set that there is an open project
    if Kernel.GlobalObjects.has_key("ProjectOpen"):
        Kernel.GlobalObjects.set_value("ProjectOpen", True)
    else:
        Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)
    #refresh the interface on project data change
    Kernel.StatusBar.UpdateTask(1, "Refreshing Interface")
    KM.raise_event("CoreEventRefreshProject")
    Kernel.StatusBar.EndTask()


def SaveProject():
    KM.raise_event("CoreEventSaveProject")
    if Kernel.GlobalObjects.has_key("PROJECT") and (Kernel.GlobalObjects.get_value("PROJECT") is not None):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        if Kernel.GlobalObjects.has_key("CurrentProjectDir") and not (Kernel.GlobalObjects.get_value("CurrentProjectDir") == ""):
            path = Kernel.GlobalObjects.get_value("CurrentProjectDir")
        else:
            path = os.path.join(wx.StandardPaths.Get().GetDocumentsDir(),
                                    "ARC", "TEMP_No_project_dirrectory_save")
        projectsaver = KM.get_component("ARCProjectSaver").object(project)
        #this might take a while lets say we busy
        Kernel.StatusBar.BeginTask(1, "Saving Project")
        projectsaver.save(path)
        Kernel.StatusBar.UpdateTask(1, "Finished Saving")
        #ok done saving, that was the longest part of it
        KM.raise_event("CoreEventRefreshProject")
        Kernel.StatusBar.EndTask()
    else:
        Kernel.Log("No current project, project not saved", "[Save Project Handeler]")
    
def SaveProjectAS(mainwindow, filehistory):
    KM.raise_event("CoreEventSaveProject")
    if Kernel.GlobalObjects.has_key("PROJECT") and (Kernel.GlobalObjects.get_value("PROJECT") is not None):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        defaultpath = (os.path.join(wx.StandardPaths.Get().GetDocumentsDir(),
                                    "ARC"))
        dlg = wx.DirDialog(mainwindow, "Choose a Location:",
                           defaultPath=defaultpath,
                           style=wx.DD_DEFAULT_STYLE
                           | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            location = dlg.GetPath()
            path = os.path.join(location, "Project.arcproj")
            filehistory.AddFileToHistory(path)
            projectsaver = KM.get_component("ARCProjectSaver").object()
            #this might take a while lets say we busy
            Kernel.StatusBar.BeginTask(1, "Saving Project")
            projectsaver.save(path)
            #ok done saving, that was the longest part of it
            Kernel.StatusBar.UpdateTask(1, "Finished Saving")
            #set the current project directory
            if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
                Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(path))
            else:
                Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(path))
            Kernel.StatusBar.EndTask()
    else:
        Kernel.Log("No current project, project not saved", "[Save AS Project Handeler]")


# Was fun for a while, but no longer needed in the active codebase
# class A1Fools(object):
#
#     @staticmethod
#     def auto_save(self):
#         raise SystemError("It Broke")
#
#     @staticmethod
#     def save_now(self):
#         raise SystemError("Oh look, a Problem, I should fix that")
#
#     @staticmethod
#     def mouse_click(self, event):
#         raise SystemError("Fix your Video Drivers, I'm not your mother!")
#
#     @staticmethod
#     def database_panel_open(self):
#         raise SystemError("Thouse pesky bugs, cant keep them out!")