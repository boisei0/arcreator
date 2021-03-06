"""Subclass of ShowAnimation_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ShowAnimation_Dialog
class ShowAnimation_Dialog( Templates.ShowAnimation_Dialog ):
	def __init__( self, parent ):
		Templates.ShowAnimation_Dialog.__init__( self, parent )
	
	# Handlers for ShowAnimation_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
