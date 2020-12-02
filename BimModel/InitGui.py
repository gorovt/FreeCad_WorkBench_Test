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

import os
import FreeCAD

class BimModelWorkbench(Workbench):

    MenuText = "BIM Model"
    ToolTip = "Tools for BIM Modeling"
    Icon = os.path.join(FreeCAD.getHomePath(), "Mod", "BimModel", "icons", "UniBim_logo_32.svg")
    
    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import HolaMundo 
        self.list = ['HolaMundo_Command'] # A list of command names created
        self.appendToolbar("BimModelToolbar", self.list) # creates a new toolbar with your commands
        self.appendMenu("BimModel", self.list) # creates a new menu
        #self.appendMenu(["BimModel","My submenu"],self.list) # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed when the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("BIM Commands", self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"

Gui.addWorkbench(BimModelWorkbench())