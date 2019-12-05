#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:56:23 2019

@author: elliegreenberg
"""
import graphics as g 
import Titlescreen

w=Titlescreen.w
w.setBackground("SkyBlue")


def EndScreen(scounter):
    #Makes the ground in the background (why it's created first)
    Ground = g.Rectangle(g.Point(0,350), g.Point(1000,700))
    Ground.setFill("ForestGreen")
    Ground.draw(w)
    #main congratulatory message
    message1 = g.Text(g.Point(150,100), "NICE JOB! ")
    message1.setStyle("bold")
    message1.setTextColor("Indigo")
    message1.setSize(36)
    message1.draw(w)
    
    #Makes henrietta and log, copied from title screen (except for the mouth)
    Ear1=g.Oval(g.Point(570,126), g.Point(600,196))
    Ear1.setFill('DarkSlateBlue')
    Ear1.draw(w)
    Ear2=g.Oval(g.Point(831,126), g.Point(863,196))
    Ear2.setFill('DarkSlateBlue')
    Ear2.draw(w)
    
    Body = g.Oval(g.Point(400,350), g.Point(1100,1000))
    Body.setFill('DarkSlateBlue')
    Body.draw(w)
    Head=g.Oval(g.Point(510,145), g.Point(922,465))
    Head.setFill('DarkSlateBlue')
    Head.draw(w)
    
    Face = g.Polygon(g.Point(613,291), g.Point(567,430), g.Point(603,470),g.Point(824,470),g.Point(863,430),g.Point(802,291))
    Face.setFill('plum4')
    Face.draw(w)
    
    Nostril1=g.Oval(g.Point(635,330), g.Point(665,370))
    Nostril1.setFill('DarkSlateBlue')
    Nostril2=g.Oval(g.Point(753,330), g.Point(783,370))
    Nostril2.setFill('DarkSlateBlue')
    Nostril1.draw(w)
    Nostril2.draw(w)
    
    Mouth=g.Circle(g.Point(655,427),25)
    Mouth.setFill('Black')
    Mouth.draw(w)
    
    Eye1=g.Oval(g.Point(653,210), g.Point(690,260))
    Eye1.setFill("black")
    Eye2=g.Oval(g.Point(731,210), g.Point(768,260))
    Eye2.setFill("black")
    Eye3=g.Circle(g.Point(756,229), 5)
    Eye3.setFill("White")
    Eye4=g.Circle(g.Point(680,229), 5)
    Eye4.setFill("White")
    for  obj in [Eye1,Eye2,Eye3,Eye4]:
                obj.draw(w)
                
    
    Log1= g.Rectangle(g.Point(0,564), g.Point(246,700))
    Log2=g.Circle(g.Point(246,632),68)
    Log3=g.Circle(g.Point(246,632),48)
    Log4=g.Circle(g.Point(246,632),28)
    for obj in [Log1,Log2, Log3,Log4]:
                obj.setFill('sienna4')
                obj.setOutline('Black')
                obj.setWidth(4)
                obj.draw(w)
    
    Leaf=g.Oval(g.Point(115,502), g.Point(132,529))
    Leaf.setFill('green')
    Leaf.draw(w)
    Stem=g.Rectangle(g.Point(122,526), g.Point(132,566))
    Stem.setFill('sienna4')
    Stem.draw(w)
    
    #makes quote box and text for henrietta to be saying "phew"
    Textbox=g.Polygon(g.Point(264,347), g.Point(451,347),g.Point(451,380),g.Point(600,425),g.Point(451,420),g.Point(264,420))
    
    Textbox.setFill("White")  
    Textbox.draw(w)
    message3=g.Text(g.Point(355,375), "Phew!") 
    message3.setSize(25)
    message3.draw(w)  
      
    #tells results of the game and instructions to exit
    message5 = g.Text(g.Point(220,250), f"You dodged {scounter} objects")
    message5.setSize(30)
    message5.setFace("courier")
    message5.draw(w)  
    message5 = g.Text(g.Point(694,660), 'Thanks for playing! Press E to exit')
    message5.setSize(30)
    message5.setStyle("bold")
    message5.setTextColor("White")
    message5.draw(w)  
#EndScreen()
