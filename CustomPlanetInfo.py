#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:10:33 2018

@author: harrymoo
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from point import point_


class CustomPlanetInfo(QMainWindow):
    def __init__(self, name="", mass=0, velocity=None, position=None):
        super(CustomPlanetInfo, self).__init__()
        uic.loadUi("ui/planetInfo.ui", self)
        
        """Connects the mass, velocity and position
        for each coordinate to its respective text box
        """
        
        self.massText.setText(str(mass))
        self.nameText.setText(str(name))
        if velocity is not None:
            self.velocityX.setText(str(velocity.x))
            self.velocityY.setText(str(velocity.y))
            self.velocityZ.setText(str(velocity.z))
        if position is not None:
            self.PositionX.setText(str(position.x))
            self.PositionY.setText(str(position.y))
            self.PositionZ.setText(str(position.z))
        
        
    def getVelocity(self):
        
        
        velX = float(self.velocityX.text())
        velY = float(self.velocityY.text())
        velZ = float(self.velocityZ.text())
        return point_(velX, velY, velZ)
    

    def getPosition(self):
        PosX= float(self.PositionX.text())
        PosY= float(self.PositionY.text())
        PosZ= float(self.PositionZ.text())
        return point_(PosX, PosY, PosZ)
    
    def getMass(self):
        return float(self.massText.text())
    
    def getName(self):
        return self.nameText.text()