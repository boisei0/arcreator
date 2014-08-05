"""Subclass of ForceAction_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ForceAction_Dialog
class ForceAction_Dialog( Templates.ForceAction_Dialog ):
	def __init__( self, parent ):
		Templates.ForceAction_Dialog.__init__( self, parent )
	
	# Handlers for ForceAction_Dialog events.
	def radioButtonEnemy_CheckChanged( self, event ):
		# TODO: Implement radioButtonEnemy_CheckChanged
		pass
	
	def radioButtonActor_CheckChanged( self, event ):
		# TODO: Implement radioButtonActor_CheckChanged
		pass
	
	def radioButtonBasic_CheckChanged( self, event ):
		# TODO: Implement radioButtonBasic_CheckChanged
		pass
	
	def radioButtonSkill_CheckChanged( self, event ):
		# TODO: Implement radioButtonSkill_CheckChanged
		pass
	
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
