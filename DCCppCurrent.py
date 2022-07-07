#!/usr/bin/env python

import fileinput
import sys

currentlines = ['#define EmergencyStop A5', '#define EmergencyStopState LOW', \
'#define EmergencyStopState HIGH', '#define E_BOOSTER_ENABLE true', \
'x?' ]

definestatus = ['On', 'On', 'On', 'On', 'On', 'On', 'On', 'On']

finalcurrentline = ['null'] * 8

currentFile = 'CurrentMonitor.h'


def FindCurrentLines():
    f = open(currentFile, "r+")
      
    l = f.readlines()

    c = 1
    modificada = list()
    for t in currentlines:
        modificada.append(('//' + t))

    print ('\nBuscando lineas desactivadas en ' + currentFile + '...\n')
    for i in l:    #i = linea de texto | revisando inactivos
        for text in modificada:
            if text in i:
                print ('linea ' + str(c) + ' ' + text.replace(" ", ""))
                ActivateCurrent(text)
        c+=1
    return definestatus 

def ReplaceCurrentLines():

    f = open(currentFile, "r+")
      
    l = f.readlines()
      
    # indice empieza por la linea 1
    c = 1
    for i in l:    #i = linea de texto | revisando inactivos
        for text in currentlines:
            if text in i:
                for data in range(len(currentlines)):
                    if text == currentlines[data - 1]:
                        if finalcurrentline[data -1] != 'null':
                            print ('linea elimina linea y añade nueva ' + finalcurrentline[data - 1])
                            l.pop(c - 1)    #Borramos la linea
                            l.insert(c -1, finalcurrentline[data -1] + '\n') #añade texto con salto de linea
                    
        c += 1

    f.truncate(0)
    f.seek(0)  

    f.writelines(l)
    f.close()

    print("Text succesfully replaced")


def check_clicked_current(opcion, estado):
    #print(estado.get())
    data = ""
    if estado.get() == 'On':
        data = currentines[opcion]
    else:
        data = '//' + currentines[opcion]
    finalcurrentline.pop(opcion)
    finalcurrentline.insert(opcion, data)
    print('check_clicked opcion: ' + str(opcion) + ' ' + finalcurrentline[opcion])    
    return data

def ActivateCurrent(texto):
	if texto == '//#define EmergencyStop A5':
		definestatus[0] = 'Off'
	if texto == '//#define EmergencyStopState LOW':
		definestatus[1] = 'Off'
	if texto == '//#define  EmergencyStopState HIGH':
		definestatus[2] = 'Off'
	if texto == '//#define E_BOOSTER_ENABLE true':
		definestatus[3] = 'Off'                   