#!/usr/bin/python
import time

class Body(object):

    switch_On = False
    tonerTube = 0


    def __init__(self, sys_id, color, is_rfid):

        self.sys_id = sys_id
        self.color = color
        self.is_rfid = is_rfid

        # SwitchesOn the system
    def start(self):
        self.switch_On = True

        return self.switch_On, print('Status: Working...\n')

        # Getting system's info
    def get_info(self):
        if self.is_rfid == True:
            rfid = 'Yes'
        else:
            rfid = 'No'

        info = "--SYSTEM-INFO--"+ "\nID:"+ self.sys_id+"\nColor: "+self.color + "\nRFID: "+ rfid

        return print(info)

    def checkTonelLvl(self, tonerTube):
        pass



    def addToner(self):

        tonerOut = 15


        return tonerOut



class TonerTube:

    def __init__(self, capacity, tonerLvl):

        self.tonerLvl = tonerLvl

        self.capacity = capacity

    def printing(self, pages):

        weight = pages * 2

        self.tonerLvl = self.tonerLvl - weight

        return print("After printing toner level is : "+ str(self.tonerLvl))

    def checkTnLvl(self):


        return self.tonerLvl


    def consumeToner(self, tonerIn):
        print("Adding toner....\n")
        value = (self.capacity/100)*70

       # tonerLvl = 0

        tube_is_full = False

        while self.tonerLvl <= int(value):

            self.tonerLvl = self.tonerLvl+ tonerIn
            time.sleep(1)

            print(str(self.tonerLvl)+ "g\n")





            if self.tonerLvl >= int(value):


                return print("...Tube is full\n")

