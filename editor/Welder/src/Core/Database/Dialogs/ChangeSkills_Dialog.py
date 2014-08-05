"""Subclass of ChangeSkills_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ChangeSkills_Dialog
class ChangeSkills_Dialog( Templates.ChangeSkills_Dialog ):
	def __init__( self, parent ):
		Templates.ChangeSkills_Dialog.__init__( self, parent )
	
	# Handlers for ChangeSkills_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
