'''
Created on Dec 20, 2010

exports all the core components to the kernel
'''

from Boot import WelderImport

Kernel             = WelderImport('Kernel')
Manager            = Kernel.Manager 
Type               = Kernel.Type
SuperType          = Kernel.SuperType
Component          = Kernel.Component
Package            = Kernel.Package
Event              = Kernel.Event
RMXP               = WelderImport('Core.RMXP')
Frames             = WelderImport('Core.Frames')
Menues             = WelderImport('Core.Menues')
Dialogs            = WelderImport('Core.Dialogs')
Controls           = WelderImport('Core.Controls')
Layouts            = WelderImport('Core.Layouts')
Data               = WelderImport('Core.Data')
Project            = WelderImport('Core.Project')
ARC_Data           = WelderImport('Core.ARC_Data')
Actions            = WelderImport('Core.Actions')
DatabaseActions    = WelderImport('Core.DatabaseActions')
RPGutil            = WelderImport('Core.RPGutil')
Icons              = WelderImport('Core.Icons')
PanelManager       = WelderImport('Core.PanelManager')
Panels             = WelderImport('Core.Panels')
Cache              = WelderImport('Core.Cache')
PyXAL              = WelderImport('Core.PyXAL')
MapEditor          = WelderImport('Core.MapEditor')
Database           = WelderImport('Core.Database')
Core               = WelderImport('Core')
Actors_Panel       = Core.Database.Actors_Panel
Classes_Panel      = Core.Database.Classes_Panel
Skills_Panel       = Core.Database.Skills_Panel
Items_Panel        = Core.Database.Items_Panel
Weapons_Panel      = Core.Database.Weapons_Panel
Armors_Panel       = Core.Database.Armors_Panel
Enemies_Panel      = Core.Database.Enemies_Panel
Troops_Panel       = Core.Database.Troops_Panel
States_Panel       = Core.Database.States_Panel
Animations_Panel   = Core.Database.Animations_Panel
Tilesets_Panel     = Core.Database.Tilesets_Panel
CommonEvents_Panel = Core.Database.CommonEvents_Panel
System_Panel       = Core.Database.System_Panel 
ScriptEditor_Panel = Core.Database.ScriptEditor.ScriptEditor_Panel

#=============================================================================
# * RMXP SuperType Declaration
#=============================================================================
class RMXPType(SuperType):

    #---------------------------- data holder --------------------------------
    RPG = Type("RPG")

    def __init__(self):
        SuperType.__init__(self, "RMXP")

        #=====================================================================
        # * add types
        #=====================================================================
        #------------------------- data holder -------------------------------
        self.add_types(self.RPG)



#=============================================================================
# * PanelManager SuperType Declaration
#=============================================================================
class PanelManagerType(SuperType):

    #--------------------------------- Toolbars ----------------------------------
    MainToolbar = Type("MainToolbar")
    DatabaseToolbar = Type("DatabaseToolbar")
    #----------------------------- Panels ------------------------------------
    StartPanel = Type("StartPanel")
    ShadowPanel = Type("ShadowPanel")
    TilesetPanel = Type("TilesetPanel")
    MapTreePanel = Type("MapTreePanel")
    MapEditorPanel = Type("MapEditorPanel")
    #Database
    MainActorsPanel = Type("MainActorsPanel")
    MainClassesPanel = Type("MainClassesPanel")
    MainSkillsPanel = Type("MainSkillsPanel")
    MainItemsPanel = Type("MainItemsPanel")
    MainWeaponsPanel = Type("MainWeaponsPanel")
    MainArmorsPanel = Type("MainArmorsPanel")
    MainEnemiesPanel = Type("MainEnemiesPanel")
    MainTroopsPanel = Type("MainTroopsPanel")
    MainStatesPanel = Type("MainStatesPanel")
    MainAnimationsPanel = Type("MainAnimationsPanel")
    MainTilesetsPanel = Type("MainTilesetsPanel")
    MainCommonEventsPanel = Type("MainCommonEventsPanel")
    MainSystemPanel = Type("MainSystemPanel")
    # Event Editor
    MainEventEditorPanel = Type("MainEventEditorPanel")
    # ScriptEditor
    MainScriptEditorPanel = Type("MainScriptEditorPanel")
    
    def __init__(self):
        SuperType.__init__(self, "PanelManagerType")

        #----------------------------- Panels --------------------------------
        self.add_types(self.StartPanel, self.ShadowPanel, self.TilesetPanel, self.MapTreePanel, self.MainToolbar, 
                       self.MapEditorPanel)
        #Database
        self.add_types(self.MainActorsPanel, self.MainClassesPanel, self.MainSkillsPanel, 
                       self.MainItemsPanel, self.MainWeaponsPanel, self.MainArmorsPanel, self.MainEnemiesPanel, 
                       self.MainTroopsPanel, self.MainStatesPanel, self.MainAnimationsPanel, self.MainTilesetsPanel, 
                       self.MainCommonEventsPanel, self.MainSystemPanel)
        #Event Editor
        self.add_types(self.MainEventEditorPanel)
        #Script Editor
        self.add_types(self.MainScriptEditorPanel)
        #--------------------------------- Toolbars ----------------------------------
        self.add_types(self.MainToolbar, self.DatabaseToolbar)

