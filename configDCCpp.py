#!/usr/bin/env python

from pathlib import Path
from DCCppfun import *
from DCCppCurrent import *
from ShieldsFun import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messages
from tkinter import filedialog



tk = Tk()

puertofinal = StringVar (tk, value = "2560")
ssidfinal = StringVar (tk, value = "WIFI network name")
psswfinal = StringVar (tk, value = "************")
hostfinal = StringVar (tk, value = "dcchost")


varuseonly1 = StringVar()
varuseonly1.set('On')
varuseprint = StringVar()
varuseprint.set('On')
varusedebug = StringVar()
varusedebug.set('On')
varusedebugvervose = StringVar()
varusedebugvervose.set('On')
varuseeeprom = StringVar()
varuseeeprom.set('On')
varuseturnout = StringVar()
varuseturnout.set('On')
varuseoutput = StringVar()
varuseoutput.set('On')
varusesensor = StringVar()
varusesensor.set('On')
varuses88 = StringVar()
varuses88.set('On')
varusetextcommand = StringVar()
varusetextcommand.set('On')
varusewiznet5100 = StringVar()
varusewiznet5100.set('On')
varusewiznet5200 = StringVar()
varusewiznet5200.set('On')
varusewiznet5500 = StringVar()
varusewiznet5500.set('On')
varuseenc28j60 = StringVar()
varuseenc28j60.set('On')

varEmergencyStop = StringVar()
varEmergencyStop.set('On')
varEmergencyStopStateLOW = StringVar()
varEmergencyStopStateLOW.set('On')
varEmergencyStopStateHIGH = StringVar()
varEmergencyStopStateHIGH.set('On')
varE_BOOSTER_ENABLE = StringVar()
varE_BOOSTER_ENABLE.set('On')

filename = 'null'   
fileConfig = 'DCCpp.h'
fileShield = 'null'


def SelecionaArchivo(opcion):
    global filename    
    filename = filedialog.askopenfilename(initialdir='/home/peyu/Arduino/libraries/CommandStation-EX', title="Selecciona un archivo", filetypes=(("DCCEX", "*.h"),("none", "")))
    print (filename)
    if opcion == 0:
        global fileConfig
        fileConfig = filename
    elif opcion == 1:
        global fileShield
        fileShield = filename


def Actualiza():
    global fileConfig
    print(fileConfig)
    if fileConfig != 'null':
        listaestado = replacelines(fileConfig)
        #cargaDCCpph(listaestado)
    else:
        messages.showinfo(message="No seleccionaste archivo", title="Error")

def ActualizaCurrent():
    global fileConfig
    print(fileConfig)
    if fileConfig != 'null':
        listacurrentestado = ReplaceCurrentLines()
        #cargaDCCpph(listaestado)
    else:
        messages.showinfo(message="No seleccionaste archivo", title="Error")



def LoadData(listaestado):
    print(listaestado)
    varuseonly1.set(listaestado[0])
    varusedebug.set(listaestado[1])
    varusedebugvervose.set(listaestado[2])
    varuseprint.set(listaestado[3])
    varuseeeprom.set(listaestado[4])
    varuseturnout.set(listaestado[5])
    varuseoutput.set(listaestado[6])
    varusesensor.set(listaestado[7])
    varuses88.set(listaestado[8])
    varusetextcommand.set(listaestado[9])
    varusewiznet5100.set(listaestado[10])
    varusewiznet5200.set(listaestado[11])
    varusewiznet5500.set(listaestado[12])
    varuseenc28j60.set(listaestado[13])


def LoadCurrentData(listacurrentestado):    
    varEmergencyStop.set(listacurrentestado[0])
    varEmergencyStopStateLOW.set(listacurrentestado[1])
    varEmergencyStopStateHIGH.set(listacurrentestado[2])
    varE_BOOSTER_ENABLE.set(listacurrentestado[3])

def ActualizaShield():
    global fileShield
    print(fileShield)
    if fileShield != 'null':
        actualizaShield(fileShield, dataShields)
    else:
        messages.showinfo(message="No seleccionaste archivo", title="Error")


pestania = ttk.Notebook(tk)
pestania.pack(fill='both', expand= 'yes')
miFrame = ttk.Frame(tk)
CM = ttk.Frame(tk)
pestania.add(miFrame, text='Config.h')
pestania.add(CM, text='CurrentMonitor.h')

#miFrame.pack(expand=1)


tk.geometry("400x570")
tk.title("Configurador DCCppS88")
tk.resizable(0, 0)

