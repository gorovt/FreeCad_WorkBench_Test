import os
import FreeCAD,FreeCADGui
from PySide import QtGui

class _HolaMundo_Class():

	def GetResources(self):
		return {'Pixmap' : os.path.join(FreeCAD.getHomePath(), "Mod", "BimModel", "icons", "UniBim_logo_32.svg"),
		  'Accel' : "",
		  'MenuText' : 'Hola Mundo',
		  'ToolTip' : 'Show a Hola Mundo message'}
	
	def Activated(self):

		QtGui.QMessageBox.information(None, "Hola mundo", "Hola Goro, saludos desde FreeCAD")

		# Give me your name
		name = QtGui.QInputDialog.getText(None, "...", "Nombre completo:")

		# Ansk and Anser
		reply = QtGui.QMessageBox.question(None, name[0], "¿Estas dispuesto a seguir trabajando con FreeCAD?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			QtGui.QMessageBox.information(None, name[0], "Sabia elección, viajero")
		if reply == QtGui.QMessageBox.No:
			QtGui.QMessageBox.information(None, name[0], "Alejate, tonto mortal")

FreeCADGui.addCommand('HolaMundo_Command', _HolaMundo_Class())