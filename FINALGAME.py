#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:07:24 2019

@author: brooksdanielson
"""

import graphics as g
import Directions
import Endscreen
import Logs_Clouds_Hit
import Jump_and_Duck
import Titlescreen
import random

w = Titlescreen.w
obj = []

def create(): 
   r = [0,1]  
   c = random.choice(r)
   if c == 0:
    
       obj.append(Logs_Clouds_Hit.Log(w,1050,450))
   elif c == 1:
 
       obj.append(Logs_Clouds_Hit.Cloud(w,1050,450))
   if not gameover:
       w.after(3000,create)
   

def main():
    global gameover
    Titlescreen.TitleScreen()
    key = None
    counter = 0
    scounter=0
    gameover=False
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
            while key!= 'e' and not gameover:
                key=w.checkKey()
                H.control(key)
                H.updatestate()
                for o in obj.copy():
                    if o.hit(H):
                        gameover=True
                    if o.offscreen():
                        scounter +=1
                        obj.remove(o)
                g.update(30)
        if gameover:
            break
    for item in w.items[:]:
        item.undraw()
    if scounter>0:
        scounter+=1
    Endscreen.EndScreen(scounter)
    while key!= 'e':
        key=w.checkKey()
        for o in obj:
            o.obj.undraw()
            obj.remove(o)
            
             
               
       
           
                
    
                
            
    w.close()
                
    
if __name__ == '__main__':
    main()