#=============================================================================
# * Package Declaration
#=============================================================================

class CorePackage(Package):
    def __init__(self):
        Package.__init__(self, "CORE", "CORE")
        self.setup_types()
        self.setup_events()
        self.setup_components()
        

    def setup_types(self):
        #=============================================================================
        # * Type Declaration 
        #=============================================================================
        #------------------------------ functions ------------------------------------
        ARCDataDumpFunction = Type("ARCDataDumpFunction")
        ARCDataLoadFunction = Type("ARCDataLoadFunction")
        ARCProjectSaveFunction = Type("ARCProjectSaveFunction")
        ARCProjectLoadFunction = Type("ARCProjectLoadFunction")

        ARCImageFunctions = Type("ARCImageFunctions")
        ARCRTPFunctions = Type("ARCRTPFunctions")

        #---------------------------- Data handlers ----------------------------------
        Project = Type("Project")
        NewProjectHandler = Type("NewProjectHandler")
        OpenProjectHandler = Type("OpenProjectHandler")
        SaveProjectHandler = Type("SaveProjectHandler")
        SaveAsProjectHandler = Type("SaveAsProjectHandler")
        ARCProjectCreator = Type("ARCProjectCreator")
        ARCProjectHolder = Type("ARCProjectHolder")
        ARCProjectSaver = Type("ARCProjectSaver")
        ARCProjectLoader = Type("ARCProjectLoader")

        #------------------------- data holders ------------------------------
        Table = Type("Table")
        IconManager = Type("IconManager")
        RTPCache = Type("RTPCache")
        RTPPygletCache = Type("RTPPygletCache")
      
        #------------------------------- frames --------------------------------------
        EditorMainWindow = Type("EditorMainWindow")
        
        #-------------------------------- ctrls --------------------------------------
        MapEditorWindow = Type("MapEditorWindow")
        MapTreeCtrl = Type("MapTreeCtrl")
        
        #-------------------------------- layouts ------------------------------------
        EditorMainWindowLayout = Type("EditorMainWindowLayout")
        ARCModeLayout = Type("ARCModeLayout")
        PanelManager = Type("PanelManager")
            
        #-------------------------------- menus --------------------------------------
        MainMenuBar = Type("MainMenuBar")
        MainStatusBar = Type("MainStatusBar")
        ProjectMenuItems = Type("ProjectMenuItems")
        PluginMenuItem = Type("PluginMenuItem")
        
        #------------------------------- dialogs -------------------------------------
        NewProjectDialog = Type("NewProjectDialog")
        
        #-------------------------------actions---------------------------------------
        ActionManager = Type("ActionManager")
        ActionTemplate = Type("ActionTemplate")

        TableEditAction           = Type("ARCTableEditAction")
        ARCArmorEditAction           = Type("ARCArmorEditAction")
        ARCActorEditAction           = Type("ARCActorEditAction")
        ARCClassEditAction           = Type("ARCClassEditAction")
        ARCLearningEditAction        = Type("ARCLearningEditAction")
        ARCTroopEditAction           = Type("ARCTroopEditAction")
        ARCSkillEditAction           = Type("ARCSkillEditAction")
        ARCWeaponEditAction          = Type("ARCWeaponEditAction")
        ARCAnimationFrameEditAction  = Type("ARCAnimationFrameEditAction")
        ARCAnimationEditAction       = Type("ARCAnimationEditAction")
        ARCAnimationTimingEditAction = Type("ARCAnimationTimingEditAction")
        ARCAudioFileEditAction       = Type("ARCAudioFileEditAction")
        ARCEnemyEditAction           = Type("ARCEnemyEditAction")
        ARCEnemyActionEditAction     = Type("ARCEnemyActionEditAction")
        ARCEventEditAction           = Type("ARCEventEditAction")
        ARCEventPageEditAction       = Type("ARCEventPageEditAction")
        ARCEventConditionEditAction  = Type("ARCEventConditionEditAction")
        ARCEventGraphicEditAction    = Type("ARCEventGraphicEditAction")
        ARCEventCommandEditAction    = Type("ARCEventCommandEditAction")
        ARCCommonEventEditAction     = Type("ARCCommonEventEditAction")
        ARCMapEditAction             = Type("ARCMapEditAction")
        ARCMapInfoEditAction         = Type("ARCMapInfoEditAction")
        ARCMoveCommandEditAction     = Type("ARCMoveCommandEditAction")
        ARCMoveRouteEditAction       = Type("ARCMoveRouteEditAction")
        ARCStateEditAction           = Type("ARCStateEditAction")
        ARCSystemEditAction          = Type("ARCSystemEditAction")
        ARCTestBattlerEditAction     = Type("ARCTestBattlerEditAction")
        ARCWordsEditAction           = Type("ARCWordsEditAction")
        ARCTilesetEditAction         = Type("ARCTilesetEditAction")
        ARCTroopPageEditAction       = Type("ARCTroopPageEditAction")
        ARCTroopConditionEditAction  = Type("ARCTroopConditionEditAction")
        ARCMemberEditAction          = Type("ARCMemberEditAction")

        #------------------------------ utilities ------------------------------------
        PyXAL = Type("PyXAL")

        #=====================================================================
        # * add the types to be registered 
        #=====================================================================
        #------------------------------ super types ----------------------------------
        self.add_types(RMXPType(), PanelManagerType())
        
        #------------------------------- functions -----------------------------------
        self.add_types(ARCDataDumpFunction, ARCDataLoadFunction, ARCProjectSaveFunction, 
                       ARCProjectLoadFunction, ARCImageFunctions, ARCRTPFunctions)
        
        #------------------------------ data handlers --------------------------------
        self.add_types(Project, NewProjectHandler, OpenProjectHandler, SaveProjectHandler, 
                               SaveAsProjectHandler, ARCProjectCreator, ARCProjectHolder,
                               ARCProjectSaver, ARCProjectLoader)

        #------------------------- data holders ------------------------------
        self.add_types(Table, IconManager, RTPCache, RTPPygletCache)
        
        #-------------------------------- frames -------------------------------------
        self.add_types(EditorMainWindow)

        #-------------------------------- ctrls --------------------------------------
        self.add_types(MapEditorWindow, MapTreeCtrl)
        
        #-------------------------------- layouts --------------------------------
        self.add_types(EditorMainWindowLayout, ARCModeLayout, PanelManager)
        
        #-------------------------------- menus --------------------------------------
        self.add_types(MainMenuBar, MainStatusBar, ProjectMenuItems,
                               PluginMenuItem)
        
        #-------------------------------- dialogs ------------------------------------
        self.add_types(NewProjectDialog)
        
        #-------------------------------actions---------------------------------------
        self.add_types(ActionManager, ActionTemplate)

        self.add_types(TableEditAction)

        self.add_types(ARCArmorEditAction, ARCActorEditAction, ARCClassEditAction, ARCLearningEditAction, 
                       ARCTroopEditAction, ARCSkillEditAction, ARCWeaponEditAction, ARCAnimationFrameEditAction, 
                       ARCAnimationEditAction, ARCAnimationTimingEditAction, ARCAudioFileEditAction, ARCEnemyEditAction, 
                       ARCEnemyActionEditAction, ARCEventEditAction, ARCEventPageEditAction, ARCEventConditionEditAction, 
                       ARCEventGraphicEditAction, ARCEventCommandEditAction, ARCCommonEventEditAction, ARCMapEditAction, 
                       ARCMapInfoEditAction, ARCMoveCommandEditAction, ARCMoveRouteEditAction, ARCStateEditAction, 
                       ARCSystemEditAction, ARCTestBattlerEditAction, ARCWordsEditAction, ARCTilesetEditAction, 
                       ARCTroopPageEditAction, ARCTroopConditionEditAction, ARCMemberEditAction)

        self.add_types(ARCActorEditAction)

        #------------------------------ utilities ------------------------------------
        self.add_types(PyXAL)
        
    def setup_events(self):
        #=============================================================================
        # * events
        #=============================================================================
       
        CoreEventOpenProject = Event("CoreEventOpenProject")
        CoreEventSaveProject = Event("CoreEventSaveProject")
        CoreEventRefreshProject = Event("CoreEventRefreshProject")
        CoreEventUpdateProjectMenu = Event("CoreEventUpdateProjectMenu")
        CoreEventARCRedirectClassPathsOnSave = Event("CoreEventARCRedirectClassPathsOnSave")
        CoreEventARCRedirectClassPathsOnLoad = Event("CoreEventARCRedirectClassPathsOnLoad")
        CoreEventARCExtendNamespaceOnLoad = Event("CoreEventARCExtendNamespaceOnLoad")
        CoreExitMainWindow = Event("CoreExitMainWindow")
        CoreEventAutoSave = Event("CoreEventAutoSave")
        CoreEventMapEditorMouseLeftDown = Event("CoreEventMapEditorMouseLeftDown")
        CoreEventBrokenDatabasePanel = Event("CoreEventBrokenDatabasePanel")

        
        #=====================================================================
        # * add the events to be registered 
        #=====================================================================
        
        self.add_events(CoreEventOpenProject, CoreEventSaveProject, CoreEventRefreshProject, CoreEventUpdateProjectMenu,
                        CoreEventARCRedirectClassPathsOnSave, CoreEventARCRedirectClassPathsOnLoad,
                        CoreEventARCExtendNamespaceOnLoad, CoreExitMainWindow, CoreEventAutoSave, CoreEventMapEditorMouseLeftDown,
                        CoreEventBrokenDatabasePanel)
        
        #=====================================================================
        # * add event hooks to be registered
        #=====================================================================
        self.add_event_hook("CoreEventARCExtendNamespaceOnLoad", RMXP.RGSS1_RPG.extend_namespace,  RMXP.RGSS1_RPG)
        #aprilfools
        # self.add_event_hook("CoreEventAutoSave", Data.A1Fools.auto_save, Data.A1Fools)
        # self.add_event_hook("CoreEventSaveProject", Data.A1Fools.save_now, Data.A1Fools)
        # self.add_event_hook("CoreEventMapEditorMouseLeftDown", Data.A1Fools.mouse_click, Data.A1Fools)
        # self.add_event_hook("CoreEventBrokenDatabasePanel", Data.A1Fools.database_panel_open, Data.A1Fools)


    def setup_components(self):
        #=====================================================================
        # * add components (main components)
        #=====================================================================

        #--------------------------- functions -------------------------------
        self.add_component(Component(ARC_Data.ARC_Dump.dump, "ARCDataDumpFunction",
                                     None, "CoreARCDataDumpFunction", "CORE",
                                     1.0, self))
        self.add_component(Component(ARC_Data.ARC_Dump.load, "ARCDataLoadFunction",
                                     None, "CoreARCDataLoadFunction", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectSaveFunction, "ARCProjectSaveFunction", 
                                     None, "CoreARCProjctSaveFunction", "CORE", 
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectLoadFunction, "ARCProjectLoadFunction", 
                                     None, "CoreARCProjectLoadFunction", "CORE", 
                                     1.0, self))
        self.add_component(Component(Cache.ImageFunctions, "ARCImageFunctions", 
                                     None, "CoreARCImageFunctions", "CORE", 
                                     1.0, self))
        self.add_component(Component(Cache.RTPFunctions, "ARCRTPFunctions", 
                                     None, "CoreARCRTPFunctions", "CORE",
                                     1.0, self))

        #-------------------------- data Handler -----------------------------
        self.add_component(Component(Data.NewProject, "NewProjectHandler",
                                     None, "CoreNewProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Data.OpenProject, "OpenProjectHandler",
                                     None, "CoreOpenProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Data.SaveProject, "SaveProjectHandler",
                                     None, "CoreSaveProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Data.SaveProjectAS, "SaveAsProjectHandler",
                                     None, "CoreSaveAsProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectCreator, "ARCProjectCreator",
                                     None, "CoreARCProjectCreator", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.Project, "ARCProjectHolder",
                                     None, "CoreARCProjectHolder", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectSaver, "ARCProjectSaver",
                                     None, "CoreARCProjectSaver", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectLoader, "ARCProjectLoader",
                                     None, "CoreARCProjectLoader", "CORE",
                                     1.0, self))

        #------------------------- data holders ------------------------------
        self.add_component(Component(RPGutil.Table, "Table", 
                                     None, "CoreTable", "CORE", 
                                     1.0, self))
        self.add_component(Component(Icons.IconManager, "IconManager",
                                     None, "CoreIconManager", "CORE", 
                                     1.0, self))
        self.add_component(Component(Cache.PILCache, "RTPCache",
                                     None, "CoreRTPCache", "CORE",
                                     1.0, self))
        self.add_component(Component(Cache.PygletCache, "RTPPygletCache",
                                     None, "CoreRTPPygletCache", "CORE",
                                     1.0, self))

        #---------------------------- frames ---------------------------------
        self.add_component(Component(Frames.CoreEditorMainWindow,
                                     "EditorMainWindow", None,
                                     "CoreEditorMainWindow", "CORE",
                                     1.0, self))

        #----------------------------- ctrls ---------------------------------
        self.add_component(Component(Controls.WxRMXPMapPanel,
                                     "MapEditorWindow", None,
                                     "WxRMXPMapWindow", "CORE", 1.0, self))
        self.add_component(Component(Controls.MapTreeCtrl,
                                     "MapTreeCtrl", None,
                                     "CoreMapTreeCtrl", "CORE", 1.0,
                                     self))
        

        #----------------------------- layouts -------------------------------
        self.add_component(Component(Layouts.MainWindowLayout,
                                     "EditorMainWindowLayout", None,
                                     "CoreEditorMainWindowLayout", "CORE", 1.0, self))
        self.add_component(Component(Layouts.ARCModeLayout,
                                     "ARCModeLayout", None,
                                     "CoreARCModeLayout", "CORE", 1.0, self))
        self.add_component(Component(PanelManager.PanelManager,
                                     "PanelManager", None,
                                     "CorePanelManager", "CORE", 1.0, self))

        #----------------------------- menus ---------------------------------
        self.add_component(Component(Menues.CoreMainMenuBar, "MainMenuBar",
                                     None, "CoreMainMenuBar", "CORE", 1.0,
                                     self))
        self.add_component(Component(Controls.MainStatusBar,
                                     "MainStatusBar", None, "CoreStatusBar",
                                     "CORE", 1.0, self))
        self.add_component(Component(Menues.PluginMenuItem, "PluginMenuItem",
                                     None, "CorePluginMenuItem", "CORE",
                                     1.0, self))

        #---------------------------- dialogs --------------------------------
        self.add_component(Component(Dialogs.NewProjectDialog,
                                     "NewProjectDialog", None,
                                     "CoreNewProjectDialog", "CORE", 1.0, self))

        #-------------------------------actions---------------------------------------
        self.add_component(Component(Actions.ActionManager, "ActionManager",
                                     None, "CoreActionManager", "CORE", 1.0, self))
        self.add_component(Component(Actions.ActionTemplate, "ActionTemplate",
                                     None, "CoreActionTemplate", "CORE", 1.0, self))
        
        self.add_component(Component(DatabaseActions.TableEditAction, "ARCTableEditAction",
                                     None, "CoreTableEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.ArmorEditAction, "ARCArmorEditAction",
                                     None, "CoreArmorEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.ActorEditAction, "ARCActorEditAction",
                                     None, "CoreActorEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.ClassEditAction, "ARCClassEditAction",
                                     None, "CoreClassEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.LearningEditAction, "ARCLearningEditAction",
                                     None, "CoreLearningEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.TroopEditAction, "ARCTroopEditAction",
                                     None, "CoreTroopEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.SkillEditAction, "ARCSkillEditAction",
                                     None, "CoreSkillEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.WeaponEditAction, "ARCWeaponEditAction",
                                     None, "CoreWeaponEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.AnimationFrameEditAction, "ARCAnimationFrameEditAction",
                                     None, "CoreAnimationFrameEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.AnimationEditAction, "ARCAnimationEditAction",
                                     None, "CoreAnimationEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.AnimationTimingEditAction, "ARCAnimationTimingEditAction",
                                     None, "CoreAnimationTimingEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.AudioFileEditAction, "ARCAudioFileEditAction",
                                     None, "CoreAudioFileEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EnemyEditAction, "ARCEnemyEditAction",
                                     None, "CoreEnemyEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EnemyActionEditAction, "ARCEnemyActionEditAction",
                                     None, "CoreEnemyActionEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EventEditAction, "ARCEventEditAction",
                                     None, "CoreEventEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EventPageEditAction, "ARCEventPageEditAction",
                                     None, "CoreEventPageEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EventConditionEditAction, "ARCEventConditionEditAction",
                                     None, "CoreEventConditionEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EventGraphicEditAction, "ARCEventGraphicEditAction",
                                     None, "CoreEventGraphicEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.EventCommandEditAction, "ARCEventCommandEditAction",
                                     None, "CoreEventCommandEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.CommonEventEditAction, "ARCCommonEventEditAction",
                                     None, "CoreCommonEventEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.MapEditAction, "ARCMapEditAction",
                                     None, "CoreMapEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.MapInfoEditAction, "ARCMapInfoEditAction",
                                     None, "CoreMapInfoEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.MoveCommandEditAction, "ARCMoveCommandEditAction",
                                     None, "CoreMoveCommandEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.MoveRouteEditAction, "ARCMoveRouteEditAction",
                                     None, "CoreMoveRouteEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.StateEditAction, "ARCStateEditAction",
                                     None, "CoreStateEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.SystemEditAction, "ARCSystemEditAction",
                                     None, "CoreSystemEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.TestBattlerEditAction, "ARCTestBattlerEditAction",
                                     None, "CoreTestBattlerEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.WordsEditAction, "ARCWordsEditAction",
                                     None, "CoreWordsEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.TilesetEditAction, "ARCTilesetEditAction",
                                     None, "CoreTilesetEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.TroopPageEditAction, "ARCTroopPageEditAction",
                                     None, "CoreTroopPageEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.TroopConditionEditAction, "ARCTroopConditionEditAction",
                                     None, "CoreTroopConditionEditAction", "CORE", 1.0, self))
        self.add_component(Component(DatabaseActions.MemberEditAction, "ARCMemberEditAction",
                                     None, "CoreMemberEditAction", "CORE", 1.0, self))

        #------------------------------ utilities ------------------------------------
        self.add_component(Component(PyXAL._PyXAL, "PyXAL", None, "CorePyXAL", "CORE", 1.0, self))

        #=====================================================================
        # * add components (RMXP)
        #=====================================================================
        #-------------------------- functions --------------------------------

        #------------------------- data holders ------------------------------
        self.add_component(Component(RMXP.RGSS1_RPG.RPG, "RPG", "RMXP",
                                     "RGSS1_RPG", "CORE", 1.0, self))

        #-------------------------- data handlers ----------------------------


        #----------------------------- ctrls ---------------------------------
        

        #----------------------------- Dialogs -------------------------------

        #=====================================================================
        # * add components (PanelManager)
        #=====================================================================
        #------------------------------ Panels--------------------------------
        self.add_component(Component(Panels.StartPanel, "StartPanel", "PanelManagerType",
                                     "CoreStartPanel", "CORE", 1.0, self))
        self.add_component(Component(Panels.ShadowPanel, "ShadowPanel", "PanelManagerType",
                                     "CoreShadowPanel", "CORE", 1.0, self))

        self.add_component(Component(MapEditor.BrushPanels.TilesetPanel, "TilesetPanel", "PanelManagerType",
                                     "CoreTilesetPanel", "CORE", 1.0, self))
        self.add_component(Component(MapEditor.BrushPanels.MapTreePanel, "MapTreePanel", "PanelManagerType",
                                     "CoreMapTreePanel", "CORE", 1.0, self))
        self.add_component(Component(MapEditor.MapEditorPanel.MapPanel, "MapEditorPanel", "PanelManagerType",
                                     "CoreMapEditorPanel", "CORE", 1.0, self))

        self.add_component(Component(Panels.MainToolbar, "MainToolbar", "PanelManagerType",
                                     "CoreMainToolbar", "CORE", 1.0, self))
        self.add_component(Component(Panels.DatabaseToolbar, "DatabaseToolbar", "PanelManagerType",
                                     "CoreDatabaseToolbar", "CORE", 1.0, self))

        # Database
        self.add_component(Component(Actors_Panel, "MainActorsPanel", "PanelManagerType", 
                                     "COREMainActorsPanel", "CORE", 1.0, self))
        self.add_component(Component(Classes_Panel, "MainClassesPanel", "PanelManagerType", 
                                     "COREMainClassesPanel", "CORE", 1.0, self))
        self.add_component(Component(Skills_Panel, "MainSkillsPanel", "PanelManagerType", 
                                     "COREMainSkillsPanel", "CORE", 1.0, self))
        self.add_component(Component(Items_Panel, "MainItemsPanel", "PanelManagerType", 
                                     "COREMainItemsPanel", "CORE", 1.0, self))
        self.add_component(Component(Weapons_Panel, "MainWeaponsPanel", "PanelManagerType", 
                                     "COREMainWeaponsPanel", "CORE", 1.0, self))
        self.add_component(Component(Armors_Panel, "MainArmorsPanel", "PanelManagerType", 
                                     "COREMainArmorsPanel", "CORE", 1.0, self))
        self.add_component(Component(Enemies_Panel, "MainEnemiesPanel", "PanelManagerType", 
                                     "COREMainEnemiesPanel", "CORE", 1.0, self))
        self.add_component(Component(Troops_Panel, "MainTroopsPanel", "PanelManagerType", 
                                     "COREMainTroopsPanel", "CORE", 1.0, self))
        self.add_component(Component(States_Panel, "MainStatesPanel", "PanelManagerType", 
                                     "COREMainStatesPanel", "CORE", 1.0, self))
        self.add_component(Component(Animations_Panel, "MainAnimationsPanel", "PanelManagerType", 
                                     "COREMainAnimationsPanel", "CORE", 1.0, self))
        self.add_component(Component(Tilesets_Panel, "MainTilesetsPanel", "PanelManagerType", 
                                     "COREMainTilesetsPanel", "CORE", 1.0, self))
        self.add_component(Component(CommonEvents_Panel, "MainCommonEventsPanel", "PanelManagerType", 
                                     "COREMainCommonEventsPanel", "CORE", 1.0, self))
        self.add_component(Component(System_Panel, "MainSystemPanel", "PanelManagerType", 
                                     "COREMainSystemPanel", "CORE", 1.0, self))

        #Event Editor

        #Script Editor
        self.add_component(Component(ScriptEditor_Panel, "MainScriptEditorPanel", "PanelManagerType", 
                                     "COREMainScriptEditorPanel", "CORE", 1.0, self))
        
        



package = CorePackage()
key = package.add_to_kernel()

# this line is only here because it is the core and should be enabled by default, 
# if it was a normal plug-in it would be enabled else where
Manager.enable_packages(key)





