#!/usr/bin/python
# -*- coding: utf-8 -*-

# Implementation of the variable definition wizard page.
#
#
# This file is part of FMICodeGenerator (https://github.com/ghorwin/FMICodeGenerator)
#
# BSD 3-Clause License
#
# Copyright (c) 2018, Andreas Nicolai
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt

from ui.Ui_WizardPageVariables import Ui_WizardPageVariables

from FMIGenerator import FMIGenerator, VarDef

class WizardPageVariables(QWidget):
	def __init__(self):
		super(WizardPageVariables, self).__init__()
		self.ui = Ui_WizardPageVariables()
		self.ui.setupUi(self)
		
		self.ui.groupBox_2.setEnabled(False) # disabled by default
		self.variables = []
		
		# add default variable
		newVar = VarDef("ResultRootDir", "constant", "parameter", "exact")
		newVar.valueRef = 42
		newVar.startValue = "<default>"
		
		self.variables.append(newVar)
		
		self.updateTable()
		self.show()

	def updateTable(self):
		"""Syncronizes self.variables with table widget"""
		
		self.ui.tableWidget.setRowCount(len(self.variables))
		for i in range(len(self.variables)):
			var = self.variables[i]
			
			item = QTableWidgetItem()
			item.setText(var.name)
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.ui.tableWidget.setItem(i, 0, item)
			
			item = QTableWidgetItem()
			item.setText("{}".format(var.valueRef))
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.ui.tableWidget.setItem(i, 1, item)
			
			item = QTableWidgetItem()
			item.setText(var.variability)
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.ui.tableWidget.setItem(i, 2, item)
			
			item = QTableWidgetItem()
			item.setText(var.causality)
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.ui.tableWidget.setItem(i, 3, item)
			
			item = QTableWidgetItem()
			item.setText(var.initial)
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.ui.tableWidget.setItem(i, 4, item)
			
			item = QTableWidgetItem()
			item.setText("{}".format(var.startValue))
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.ui.tableWidget.setItem(i, 5, item)
			
		self.ui.tableWidget.resizeColumnsToContents()

	
	def updateEditField(self, var):
		pass
		


	@pyqtSlot()
	def on_toolButtonAdd_clicked(self):
		# add a new table row and enabled edit field
		currentVarCount = self.ui.tableWidget.rowCount()
		
		newVar = VarDef("<unnamed>", "continuous", "local", "exact")
		self.variables.append(newVar)
		
		# update table
		self.updateTable()
		
		# select last line, this will trigger the edit field population
		self.ui.tableWidget.selectRow(len(self.variables)-1)