def cargaDCCpph():
    listaestado = FindLines()
    LoadData (listaestado)
    FindCurrentLines()

cargaDCCpph()       

#seleccionaArchivoButton = Button(miFrame, text = 'Seleccionar\narchivo', command=lambda: SelecionaArchivo(0))
#seleccionaArchivoButton.grid(column=1, row=15, pady=[15,0])

enviaArchivoButton = Button(miFrame, text = 'Actualizar\narchivo', command=lambda: Actualiza())
enviaArchivoButton.grid(column=2, row=15, pady=[15,0])

useOnly1 = Label(miFrame, text="Use Only 1 Interrupt:")
useOnly1.grid(column=1, row=1, sticky="W", padx =[30,0], pady=[10,0])

activaOnly1 = Checkbutton(miFrame, textvariable=varuseonly1, 
    variable=varuseonly1, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked(0, varuseonly1))
activaOnly1.grid(column=2, row=1, sticky="W", padx =[20,0], pady=[10,0])

useDebugMode = Label(miFrame, text = 'Debug mode:')
useDebugMode.grid(column=1, row=2, sticky="W", padx =[30,0], pady=[10,0])

activaDebugMode = Checkbutton(miFrame, textvariable=varusedebug, 
    variable=varusedebug, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(1, varusedebug))
activaDebugMode.grid(column=2, row=2, sticky="W", padx =[20], pady=[10,0])

useDebugVervoseMode = Label(miFrame, text='Debug vervose mode:')
useDebugVervoseMode.grid(column=1, row=3, sticky="W", padx =[30,0], pady=[10,0])

activaDebugVervose = Checkbutton(miFrame, textvariable=varusedebugvervose, 
    variable=varusedebugvervose, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(2, varusedebugvervose))
activaDebugVervose.grid(column=2, row=3, sticky="W", padx =[20,0], pady=[10,0]) 

useDCCPrint = Label(miFrame, text="DCCPP PRINT DCCPP:")
useDCCPrint.grid(column=1, row=4, sticky="W", padx =[30,0], pady=[10,0])

activaDCCPrint = Checkbutton(miFrame, textvariable=varuseprint, 
    variable=varuseprint, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked(3, varuseprint))
activaDCCPrint.grid(column=2, row=4, sticky="W", padx =[20,0], pady=[10,0])

useEeprom = Label(miFrame, text="EEPROM:")
useEeprom.grid(column=1, row=5, sticky="W", padx =[30,0], pady=[10,0])

activaEeprom = Checkbutton(miFrame, textvariable=varuseeeprom, 
    variable=varuseeeprom, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(4, varuseeeprom))
activaEeprom.grid(column=2, row=5, sticky="W", padx =[20,0], pady=[10,0])

useTurnout = Label(miFrame, text='Use Turnout:')
useTurnout.grid(column=1, row=6, sticky="W", padx =[30,0], pady=[10,0])

activaTurnout = Checkbutton(miFrame, textvariable=varuseturnout, 
    variable=varuseturnout, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(5, varuseturnout))
activaTurnout.grid(column=2, row=6, sticky="W", padx =[20,0], pady=[10,0])

useOutput = Label(miFrame, text="Use Output:")
useOutput.grid(column=1, row=7, sticky="W", padx =[30,0], pady=[10,0])

activaOutput = Checkbutton(miFrame, textvariable=varuseoutput, 
    variable=varuseoutput, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(6, varuseoutput))
activaOutput.grid(column=2, row=7, sticky="W", padx =[20,0], pady=[10,0])

useSensor = Label(miFrame, text="Use Sensor:")
useSensor.grid(column=1, row=8, sticky="W", padx =[30,0], pady=[10,0])

activaSensor = Checkbutton(miFrame, textvariable=varusesensor, 
    variable=varusesensor, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(7, varusesensor))
activaSensor.grid(column=2, row=8, sticky="W", padx =[20,0], pady=[10,0])

useS88 = Label(miFrame, text = 'Use S88:')
useS88.grid(column=1, row=9, sticky="W", padx =[30,0], pady=[10,0])

activaS88 = Checkbutton(miFrame, textvariable=varuses88, 
    variable=varuses88, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(8, varuses88))
activaS88.grid(column=2, row=9, sticky="W", padx =[20,0], pady=[10,0])

useTextcommand = Label(miFrame, text="Use TextCommand:")
useTextcommand.grid(column=1, row=10, sticky="W", padx =[30,0], pady=[10,0])

activaTextCommand = Checkbutton(miFrame, textvariable=varusetextcommand, 
    variable=varusetextcommand, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(9, varusetextcommand))
