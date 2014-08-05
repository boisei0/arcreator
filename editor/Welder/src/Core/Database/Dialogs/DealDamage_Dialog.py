"""Subclass of DealDamage_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing DealDamage_Dialog
class DealDamage_Dialog( Templates.DealDamage_Dialog ):
	def __init__( self, parent ):
		Templates.DealDamage_Dialog.__init__( self, parent )
	
	# Handlers for DealDamage_Dialog events.
	def radioButtonEnemy_CheckChanged( self, event ):
		# TODO: Implement radioButtonEnemy_CheckChanged
		pass
	
	def radioButtonActor_CheckChanged( self, event ):
		# TODO: Implement radioButtonActor_CheckChanged
		pass
	
	def radioButtonConstant_CheckChanged( self, event ):
		# TODO: Implement radioButtonConstant_CheckChanged
		pass
	
	def radioButtonVariable_CheckChanged( self, event ):
		# TODO: Implement radioButtonVariable_CheckChanged
		pass
	
	def comboBoxVariable_Clicked( self, event ):
		# TODO: Implement comboBoxVariable_Clicked
		pass
	
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
