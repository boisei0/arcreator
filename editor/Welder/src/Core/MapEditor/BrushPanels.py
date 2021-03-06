import wx

from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')
KM = Kernel.Manager

Panels = Core.Panels

class TilesetPanel(wx.ScrolledWindow, Panels.PanelBase):
    
    _arc_panel_info_string = "Name Caption Left CloseB BestS MinimizeM Layer Row Pos MinimizeB DestroyOC"
    _arc_panel_info_data = {
        "Name": "Tileset",
        "Caption": "Tileset",
        "CloseB": False,
        "BestS": (32 * 8, 32 * 12),
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Layer": 1,
        "Row": 1,
        "Pos": 1,
        "MinimizeB": True
    }

    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, wx.ID_ANY)
        self.bindFocus()
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.SetScrollbars(32, 32, 8, 50)


class MapTreePanel(wx.Panel, Panels.PanelBase):

    _arc_panel_info_string = "Name Caption Left CloseB BestS MinimizeM Layer Row Pos MinimizeB IconARCM DestroyOC"
    _arc_panel_info_data = {
        "Name": "Maps",
        "Caption": "Maps",
        "CloseB": False,
        "BestS": (32 * 8, 32 * 4),
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Layer": 1,
        "Row": 1,
        "Pos": 1,
        "MinimizeB": True,
        'IconARCM': 'project_icon'
    }

    def __init__(self, parent, mapEditerPanel=None):
        wx.Panel.__init__(self, parent)

        self.mapEditerPanel = mapEditerPanel

        #set up Sizer
        box = wx.BoxSizer(wx.VERTICAL)
        #set up tree
        mapTreeCtrl = KM.get_component("MapTreeCtrl").object
        self.treectrl = mapTreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250), True)
        #add ctrls to sizer
        box.Add(self.treectrl, 1, wx.ALL | wx.EXPAND)
        #set sizer
        self.SetSizerAndFit(box)

        #bind events
        self.treectrl.Bind(wx.EVT_LEFT_DCLICK, self.TreeLeftDClick)

    def TreeLeftDClick(self, event):
        pt = event.GetPosition()
        item, flags = self.treectrl.HitTest(pt)
        if item:
            data = self.treectrl.GetItemData(item).GetData()
            if data:
                map_id, name = data
                project = Kernel.GlobalObjects.get_value("PROJECT")
                map_ = project.getMapData(map_id)
                tilesets = project.getData("Tilesets")
                if Kernel.GlobalObjects.has_key("PanelManager"):
                    Kernel.GlobalObjects.get_value("PanelManager")\
                        .dispatch_panel("MapEditorPanel", "Map Editor Panel " + str(map_id), arguments=[map_, tilesets],
                                        info="Name Caption", data={"Name": "[" + str(map_id) + "] " + name,
                                                                   "Caption": "[" + str(map_id) + "] " + name})
        event.Skip()