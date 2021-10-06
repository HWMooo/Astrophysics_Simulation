#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:22:51 2018

@author: harrymoo
"""

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5 import uic
import Planetcode as Pc
from point import point_
from ui.CustomPlanetInfo import CustomPlanetInfo




class MainWindow(QMainWindow):
    def __init__(self):
        
        """Sets the buttons for gui along with default planets and focal point"""
        
        super(MainWindow, self).__init__()
        uic.loadUi("ui/MainWindow.ui", self)
        
        self.planets = []
                
        
        self.planetListLayout = QVBoxLayout()
        widget = QWidget()
        self.planetListContents.setWidget(widget)
        widget.setLayout(self.planetListLayout)
        
        self.addPlanetButton.clicked.connect(lambda x: self.addPlanet())
        self.plotButton.clicked.connect(self.plotResult)
        self.setDefaults.clicked.connect(self.defaults)
        
        self.addPlanet("Sun")

    def defaults(self):
        
        """default configurations"""
        
        self.addPlanet("Earth")
        self.addPlanet("Mars")
    
    def addPlanet(self, selection=None):
        
        """All the data required for orbits, t
        his is the information displayed when a planet is chosen.
        """
        if selection is None:
            selection = self.selectedPlanet.currentText()
        if selection == "Custom Planet":
            self._add_new_planet()
        elif selection == "Sun":
            self._add_new_planet(name="Sun", mass=1.9e30, velocity = point_(0,0,0), position=point_(0,0,0))
            
        elif selection == "Mercury":    
            self._add_new_planet(name="Mercury", mass=3.3e23, velocity=point_(0,47000,0), position=point_(5.7e10,0,0))
            
        elif selection == "Venus":    
            self._add_new_planet(name="Venus", mass=4.9e24, velocity=point_(0,35000,0), position=point_(1.1e11, 0, 0))
            
        elif selection == "Earth":    
            self._add_new_planet(name="Earth", mass=5.9e24, velocity=point_(0,30000,0), position=point_(1.5e11,0,0))
            
        elif selection == "Mars":    
            self._add_new_planet(name="Mars", mass=6.4e23, velocity=point_(0, 24000, 0), position=point_(2.2e11,0,0))
            
        elif selection == "Jupiter":    
            self._add_new_planet(name="Jupiter", mass=1.9e27, velocity=point_(0, 13000, 0), position=point_(7.7e11,0,0))
         
        elif selection == "Saturn":    
            self._add_new_planet(name="Saturn", mass=5.7e26, velocity=point_(0, 9000, 0), position=point_(1.4e12,0,0))
            
        elif selection == "Uranus":    
            self._add_new_planet(name="Uranus", mass=8.7e25, velocity=point_(0, 6835, 0), position=point_(2.8e12,0,0))
            
        elif selection == "Neptune":    
            self._add_new_planet(name="Neptune", mass=1.0e26, velocity=point_(0, 5477, 0), position=point_(4.5e12,0,0))
        
        elif selection == "Pluto":    
            self._add_new_planet(name="Pluto", mass=1.3e22, velocity=point_(0, 4748, 0), position=point_(3.7e12,0,0))

            



    def plotResult(self):
        
        """plots the planets using functions imported 
        from Planetcode.py and uses the above values given in addPlanet
        """
        
        Planets = []
        for planetInfo in self.planets:
            newPlanet = Pc.Planet_(position=planetInfo.getPosition(), 
                               mass=planetInfo.getMass(),
                               velocity=planetInfo.getVelocity(),
                               name=planetInfo.getName())
            Planets.append(newPlanet)
        motions = Pc.simulation(Planets, time_step = 100, number_of_steps = self.timeStepValue.value(), report_freq = 1000)
        self.plotWidget.clearCanvas()
        Pc.plot_output(self.plotWidget.ax, motions)
        self.plotWidget.update()


    def _add_new_planet(self, name="", mass = 0, velocity=point_(0,0,0), position=point_(0,0,0)):
        newPlanetInfo = CustomPlanetInfo(name, mass, velocity, position)
        self.planetListLayout.addWidget(newPlanetInfo)
        self.planets.append(newPlanetInfo)