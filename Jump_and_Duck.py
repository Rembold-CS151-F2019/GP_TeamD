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

#Making the class of Henrietta
class Hen:
    def __init__(self, w,x,y,r):
        self.w=w
        self.x=x
        self.y=y
        self.r=r
        self.Create() 
        self.oldstate=0 #starts with henrietta regular size and on the ground
        self.newstate=None #user hasn't input any commands to make her jump or duck yet so no new state
        
    def getr(self):
        return self.r
    def Create(self): #makes Henrietta
        self.body=g.Circle(g.Point(self.x,self.y), self.r)
        self.body.setFill('DarkSlateBlue')
        self.body.draw(self.w)
        
   
    def updatestate(self):
        '''
        This changes Henrietta's size and location based on what she was before (what her oldstate was).
        (prevents a small, ducking circle from being able to jump, has to return to regular state first and then jump 
        after a second Up click)
        If ducking, the state is -1, if regular, the state is zero, and if jumping, the state is 1.
        To change from state to state, this first undraws the old Henrietta and then draws a new one (newstate).
        '''
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
        '''This sets the status of the states based on what the user imputs. For example, If the user
        presses Up, and henrietta was ducking (oldstate=-1), it makes her her regular size (newstate=0).
        '''
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


  