activaTextCommand.grid(column=2, row=10, sticky="W", padx =[20,0], pady=[10,0])

useWiznet5100 = Label(miFrame, text = 'Use Ethernet wiznet 5100:')
useWiznet5100.grid(column=1, row=11, sticky="W", padx =[30,0], pady=[10,0])

activaWiznet5100 = Checkbutton(miFrame, textvariable=varusewiznet5100, 
    variable=varusewiznet5100, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(10, varusewiznet5100))
activaWiznet5100.grid(column=2, row=11, sticky="W", padx =[20,0], pady=[10,0])

useWiznet5200 = Label(miFrame, text = 'Use Ethernet wiznet 5200:')
useWiznet5200.grid(column=1, row=12, sticky="W", padx =[30,0], pady=[10,0])

activaWiznet5200 = Checkbutton(miFrame, textvariable=varusewiznet5200, 
    variable=varusewiznet5200, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(11, varusewiznet5200))
activaWiznet5200.grid(column=2, row=12, sticky="W", padx =[20,0], pady=[10,0])


useWiznet5500 = Label(miFrame, text = 'Use Ethernet wiznet 5500:')
useWiznet5500.grid(column=1, row=13, sticky="W", padx =[30,0], pady=[10,0])

activaWiznet5500 = Checkbutton(miFrame, textvariable=varusewiznet5500, 
    variable=varusewiznet5500, 
    onvalue='On', 
    offvalue='Off',
    command=lambda:check_clicked(12, varusewiznet5500))
activaWiznet5500.grid(column=2, row=13, sticky="W", padx =[20,0], pady=[10,0])

useENC28J60 = Label(miFrame, text="Use Ethernet ENC28J60:")
useENC28J60.grid(column=1, row=14, sticky="W", padx =[30,0], pady=[10,0])

activaENC28J60 = Checkbutton(miFrame, textvariable=varuseenc28j60, 
    variable=varuseenc28j60, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked(13, varuseenc28j60))
activaENC28J60.grid(column=2, row=14, sticky="W", padx =[20,0], pady=[10,0])




enviaArchivoButton = Button(CM, text = 'Actualizar\narchivo', command=lambda: ActualizaCurrent())
enviaArchivoButton.grid(column=2, row=15, pady=[15,0])

useEmergencyStop = Label(CM, text="define EmergencyStop A5:")
useEmergencyStop.grid(column=1, row=1, sticky="W", padx =[30,0], pady=[10,0])

activaEmergencyStop = Checkbutton(CM, textvariable=varEmergencyStop, 
    variable=varEmergencyStop, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked_current(0, varEmergencyStop))
activaEmergencyStop.grid(column=2, row=1, sticky="W", padx =[20,0], pady=[10,0])

useEmergencyStopState_LOW = Label(CM, text="define EmergencyStopState LOW:")
useEmergencyStopState_LOW.grid(column=1, row=2, sticky="W", padx =[30,0], pady=[10,0])

activaEmergencyStopState_LOW = Checkbutton(CM, textvariable=varEmergencyStopStateLOW, 
    variable=varEmergencyStopStateLOW, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked_current(1, varEmergencyStopStateLOW))
activaEmergencyStopState_LOW.grid(column=2, row=2, sticky="W", padx =[20,0], pady=[10,0])

useEmergencyStopState_HIGH = Label(CM, text="define EmergencyStopState HIGH:")
useEmergencyStopState_HIGH.grid(column=1, row=3, sticky="W", padx =[30,0], pady=[10,0])

activaEmergencyStopState_HIGH = Checkbutton(CM, textvariable=varEmergencyStopStateHIGH, 
    variable=varEmergencyStopStateHIGH, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked_current(2, varEmergencyStopStateHIGH))
activaEmergencyStopState_HIGH.grid(column=2, row=3, sticky="W", padx =[20,0], pady=[10,0])

useE_BOOSTER_ENABLE = Label(CM, text="define EmergencyStop A5:")
useE_BOOSTER_ENABLE.grid(column=1, row=4, sticky="W", padx =[30,0], pady=[10,0])

activaE_BOOSTER_ENABLE = Checkbutton(CM, textvariable=varE_BOOSTER_ENABLE, 
    variable=varE_BOOSTER_ENABLE, 
    onvalue='On', 
    offvalue='Off', 
    command=lambda:check_clicked_current(3, varE_BOOSTER_ENABLE))
activaE_BOOSTER_ENABLE.grid(column=2, row=4, sticky="W", padx =[20,0], pady=[10,0])

