"""Subclass of ControlTimer_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ControlTimer_Dialog
class ControlTimer_Dialog( Templates.ControlTimer_Dialog ):
	def __init__( self, parent ):
		Templates.ControlTimer_Dialog.__init__( self, parent )
	
	# Handlers for ControlTimer_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
