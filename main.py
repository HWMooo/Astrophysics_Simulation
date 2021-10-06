#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:46:22 2018

@author: harrymoo
"""
import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow


if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance() 
    
mainWin = MainWindow()
mainWin.show()
app.exec_()

""""Tool tip works for each button, 
along with shortcuts
(use the tool tip to find out shortcuts).
 """