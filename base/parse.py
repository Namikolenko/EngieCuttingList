def ParseWeldolet(otherstr):
    if otherstr == '3/8 inches':
        otherstr = 'weldolet_diam1'
    if otherstr == '1/2 inches':
        otherstr = 'weldolet_diam2'
    if otherstr == '3/4 inches':
        otherstr = 'weldolet_diam3'
    if otherstr == '1 inches':
        otherstr = 'weldolet_diam4'
    if otherstr == '1-1/2 inches':
        otherstr = 'weldolet_diam5'
    if otherstr == '2 inches':
        otherstr = 'weldolet_diam6'
    if otherstr == '3 inches':
        otherstr = 'weldolet_diam7'
    if otherstr == '4 inches':
        otherstr = 'weldolet_diam8'
    if otherstr == '6 inches':
        otherstr = 'weldolet_diam9'
    if otherstr == '8 inches':
        otherstr = 'weldolet_diam10'
    if otherstr == '10 inches':
        otherstr = 'weldolet_diam11'
    if otherstr == '12 inches':
        otherstr = 'weldolet_diam12'
    if otherstr == '14 inches':
        otherstr = 'weldolet_diam13'
    if otherstr == '16 inches':
        otherstr = 'weldolet_diam14'
    if otherstr == '18 inches':
        otherstr = 'weldolet_diam15'
    if otherstr == '20 inches':
        otherstr = 'weldolet_diam16'
    if otherstr == '24 inches':
        otherstr = 'weldolet_diam17'
    return otherstr


def ParseWeldingBend(string):
    if string == 'LR90R':
        return 'L_R_90_R'
    elif string == 'LR45B':
        return 'L_R_45_B'
    elif string == 'LR180':
        return 'L_R_180'
    elif string == 'SR180':
        return 'S_R_180'
    elif string == 'SR90A':
        return 'S_R_90_A'
    else:
        return string


def ParseValve(string):
    if string == 'GateValve150ibs':
        return 'valve_150ibs'
    elif string == 'GateValve300ibs':
        return 'valve_300ibs'
    elif string == 'BallValve150ibs':
        return 'ball_150ibs'
    elif string == 'BallValve300ibs':
        return 'ball_300ibs'
    elif string == 'CheckValve150ibs':
        return 'check_150ibs'
    elif string == 'CheckValve300ibs':
        return 'check_300ibs'
    else:
        return string


def ParseFlange212(string):
    if string == 'PN2.5':
        return 'PN212'
    else:
        return string
