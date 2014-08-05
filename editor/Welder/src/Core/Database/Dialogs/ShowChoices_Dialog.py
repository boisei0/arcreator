"""Subclass of ShowChoices_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ShowChoices_Dialog
class ShowChoices_Dialog( Templates.ShowChoices_Dialog ):
	def __init__( self, parent ):
		Templates.ShowChoices_Dialog.__init__( self, parent )
	
	# Handlers for ShowChoices_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
