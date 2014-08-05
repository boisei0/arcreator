"""Subclass of ChooseActor_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ChooseActor_Dialog
class ChooseActor_Dialog( Templates.ChooseActor_Dialog ):
	def __init__( self, parent ):
		Templates.ChooseActor_Dialog.__init__( self, parent )
	
	# Handlers for ChooseActor_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
