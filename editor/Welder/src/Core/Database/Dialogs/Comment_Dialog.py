"""Subclass of Comment_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing Comment_Dialog
class Comment_Dialog( Templates.Comment_Dialog ):
	def __init__( self, parent ):
		Templates.Comment_Dialog.__init__( self, parent )
	
	# Handlers for Comment_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
