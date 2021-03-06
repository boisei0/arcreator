import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates
PanelBase = Core.Panels.PanelBase
DM = Core.Database.Manager

ChangeMaximum_Dialog = Core.Database.Dialogs.ChangeMaximum_Dialog

#--------------------------------------------------------------------------------------
# States_Panel
#--------------------------------------------------------------------------------------

# Implementing States_Panel
class States_Panel( Templates.States_Panel, PanelBase ):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "States Panel", "Caption": "States Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'statesicon'}

    def __init__( self, parent ):
        Templates.States_Panel.__init__( self, parent )

        DM.DrawHeaderBitmap(self.bitmapStates, 'States')

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()

    # Handlers for States_Panel events.
    def listBoxStates_SelectionChanged( self, event ):
        # TODO: Implement listBoxStates_SelectionChanged
        pass

    def buttonMaximum_Clicked( self, event ):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def textCtrlName_ValueChanged( self, event ):
        # TODO: Implement textCtrlName_ValueChanged
        pass

    def comboBoxAnimation_SelectionChanged( self, event ):
        # TODO: Implement comboBoxAnimation_SelectionChanged
        pass

    def comboBoxRestriction_SelectionChanged( self, event ):
        # TODO: Implement comboBoxRestriction_SelectionChanged
        pass

    def checkBoxNonresistance_CheckChanged( self, event ):
        # TODO: Implement checkBoxNonresistance_CheckChanged
        pass

    def checkBoxHP0_CheckChanged( self, event ):
        # TODO: Implement checkBoxHP0_CheckChanged
        pass

    def checkBoxNoExp_CheckChanged( self, event ):
        # TODO: Implement checkBoxNoExp_CheckChanged
        pass

    def checkBoxNoEvade_CheckChanged( self, event ):
        # TODO: Implement checkBoxNoEvade_CheckChanged
        pass

    def checkBoxSlipDamage_CheckChanged( self, event ):
        # TODO: Implement checkBoxSlipDamage_CheckChanged
        pass

    def spinCtrlRating_ValueChanged( self, event ):
        # TODO: Implement spinCtrlRating_ValueChanged
        pass

    def spinCtrlHitRate_ValueChanged( self, event ):
        # TODO: Implement spinCtrlHitRate_ValueChanged
        pass

    def spinCtrlMaxHP_ValueChanged( self, event ):
        # TODO: Implement spinCtrlMaxHP_ValueChanged
        pass

    def spinCtrlMaxSP_ValueChanged( self, event ):
        # TODO: Implement spinCtrlMaxSP_ValueChanged
        pass

    def spinCtrlStr_ValueChanged( self, event ):
        # TODO: Implement spinCtrlStr_ValueChanged
        pass

    def spinCtrlDex_ValueChanged( self, event ):
        # TODO: Implement spinCtrlDex_ValueChanged
        pass

    def spinCtrlAgi_ValueChanged( self, event ):
        # TODO: Implement spinCtrlAgi_ValueChanged
        pass

    def spinCtrlInt_ValueChanged( self, event ):
        # TODO: Implement spinCtrlInt_ValueChanged
        pass

    def spinCtrlAtk_ValueChanged( self, event ):
        # TODO: Implement spinCtrlAtk_ValueChanged
        pass

    def spinCtrlPdef_ValueChanged( self, event ):
        # TODO: Implement spinCtrlPdef_ValueChanged
        pass

    def spinCtrlMdef_ValueChanged( self, event ):
        # TODO: Implement spinCtrlMdef_ValueChanged
        pass

    def spinCtrlEva_ValueChanged( self, event ):
        # TODO: Implement spinCtrlEva_ValueChanged
        pass

    def checkBoxBattleRelease_CheckChanged( self, event ):
        # TODO: Implement checkBoxBattleRelease_CheckChanged
        pass

    def spinCtrlTurns_ValueChanged( self, event ):
        # TODO: Implement spinCtrlTurns_ValueChanged
        pass

    def spinCtrlTurnPercent_ValueChanged( self, event ):
        # TODO: Implement spinCtrlTurnPercent_ValueChanged
        pass

    def spinCtrlPhysical_ValueChanged( self, event ):
        # TODO: Implement spinCtrlPhysical_ValueChanged
        pass

    def checkListElements_CheckChanged( self, event ):
        # TODO: Implement checkListElements_CheckChanged
        pass

    def checkListStates_CheckChanged( self, event ):
        # TODO: Implement checkListStates_CheckChanged
        pass


