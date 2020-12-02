# ***************************************************************************
# *   Copyright (c) 2020 Luciano Gorosito lucianogorosito@hotmail.com       *   
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************/

""" FreeCAD Command """

import os
import FreeCAD,Part
import FreeCADGui
from PySide import QtCore,QtGui

class _MainForm_Class():

	def GetResources(self):
		return {'Pixmap' : os.path.join(FreeCAD.getHomePath(), "Mod", "BimModel", "icons", "MF_256.svg"),
		  'Accel' : "",
		  'MenuText' : 'Main Form',
		  'ToolTip' : 'Show a Main Form'}
	
	def Activated(self):
		
		#Load dialog
		self.form = FreeCADGui.PySideUic.loadUi(os.path.join(FreeCAD.getHomePath(), "Mod", "BimModel", "ui_main.ui"))

		# Center the form
		mw = FreeCADGui.getMainWindow()
		self.form.move(mw.frameGeometry().topLeft() + mw.rect().center() - self.form.rect().center())

		# connect signals/slots
		self.form.btnApply.clicked.connect(self.createPlane)


		# Show Dialog
		self.form.show()

	def createPlane(self):
		try:
			# first we check if valid numbers have been entered
			w = float(self.form.txtAncho.text())
			h = float(self.form.txtAlto.text())
		except ValueError:
			QtGui.QMessageBox.information(None, "Error", "Error! Width and Height values must be valid numbers!")
		else:
			# create a face from 4 points
			p1 = FreeCAD.Vector(0,0,0)
			p2 = FreeCAD.Vector(w,0,0)
			p3 = FreeCAD.Vector(w,h,0)
			p4 = FreeCAD.Vector(0,h,0)
			pointList = [p1,p2,p3,p4,p1]
			myWire = Part.makePolygon(pointList)
			myFace = Part.Face(myWire)
			Part.show(myFace)
			self.form.hide()
		
FreeCADGui.addCommand('MainForm_Command', _MainForm_Class())