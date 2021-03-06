"""Subclass of ErasePicture_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ErasePicture_Dialog
class ErasePicture_Dialog( Templates.ErasePicture_Dialog ):
	def __init__( self, parent ):
		Templates.ErasePicture_Dialog.__init__( self, parent )
	
	# Handlers for ErasePicture_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
