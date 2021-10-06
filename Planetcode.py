#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:47:01 2018

@author: harrymoo
"""
import math as m
import matplotlib.pyplot as plt


class point_:
    
    """Point_ holds x, y and z data"""
    
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
class Planet_:
    
    """body_ holds position, mass and velocity data, 
    can input name if using information for an existing planet
    """
    
    def __init__(self, position, mass, velocity, name = ""):
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.name = name
  
def planet_acceleration(Planets,Planet_index):
    
    """ takes a list PLanets and index of planets,
    then iterate with all external bodies,
    then sums to acceleration of the target planet,
    Relative correction creates space error, modified to classical theory
    """
    
    G = 6.67408e-11
    acceleration = point_(0,0,0)
    target_Planet = Planets[Planet_index]
    for index, external_Planet in enumerate(Planets):
        if index != Planet_index:
            r = (target_Planet.position.x - external_Planet.position.x)**2 + (target_Planet.position.y - external_Planet.position.y)**2 + (target_Planet.position.z - external_Planet.position.z)**2
            r = m.sqrt(r)
            acceleration_ = G*external_Planet.mass/r**3
            acceleration.x += acceleration_*(external_Planet.position.x-target_Planet.position.x)
            acceleration.y += acceleration_*(external_Planet.position.y-target_Planet.position.y)
            acceleration.z += acceleration_*(external_Planet.position.z-target_Planet.position.z)

    return acceleration

def calculate_velocity(Planets, time_step = 1):
    
    """updates velocity using acceleration and adds to given velocity,
    done before position to keep all time steps in sync
    """
    
    for Planet_index, target_Planet in enumerate(Planets):
        acceleration = planet_acceleration(Planets, Planet_index)

        target_Planet.velocity.x += acceleration.x * time_step
        target_Planet.velocity.y += acceleration.y * time_step
        target_Planet.velocity.z += acceleration.z * time_step 


def update_position(Planets, time_step = 1):
    
    """calculates position using updated velocity with respect to time"""
    
    for target_Planet in Planets:
        target_Planet.position.x += target_Planet.velocity.x * time_step
        target_Planet.position.y += target_Planet.velocity.y * time_step
        target_Planet.position.z += target_Planet.velocity.z * time_step

def gravity_step(Planets, time_step = 1):
    
    """combines above functions into one single function"""
    
    calculate_velocity(Planets, time_step = time_step)
    update_position(Planets, time_step = time_step)     

def plot_output(plotObj, Planets, outfile = None):
    max_range = 0
    for current in Planets: 
        max_dim = max(max(current["x"]),max(current["y"]),max(current["z"]))
        if max_dim > max_range:
            max_range = max_dim
        plotObj.plot(current["x"], current["y"], current["z"], label = current["name"]) 
            
    plotObj.set_xlim([-max_range,max_range])
    plotObj.set_ylim([-max_range,max_range])
    plotObj.set_zlim([-max_range,max_range])
    plotObj.legend()
    
    if outfile:
        plt.savefig(outfile)
    
def simulation(Planets, names = None, time_step = 1, number_of_steps = 500, report_freq = 100):
    
    """Creates container for each planet and repeats calculations for number of steps,
    this value is changed for GUI
    """
    
    Planet_position_history = []
    for current in Planets:
        Planet_position_history.append({"x":[], "y":[], "z":[], "name":current.name})
        
    for i in range(1,number_of_steps):
        gravity_step(Planets, time_step = 1000)            
        
        if i % report_freq == 0:
            for index, Planet_position in enumerate(Planet_position_history):
                Planet_position["x"].append(Planets[index].position.x)
                Planet_position["y"].append(Planets[index].position.y)           
                Planet_position["z"].append(Planets[index].position.z)       

    return Planet_position_history  




        












