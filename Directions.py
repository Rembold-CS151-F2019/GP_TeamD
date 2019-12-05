#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:14:50 2019

@author: elliegreenberg
"""

import graphics as g 
import Titlescreen

w= Titlescreen.w


def DirectionScreen():
    w.setBackground("MediumPurple1")
    
    message1 = g.Text(g.Point(158,81), "Directions ")
    message2 = g.Text(g.Point(420,200),"Help Henrietta avoid the obstacles she encounters on her run! ")
    message3 = g.Text(g.Point(450,250), 'Click the Up and Down arrows on your keyboard to jump over logs')
    message4 = g.Text(g.Point(200,300), ' and duck under clouds')
    
    message5=g.Text(g.Point(186,481), ' Henrietta <3')
    message6=g.Text(g.Point(484,481), ' LOGS')
    message7=g.Text(g.Point(797,481), ' CLOUDS')
    message8=g.Text(g.Point(333,673), '  Jump!')
    message9=g.Text(g.Point(662,673), ' Duck!')
    
    message10=g.Text(g.Point(468,148), ' **( press the right arrow to continue )')
    
    message1.setStyle("bold")
    message1.setTextColor("Black")
    message1.setSize(36)
    message1.draw(w)
    
    for  obj in [message2,message3,message4,message5,message6,message7,message8,message9,message10]:
                obj.setSize(25)
                obj.setStyle("bold")
                obj.setTextColor("White")
                obj.draw(w)
                
    Henrietta=g.Circle(g.Point(186,380), 50)
    Henrietta.setFill('DarkSlateBlue')
    Log=g.Circle(g.Point(484,385), 50)
    Log.setFill('sienna4')
    Cloud=g.Circle(g.Point(797,377), 50)
    Cloud.setFill('snow')
    
    Ground1=g.Line(g.Point(266,656), g.Point(405,656))
    Ground1.setOutline("ForestGreen")
    Ground1.setWidth(5)
    Ground2=g.Line(g.Point(601,656), g.Point(726,656))
    Ground2.setOutline("ForestGreen")
    Ground2.setWidth(5)
    
    Jump=g.Circle(g.Point(338,571), 30)
    Jump.setFill('DarkSlateBlue')
    Duck=g.Circle(g.Point(663,643),14)
    Duck.setFill('DarkSlateBlue')
    
    for  obj in [Henrietta, Log, Cloud, Ground1, Ground2, Jump, Duck]:
                obj.draw(w)
    
    
    
    
    
    #print(w.getMouse().getY())
#DirectionScreen()    
#
#    
#key= None
#while key != 'q':
#    key=w.checkKey()
#    click=w.checkMouse()
#    #P.control(key)
#    if click != None:
#        print(click)
#
#
#w.close()  