import os
import sys
import math

import wx
from wx import glcanvas

import pyglet
from pyglet import gl

import rabbyt

import numpy

from Boot import WelderImport

Kernel = WelderImport('Kernel')
GlobalObjects = Kernel.GlobalObjects
KM = Kernel.Manager

if hasattr(sys, 'frozen'): 
    dirName = sys.executable
else:
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

if not os.path.isdir(dirName):
    LOCAL_PATH = os.path.split(dirName)[0]
else:
    LOCAL_PATH = dirName


    
  

##Kernel.GlobalObjects.get_value("Welder_config").get_section("RTPs").set('RMXP', rtpDir)
TEST_PATH = os.path.join(LOCAL_PATH, "RTP", "Templates", "Default Project", "Default Project.arcproj")
PAGE_INDEX = 0
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Test(wx.App):

    def __init__(self, redirect=False, filename=None):
        # Initialize global dictionary that contains the pages
        global Panels
        # Create the application and main frame
        wx.App.__init__(self, redirect, filename)
        self.load_project()
        self.frame = wx.Frame(None, wx.ID_ANY, title='Welder Database', size=(800, 600))
        self.frame.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
        self.frame.CenterOnScreen()

    def create_panels(self):
        
        nb = wx.Notebook( self.frame )

        Panels = [None for i in xrange(14)]
        Panels[0] = ('Actors', 'Actors_Panel')
        Panels[1] = ('Classes', 'Classes_Panel')
        Panels[2] = ('Skills', 'Skills_Panel')
        Panels[3] = ('Items', 'Items_Panel')
        Panels[4] = ('Weapons', 'Weapons_Panel')
        Panels[5] = ('Armors', 'Armors_Panel')
        Panels[6] = ('Enemies', 'Enemies_Panel')
        Panels[7] = ('Troops', 'Troops_Panel')
        Panels[8] = ('States', 'States_Panel')
        Panels[9] = ('Animations', 'Animations_Panel')
        Panels[10] = ('Tilesets', 'Tilesets_Panel')
        Panels[11] = ('Common Events', 'CommonEvents_Panel')
        Panels[12] = ('System', 'System_Panel')
        Panels[13] = ('Configuration', 'Configuration_Panel')

        for data in Panels:
            if data is None:
                continue
            exec('page = Core.Database.' + data[1] + '(nb)')
            nb.AddPage(page, data[0])
        nb.SetSelection(PAGE_INDEX)
        PyXAL = KM.get_component("PyXAL").object
        if PyXAL is not None:
            PyXAL.Init(self.frame.GetHandle(), True)
        self.frame.Show()

    def load_project(self):
        #get a project loader
        projectloader = KM.get_component("ARCProjectLoader").object()
        projectloader.load(TEST_PATH)
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
            Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(TEST_PATH))
        else:
            Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(TEST_PATH))
        #set that there is an open project
        if Kernel.GlobalObjects.has_key("ProjectOpen"):
            Kernel.GlobalObjects.set_value("ProjectOpen", True)
        else:
            Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)

# Create window and execute the main loop
if __name__ == '__main__':

    if Kernel.GlobalObjects.has_key("Program_Dir"):
        Kernel.GlobalObjects.set_value("Program_Dir", LOCAL_PATH)
    else:
        Kernel.GlobalObjects.request_new_key("Program_Dir", "CORE", LOCAL_PATH)

    print "[BOOT] Programming Running in %s" % dirName
    print "[BOOT] LOCAL PATH: %s" % LOCAL_PATH
    print "[BOOT] CONFIG PATH: %s" % Kernel.GetConfigFolder()

    import Boot
    Boot.ConfigManager.LoadConfig()

    Core = WelderImport('Core')
    Core.late_bind()

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)
    app = Test()
    app.create_panels()
    app.MainLoop()
    app.Destroy()
