"""Subclass of BattleProcessing_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing BattleProcessing_Dialog
class BattleProcessing_Dialog( Templates.BattleProcessing_Dialog ):
	def __init__( self, parent ):
		Templates.BattleProcessing_Dialog.__init__( self, parent )
	
	# Handlers for BattleProcessing_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
