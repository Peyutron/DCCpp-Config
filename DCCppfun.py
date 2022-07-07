#!/usr/bin/env python

import fileinput
import sys

lines = ['#define USE_ONLY1_INTERRUPT', '#define DCCPP_DEBUG_MODE',\
'#define DCCPP_DEBUG_VERBOSE_MODE', '#define DCCPP_PRINT_DCCPP',\
'#define USE_EEPROM', '#define USE_TURNOUT',\
'#define USE_OUTPUT', '#define USE_SENSOR',\
'#define USE_S88', '#define USE_TEXTCOMMAND',\
'#define USE_ETHERNET_WIZNET_5100', '#define USE_ETHERNET_WIZNET_5200',\
'#define USE_ETHERNET_WIZNET_5500', '#define USE_ETHERNET_ENC28J60',\
'x?']

definestatus = ['On', 'On', 'On', 'On',\
                'On', 'On', 'On', 'On',\
                'On', 'On', 'On', 'On',\
                'On', 'On','On']


finalline = ['null'] * 15
startline = ['null'] * 15

filess = "DCCpp.h"


def FindLines():
    f = open(filess, "r+")
      
    l = f.readlines()

    c = 1
    modificada = list()
    for t in lines:
        modificada.append(('//' + t))

    print ('\nBuscando lineas desactivadas en ' + filess + '...\n')
    for i in l:    #i = linea de texto | revisando inactivos
        for text in modificada:
            if text in i:
                print ('linea ' + str(c) + ' ' + text.replace(" ", ""))
                activatefun(text)
        c+=1
    return definestatus        


def replacelines(file):

    f = open(file, "r+")
      
    l = f.readlines()
      
    # indice empieza por la linea 1
    c = 1
    for i in l:    #i = linea de texto | revisando inactivos
        for text in lines:
            if text in i:
                for data in range(len(lines)):
                    if text == lines[data - 1]:
                        if finalline[data -1] != 'null':
                            print ('linea elimina linea y añade nueva ' + finalline[data - 1])
                            l.pop(c - 1)    #Borramos la linea
                            l.insert(c -1, finalline[data -1] + '\n') #añade texto con salto de linea
                    
        c += 1

    f.truncate(0)
    f.seek(0)  

    f.writelines(l)
    f.close()

    print("Text succesfully replaced")


def check_clicked(opcion, estado):
    #print(estado.get())
    data = ""
    if estado.get() == 'On':
        data = lines[opcion]
    else:
        data = '//' + lines[opcion]
    finalline.pop(opcion)
    finalline.insert(opcion, data)
    print('check_clicked opcion: ' + str(opcion) + ' ' + finalline[opcion])    
    return data


def activatefun(texto):

    if texto == '//#define USE_ONLY1_INTERRUPT':
        definestatus[0] = 'Off'

    if texto == '//#define DCCPP_DEBUG_MODE':
        definestatus[1] = 'Off'

    if texto == '//#define DCCPP_DEBUG_VERBOSE_MODE':
        definestatus[2] = 'Off'

    if texto == '//#define DCCPP_PRINT_DCCPP':
        definestatus[3] = 'Off' 

    if texto == '//#define USE_EEPROM':
        definestatus[4] = 'Off'

    if texto == '//#define USE_TURNOUT':
        definestatus[5] = 'Off'

    if texto == '//#define USE_OUTPUT':
        definestatus[6] = 'Off'

    if texto == '//#define USE_SENSOR':
        definestatus[7] = 'Off'

    if texto == '//#define USE_S88':
        definestatus[8] = 'Off'

    if texto == '//#define USE_TEXTCOMMAND':
        definestatus[9] = 'Off'
    
    if texto == '//#define USE_ETHERNET_WIZNET_5100':
        definestatus[10] = 'Off'

    if texto == '//#define USE_ETHERNET_WIZNET_5200':
        definestatus[11] = 'Off'    

    if texto == '//#define USE_ETHERNET_WIZNET_5500':
        definestatus[12] = 'Off'

    if texto == '//#define USE_ETHERNET_ENC28J60':
        definestatus[13] = 'Off'

      


    