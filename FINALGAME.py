#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:07:24 2019

@author: brooksdanielson
"""

import graphics as g
import Directions
import Endscreen
import FINALPROJ
import Jump_and_Duck
import Titlescreen
import random

w = Titlescreen.w
obj = []

def create():    
   r = [0,1]  
   c = random.choice(r)
   if c == 0:
       #FINALPROJ.Log(w,1000,450)
       obj.append(FINALPROJ.Log(w,1000,450))
   elif c == 1:
       #FINALPROJ.Cloud(w,1000,450)
       obj.append(FINALPROJ.Cloud(w,1000,450))
       
   w.after(3000,create)
   

def main():
    Titlescreen.TitleScreen()
    key = None
    counter = 0
    while key != 'e':    
        key=w.checkKey()
        if key == "Right":
            counter += 1
            for item in w.items[:]:
                item.undraw()
            if counter == 1:
                Directions.DirectionScreen()
                key = None
            if counter == 2:
                w.setBackground("SkyBlue")
                Ground = g.Rectangle(g.Point(0,450), g.Point(1000,700))
                Ground.setFill("ForestGreen")
                Ground.draw(w)
                message0=g.Text(g.Point(500,660), "Press Enter to start") 
                message0.setSize(20)
                message0.draw(w)
                global H
                H = Jump_and_Duck.Hen(w,300,380,70)
                key = None
                
        if key == "Return":
            message0.undraw()
            create()
            key = None
            while key!= 'e':
                key=w.checkKey()
                H.control(key)
                H.updatestate()
                g.update(30)
                
             
               
       
           
                
    
                
            
    w.close()
                
    
if __name__ == '__main__':
    main()