"""
#ShieldSelect
textoshieldSel = Label(MSHIELD, text = 'Shield:')
textoshieldSel.grid(column=1, row=1, sticky="W", padx =[10,0], pady=[10,0])

varshieldSel = StringVar()
shieldSelect = Spinbox(MSHIELD, textvariable=varshieldSel,
    values=shieldnames, 
    command=lambda:loadvalues(varshieldSel, varTrack), width=30)
shieldSelect.grid(column=2, row=1, sticky="W",padx=[10,0], pady=[10,0])

#trackSelect
textoTrack = Label(MSHIELD, text = 'Vía:')
textoTrack.grid(column=1, row=2, sticky="W", padx =[10,0], pady=[10,0])

varTrack = StringVar()
trackSelect = Spinbox(MSHIELD, textvariable=varTrack, 
    values=typeTrack, 
    command=lambda:loadvalues(varshieldSel, varTrack))
trackSelect.grid(column=2, row=2, sticky="W",padx=[10,0], pady=[10,0])

#powerPin
varPowerPin = StringVar()
textoPowerPin = Label(MSHIELD, text="Pin de encendido:")
textoPowerPin.grid(column=1, row=3, sticky="W", padx =[10,0], pady=[10,0])

cambiarPowerPin = Entry(MSHIELD, textvariable = varPowerPin, width=15)
cambiarPowerPin .grid(column=2, row=3, sticky="W", padx =[10,0], pady=[10,0])

#signalPin
varSignalPin = StringVar()
textoSignalPin = Label(MSHIELD, text="Pin de señal:")
textoSignalPin.grid(column=1, row=4, sticky="W", padx =[10,0], pady=[10,0])

cambiarSignalPin = Entry(MSHIELD, textvariable = varSignalPin)
cambiarSignalPin.grid(column=2, row=4, sticky="W", padx =[10,0], pady=[10,0])

#signalPin2
varSignalPin2 = StringVar()
textoSignalPin2 = Label(MSHIELD, text="Pin de señal 2:")
textoSignalPin2.grid(column=1, row=5, sticky="W", padx =[10,0], pady=[10,0])

cambiarSignalPin2 = Entry(MSHIELD, textvariable = varSignalPin2)
cambiarSignalPin2.grid(column=2, row=5, sticky="W", padx =[10,0], pady=[10,0])

#brakePin
varBrakePin = StringVar()
textoBrakePin = Label(MSHIELD, text="Pin brake (Freno):")
textoBrakePin.grid(column=1, row=6, sticky="W", padx =[10,0], pady=[10,0])

cambiarBrakePin = Entry(MSHIELD, textvariable = varBrakePin)
cambiarBrakePin.grid(column=2, row=6, sticky="W", padx =[10,0], pady=[10,0])

#currentPin
varCurrentPin = StringVar()
textoCurrentPin = Label(MSHIELD, text="Pin senor:")
textoCurrentPin.grid(column=1, row=7, sticky="W", padx =[10,0], pady=[10,0])

cambiarCurrentPin = Entry(MSHIELD, textvariable = varCurrentPin)
cambiarCurrentPin.grid(column=2, row=7, sticky="W", padx =[10,0], pady=[10,0])

#senseFactor
varFactorSensor = StringVar()
textoSenseFactor = Label(MSHIELD, text="Factor sensibilidad:")
textoSenseFactor.grid(column=1, row=8, sticky="W", padx =[10,0], pady=[10,0])

cambiarSenseFactor = Entry(MSHIELD, textvariable = varFactorSensor)
cambiarSenseFactor.grid(column=2, row=8, sticky="W", padx =[10,0], pady=[10,0])

#miliampsTrip
varTripMiliamps = StringVar()
textoMiliampsTrip = Label(MSHIELD, text="Trip miliamperios:")
textoMiliampsTrip.grid(column=1, row=9, sticky="W", padx =[10,0], pady=[10,0])

cambiarMiliampsTrip = Entry(MSHIELD, textvariable = varTripMiliamps)
cambiarMiliampsTrip.grid(column=2, row=9, sticky="W", padx =[10,0], pady=[10,0])

#faultPin
varDefaultpin = StringVar()
textoDefaultPin = Label(MSHIELD, text="Pin por defecto:")
textoDefaultPin.grid(column=1, row=10, sticky="W", padx =[10,0], pady=[10,0])

cambiarDefaultPin = Entry(MSHIELD, textvariable = varDefaultpin)
cambiarDefaultPin.grid(column=2, row=10, sticky="W", padx =[10,0], pady=[10,0])
"""

tk.mainloop()
