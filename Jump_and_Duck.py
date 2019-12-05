#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:26:57 2019

@author: elliegreenberg
"""
import graphics as g 
import Titlescreen


w=Titlescreen.w
w.setBackground("SkyBlue")

#Ground = g.Rectangle(g.Point(0,450), g.Point(1000,700))
#Ground.setFill("ForestGreen")
#Ground.draw(w)

class Hen:
    def __init__(self, w,x,y,r):
        self.w=w
        self.x=x
        self.y=y
        self.r=r
        self.Create()
        self.oldstate=0
        self.newstate=None
    def getr(self):
        return self.r
    def Create(self):
        self.body=g.Circle(g.Point(self.x,self.y), self.r)
        self.body.setFill('DarkSlateBlue')
        self.body.draw(self.w)
        

    def updatestate(self):
        if  self.oldstate==0 and self.newstate==1:
            self.body.undraw()
            self.body=g.Circle(g.Point(300,308), 70)
            self.body.setFill('DarkSlateBlue')
            self.body.draw(w)
            self.oldstate=self.newstate
        elif self.oldstate==0 and self.newstate==-1:
            self.body.undraw()
            self.body=g.Circle(g.Point(300,416), 34)
            self.r = 34
            self.body.setFill('DarkSlateBlue')
            self.body.draw(w)
            self.oldstate=self.newstate
        elif self.oldstate==-1 and self.newstate==0:
            self.body.undraw()
            self.r = 70
            self.Create()
            self.oldstate=self.newstate
        elif self.oldstate==1 and self.newstate==0:
            self.body.undraw()
            self.r = 70
            self.Create()
            self.oldstate=self.newstate

    def control(self, key):
        if key=='Up':
            if self.oldstate==0:
                self.newstate=1
            elif self.oldstate==-1:
                self.newstate=0
        elif key=="Down":
            if self.oldstate==0:
                self.newstate=-1
            elif self.oldstate==1:
                self.newstate=0

#H=Hen(w,300,380,70)     

#
#key= None
#
#while key != 'e':
#    
#    key=w.checkKey()
#    H.control(key)
#    H.updatestate()
#    #g.update(30)
#
#w.close()  