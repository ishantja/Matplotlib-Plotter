# this function calculates the various unknown parameters required for propeller efficiency calculation

import pandas as pd
import numpy as np

def calculateData():
    X = pd.read_excel('motordata.xlsx')
    # int(mc) = input('Enter value of motor constant: ')
    # int(Kv) = input('Enter Kv rating of the motor: ')
    mc = 8.3
    Kv = 430

    X['pin'] = X.I * X.V
    X['torque'] = (mc / Kv) * X.I
    X['pout'] = (2*3.14*X.RPM*X.torque)/60
    X['emot'] = X.pout/X.pin
    X['eprop'] = X.Thrust/X.pout
    X['esys'] = X.eprop * X.emot
    return (X)



