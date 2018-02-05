from model import *

system_1 = Body('f1', 'Grey', True)


tube1 = TonerTube(100, 20)

def printing(pages):
    print("Printing...")
    tube1.printing(pages)


def checkTnLvl():

    lvl = tube1.checkTnLvl()

    if lvl < 30:

        addToner()



def addToner():

    tube1.consumeToner(system_1.addToner())




