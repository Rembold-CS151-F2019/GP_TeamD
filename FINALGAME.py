#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:07:24 2019

@author: brooksdanielson
"""
#importing all the code from Ellie and Nikki
import graphics as g
import Directions
import Endscreen
import Cloud_Log_Hit
import Jump_and_Duck
import Titlescreen
import random

w = Titlescreen.w #keeps everything on the same screen instead of multiple screens popping up
obj = [] #an object list to keep track of what is on the screen 

def create(): #function that randomly generates clouds and logs for the game
   r = [0,1]  
   c = random.choice(r)
   if c == 0:
    
       obj.append(Cloud_Log_Hit.Log(w,1050,450)) #adding to the obj list
   elif c == 1:
 
       obj.append(Cloud_Log_Hit.Cloud(w,1050,450))
   if not gameover:
       w.after(3000,create) #if the game isn't done, continue to create clouds and logs every 3 seconds
   

def main():
    global gameover #global gameover variable, keep track of if the game is still going
    Titlescreen.TitleScreen() #calls the title screen
    key = None
    counter = 0 #keeps track of how many times the right arrow has been clicked
    scounter=0
    gameover=False
    while key != 'e': #the game will exit, gameover=True, if e is pressed at any time   
        key=w.checkKey()
        if key == "Right" and counter < 2: #added so game won't break if you press the arrow too many times
            counter += 1
            for item in w.items[:]: #undraws title screen if the right arrow has been clicked once
                item.undraw()
            if counter == 1:
                Directions.DirectionScreen() #calls directions screen
                key = None #resets key to keep track of what the user presses
            if counter == 2:
                w.setBackground("SkyBlue") #draws the background for the game
                Ground = g.Rectangle(g.Point(0,450), g.Point(1000,700))
                Ground.setFill("ForestGreen")
                Ground.draw(w)
                message0=g.Text(g.Point(500,660), "Press Enter to start") #message for the user
                message0.setSize(20)
                message0.draw(w)
                global H 
                H = Jump_and_Duck.Hen(w,300,380,70)#creates Henrietta object, draws her too
                key = None
                
        if key == "Return": #if enter is pressed, the game starts
            message0.undraw() #undraws the press enter to start
            create() #calls the create function so a log or cloud will start rolling accross the screen
            key = None #resets key back to None to check what the player presses
            while key!= 'e' and not gameover: #the user can either press e or run into an object to end the game
                key=w.checkKey()
                H.control(key)#checks what key is pressed 
                H.updatestate() #updates Henrietta's state on the screen
                for o in obj.copy(): #iterates through the objects on screen, the obj list, checking to see if they hit Henrietta
                    if o.hit(H):
                        gameover=True #ends the game if she's been hit
                    if o.offscreen():
                        scounter +=1 #if the object is off screen, the score is incremented and the object is removed from the list
                        #that checks if it hits Henrietta
                        obj.remove(o)
                g.update(30) #graphics updating everthing on the screen
        if gameover:
            break #breaks out of loop if game is over
    for item in w.items[:]: #undraws everything on the game screen
        item.undraw()
    if scounter>0:
        scounter+=1 #accounts for the last object the user doged but has not left the screen yet
    Endscreen.EndScreen(scounter) #calls endscreen and inputs the number of objects doged
    while key!= 'e': #when the user presses e the endscreen will be undrawn and the window closes
        key=w.checkKey()
        for o in obj:
            o.obj.undraw()
            obj.remove(o)
            
             
               
       
           
                
    
                
            
    w.close()
                
    
if __name__ == '__main__':
    main() #runs the game when you run the script
