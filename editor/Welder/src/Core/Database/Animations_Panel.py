"""Subclass of Animations_Panel, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates
ChangeMaximum_Dialog = Core.Database.Dialogs.ChangeMaximum_Dialog
ChooseGraphic_Dialog = Core.Database.Dialogs.ChooseGraphic_Dialog
AnimationTiming_Dialog = Core.Database.Dialogs.AnimationTiming_Dialog
AnimationTweening_Dialog = Core.Database.Dialogs.AnimationTweening_Dialog
AnimationCellBatch_Dialog = Core.Database.Dialogs.AnimationCellBatch_Dialog
AnimationCellProperties_Dialog = Core.Database.Dialogs.AnimationCellProperties_Dialog
AnimationEntireSlide_Dialog = Core.Database.Dialogs.AnimationEntireSlide_Dialog
#import AnimationFrames_Dialog  # TODO: Forgot to implement these
#import CopyFrames_Dialog
#import ClearFrames_Dialog
PanelBase = Core.Panels.PanelBase
DM = Core.Database.Manager


# Implementing Animations_Panel
class Animations_Panel( Templates.Animations_Panel, PanelBase ):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Animations Panel", "Caption": "Animations Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'animationsicon'}

    def __init__( self, parent ):
        Templates.Animations_Panel.__init__( self, parent )

        DM.DrawHeaderBitmap(self.bitmapAnimations, 'Animations')

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()

    # Handlers for Animations_Panel events.
    def listBoxAnimations_SelectionChanged( self, event ):
        # TODO: Implement listBoxAnimations_SelectionChanged
        pass

    def buttonMaximum_Clicked( self, event ):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def textCtrlName_ValueChanged( self, event ):
        # TODO: Implement textCtrlName_ValueChanged
        pass

    def comboBoxGraphic_Clicked( self, event ):
        # TODO: Implement comboBoxGraphic_Clicked
        pass

    def comboBoxPosition_SelectionChanged( self, event ):
        # TODO: Implement comboBoxPosition_SelectionChanged
        pass

    def comboBoxFrames_Clicked( self, event ):
        # TODO: Implement comboBoxFrames_Clicked
        pass

    def listControlTiming_DoubleClicked( self, event ):
        # TODO: Implement listControlTiming_DoubleClicked
        pass

    def buttonBack_Clicked( self, event ):
        # TODO: Implement buttonBack_Clicked
        pass

    def listBoxFrames_SelectionChanged( self, event ):
        # TODO: Implement listBoxFrames_SelectionChanged
        pass

    def buttonNext_Clicked( self, event ):
        # TODO: Implement buttonNext_Clicked
        pass

    def buttonBattler_Clicked( self, event ):
        # TODO: Implement buttonBattler_Clicked
        pass

    def buttonPaste_Clicked( self, event ):
        # TODO: Implement buttonPaste_Clicked
        pass

    def buttonCopy_Clicked( self, event ):
        # TODO: Implement buttonCopy_Clicked
        pass

    def buttonClear_Clicked( self, event ):
        # TODO: Implement buttonClear_Clicked
        pass

    def buttonTweening_Clicked( self, event ):
        # TODO: Implement buttonTweening_Clicked
        pass

    def buttonCellBatch_Clicked( self, event ):
        # TODO: Implement buttonCellBatch_Clicked
        pass

    def buttonEntireSlide_Clicked( self, event ):
        # TODO: Implement buttonEntireSlide_Clicked
        pass

    def buttonPlayHit_Clicked( self, event ):
        # TODO: Implement buttonPlayHit_Clicked
        pass

    def buttonPlayMiss_Clicked( self, event ):
        # TODO: Implement buttonPlayMiss_Clicked
        pass

    def bitmapAnimationFrames_Clicked( self, event ):
        # TODO: Implement bitmapAnimationFrames_Clicked
        pass


