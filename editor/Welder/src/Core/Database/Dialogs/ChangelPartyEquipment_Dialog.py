"""Subclass of ChangelPartyEquipment_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ChangelPartyEquipment_Dialog
class ChangelPartyEquipment_Dialog( Templates.ChangelPartyEquipment_Dialog ):
	def __init__( self, parent ):
		Templates.ChangelPartyEquipment_Dialog.__init__( self, parent )
	
	# Handlers for ChangelPartyEquipment_Dialog events.
	def radioButtonConstant_CheckChanged( self, event ):
		# TODO: Implement radioButtonConstant_CheckChanged
		pass
	
	def radioButtonVariable_CheckChanged( self, event ):
		# TODO: Implement radioButtonVariable_CheckChanged
		pass
	
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
