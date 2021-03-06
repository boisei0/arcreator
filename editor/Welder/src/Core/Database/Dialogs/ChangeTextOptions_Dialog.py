"""Subclass of ChangeTextOptions_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ChangeTextOptions_Dialog
class ChangeTextOptions_Dialog( Templates.ChangeTextOptions_Dialog ):
	def __init__( self, parent ):
		Templates.ChangeTextOptions_Dialog.__init__( self, parent )
	
	# Handlers for ChangeTextOptions_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
