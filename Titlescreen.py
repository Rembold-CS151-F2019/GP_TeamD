#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:39:53 2019

@author: elliegreenberg
"""

#trespasser strike



import graphics as g 

w=g.GraphWin("Final Game",1000,700)
w.setBackground("SkyBlue")


def TitleScreen():
    #Makes ground and Title
    Ground = g.Rectangle(g.Point(0,350), g.Point(1000,700))
    Ground.setFill("ForestGreen")
    Ground.draw(w)
    message1 = g.Text(g.Point(300,50), "Henrietta ")
    message5=g.Text(g.Point(300,100), "the hippopotamus's ")
    message2 = g.Text(g.Point(300,150),"wild run!")
    for  obj in [message1,message2,message5]:
                obj.setStyle("bold")
                obj.setTextColor("Indigo")
                obj.setSize(36)
                obj.setFace("courier")
                obj.draw(w)
                
    
    #Draws Henrietta's ears
    Ear1=g.Oval(g.Point(570,126), g.Point(600,196))
    Ear1.setFill('DarkSlateBlue')
    Ear1.draw(w)
    Ear2=g.Oval(g.Point(831,126), g.Point(863,196))
    Ear2.setFill('DarkSlateBlue')
    Ear2.draw(w)
    
    #Draws the ovals that make up the body and head of Henrietta
    Body = g.Oval(g.Point(400,350), g.Point(1100,1000))
    Body.setFill('DarkSlateBlue')
    Body.draw(w)
    Head=g.Oval(g.Point(510,145), g.Point(922,465))
    Head.setFill('DarkSlateBlue')
    Head.draw(w)
    
    #Makes the muzzle? snout? hippo face?
    Face = g.Polygon(g.Point(613,291), g.Point(567,430), g.Point(603,470),g.Point(824,470),g.Point(863,430),g.Point(802,291))
    Face.setFill('plum4')
    Face.draw(w)
    
    #NOSTRILSSSS
    Nostril1=g.Oval(g.Point(635,330), g.Point(665,370))
    Nostril1.setFill('DarkSlateBlue')
    Nostril2=g.Oval(g.Point(753,330), g.Point(783,370))
    Nostril2.setFill('DarkSlateBlue')
    Nostril1.draw(w)
    Nostril2.draw(w)
    
    #Draws the smile
    Smile=g.Polygon(g.Point(599,421), g.Point(622,446),g.Point(703,465),g.Point(745,461), g.Point(766,458),g.Point(786,454),g.Point(806,437),g.Point(827,416))
    Smile.setFill('Black')
    Smile.draw(w)
    
    #Draws Henriettas eyes and makes them less scary by adding in little reflection circles
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
                
    #Makes the log and leaf in the left corner
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
    
    #Draws the two clouds
    Cloud1 = g.Circle(g.Point(733,60), 50)
    Cloud2 = g.Circle(g.Point(693,60), 35)
    Cloud3 = g.Circle(g.Point(773,55), 30)
    Cloud4 = g.Circle(g.Point(800,55), 25)
    Cloud5 = g.Circle(g.Point(668,60), 20)
    Cloud6 = g.Circle(g.Point(784,81), 30)
    
    Cloud7 = g.Circle(g.Point(930,106), 45)
    Cloud8 = g.Circle(g.Point(960,115), 35)
    Cloud9 = g.Circle(g.Point(920,135), 30)
    
    for  obj in [Cloud1,Cloud2,Cloud3,Cloud4,Cloud5,Cloud6, Cloud7, Cloud8, Cloud9]:
                obj.setFill('snow')
                obj.setOutline("snow")
                obj.draw(w)
    
    #Draws the textbox and text that tells the user what to do next
    Textbox=g.Rectangle(g.Point(75,269), g.Point(385,488))
    Textbox.setFill("MediumPurple1")  
    Textbox.draw(w)
    message3=g.Text(g.Point(235,336), "Press the right arrow to continue") 
    message3.setSize(18)
    message3.draw(w)  
    message4=g.Text(g.Point(235,414), "Press E to exit at any time")    
    message4.setSize(18)
    message4.draw(w)  
    









