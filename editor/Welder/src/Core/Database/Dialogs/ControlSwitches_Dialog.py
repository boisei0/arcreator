"""Subclass of ControlSwitches_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ControlSwitches_Dialog
class ControlSwitches_Dialog( Templates.ControlSwitches_Dialog ):
	def __init__( self, parent ):
		Templates.ControlSwitches_Dialog.__init__( self, parent )
	
	# Handlers for ControlSwitches_Dialog events.
	def spinCtrlBatchStart_ValueChanged( self, event ):
		# TODO: Implement spinCtrlBatchStart_ValueChanged
		pass
	
	def spinCtrlBatchEnd_ValueChanged( self, event ):
		# TODO: Implement spinCtrlBatchEnd_ValueChanged
		pass
	
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
