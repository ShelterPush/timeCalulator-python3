#! python3
# timeCalculator.py - Program to calculate the amount of time between times
#  to one decimal point

import sys

def timeInput():
    while True:
        print('Use the following format: HH:MM')
        print('To use 12-hour time, use: HH:MM XM')
        inputTime = input()
        if ':' in inputTime:
            if len(inputTime) > 3 and len(inputTime) <= 8:
                if inputTime[1] == ':':
                    inputTime = '0' + inputTime
                try:
                    inputHour = int(inputTime[0:2])
                    inputMinute = int(inputTime[3:5])
                except ValueError:
                    continue
                if len(inputTime) > 5:
                    if inputTime[-2].lower() == 'p':
                        if inputHour <= 11:
                            inputHour += 12
                    elif inputTime[-2].lower() == 'a':
                        if inputHour == 12:
                            inputHour = 0
                    else:
                        continue
                if inputHour >= 0 and inputHour <= 23:
                    if inputMinute >= 0 and inputMinute <= 59:
                        break
    timeMinutes = (inputHour * 60) + inputMinute
    return timeMinutes

print('This program calculates a decimal value of how many hours are between two times in the same day.\n')
while True:
    print('Input the starting time.')
    startTime = timeInput()
    print()
    print('Input the ending time.')
    endTime = timeInput()
    timeDifference = endTime - startTime
    print()
    if round(0.25,1) == 0.2:
        binaryFix = 0.01 # round() rounds 0.25 to 0.2 without this
    else:
        binaryFix = 0
    diffHours = round(timeDifference/60+binaryFix, 1) # added +binaryFix to fix the round() issues
    print(str(diffHours) + ' hours')
    print()
    # exit code
    while True:
        print('Press enter to do this again, or type q and press enter to exit.')
        exitInput = input()
        if exitInput.lower() == 'q':
            sys.exit()
        elif exitInput == '':
            break
        else:
            continue
