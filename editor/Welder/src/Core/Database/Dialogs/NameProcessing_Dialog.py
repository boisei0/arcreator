"""Subclass of NameProcessing_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing NameProcessing_Dialog
class NameProcessing_Dialog( Templates.NameProcessing_Dialog ):
	def __init__( self, parent ):
		Templates.NameProcessing_Dialog.__init__( self, parent )
	
	# Handlers for NameProcessing_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
