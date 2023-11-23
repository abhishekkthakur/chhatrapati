import tkinter as tk
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *

## Creating a new tkinter window
master = tk.Tk()
master.title('Gibbs energy calculator')
master.geometry('800x600')             ## First is width

## Function to calculate the Gibbs energy
def gibbsCalculate():
    tempElemA = str(elemA.get())
    tempElemB = str(elemB.get())
    T = float(temp.get())
    if (len(interL0.get()) == 0):
        L0 = 0
    else:
        L0 = float(interL0.get())
    if (len(interL1.get()) == 0):
        L1 = 0
    else:
        L1 = float(interL1.get())
    if (len(interL2.get()) == 0):
        L2 = 0
    else:
        L2 = float(interL2.get())
    R = 8.314
    if (tempElemA == 'Cr'):
        if (T <= 2180):
            g0ElemA = -8856.94 + 157.48 * T - 26.908 * T * math.log(T) + 1.89435E-3 *T**2 - 1.47721E-6 * T**3 + 139250 * T**(-1)
        else:
            g0ElemA = -34869.344 + 344.18 * T - 50 * T * math.log(T) - 2885.26E29 * T**(-9)
    elif (tempElemA == 'W'):
        if (T <= 3695):
            g0ElemA = -7646.311 + 130.4 * T - 24.1 * T * math.log(T) - 1.936E-3 * T**2 + 0.207E-6 * T**3 + 44500 * T**(-1) - 0.0533E-9 * T**4
        else:
            g0ElemA = -82868.801 + 389.362335 * T - 54 * T * math.log(T) + 1528.621E30 * T**(-9)
    else:
        if (T <= 1300):
            g0ElemA = -7285.889 + 119.139857 * T - 23.7592624 * T * math.log(T) - 2.623033E-3 * T**2 + 0.170109E-6 * T**3 -3293 * T**(-1)
        elif (T <= 2500):
            g0ElemA = -22389.955 + 243.88676 * T - 41.137088 * T * math.log(T) + 6.167572E-3 * T**2 - 0.655136E-6 * T**3 + 2429586 * T**(-1)
        elif (T <= 3290):
            g0ElemA = 229382.886 - 722.59722 * T + 78.5244752 * T * math.log(T) - 17.983376E-3 * T**2 + 0.195033E-6 *T**3 - 93813648 * T**(-1)
        else:
            g0ElemA = -1042384.014 + 2985.491246 * T - 362.1591318 * T * math.log(T) + 43.117795E-3 * T**2 - 1.055148E-6 * T**3 + 554714342 * T**(-1)
    if (tempElemB == 'Cr'):
        if (T <= 2180):
            g0ElemB = -8856.94 + 157.48 * T - 26.908 * T * math.log(T) + 1.89435E-3 *T**2 - 1.47721E-6 * T**3 + 139250 * T**(-1)
        else:
            g0ElemB = -34869.344 + 344.18 * T - 50 * T * math.log(T) - 2885.26E29 * T**(-9)
    elif (tempElemB == 'W'):
        if (T <= 3695):
            g0ElemB = -7646.311 + 130.4 * T - 24.1 * T * math.log(T) - 1.936E-3 * T**2 + 0.207E-6 * T**3 + 44500 * T**(-1) - 0.0533E-9 * T**4
        else:
            g0ElemB = -82868.801 + 389.362335 * T - 54 * T * math.log(T) + 1528.621E30 * T**(-9)
    else:
        if (T <= 1300):
            g0ElemB = -7285.889 + 119.139857 * T - 23.7592624 * T * math.log(T) - 2.623033E-3 * T**2 + 0.170109E-6 * T**3 -3293 * T**(-1)
        elif (T <= 2500):
            g0ElemB = -22389.955 + 243.88676 * T - 41.137088 * T * math.log(T) + 6.167572E-3 * T**2 - 0.655136E-6 * T**3 + 2429586 * T**(-1)
        elif (T <= 3290):
            g0ElemB = 229382.886 - 722.59722 * T + 78.5244752 * T * math.log(T) - 17.983376E-3 * T**2 + 0.195033E-6 *T**3 - 93813648 * T**(-1)
        else:
            g0ElemB = -1042384.014 + 2985.491246 * T - 362.1591318 * T * math.log(T) + 43.117795E-3 * T**2 - 1.055148E-6 * T**3 + 554714342 * T**(-1)

    ## Calculating Gibbs energy for the entire composition range
    composition = []
    gmm = []
    gid = []
    gex = []
    tempxB = 0.01
    while (tempxB < 1.0):
        tempgmm = (1 - tempxB) * g0ElemA + tempxB * g0ElemB
        gmm.append(tempgmm * 0.001)
        tempgid = R * T * ((1 - tempxB) * math.log(1 - tempxB) + tempxB * math.log(tempxB))
        gid.append(tempgid * 0.001)
        tempgex = (1 - tempxB) * tempxB * (L0 + (1 - 2 * tempxB) * L1 + (1 - 2 * tempxB)**2 * L2)
        gex.append(tempgex * 0.001)
        composition.append(tempxB)
        tempxB = tempxB + 0.01

    return g0ElemA, g0ElemB, composition, gmm, gid, gex, L0, L1, L2
    
def gibbsEqui():
    g0ElemA, g0ElemB, composition, gmm, gid, gex, L0, L1, L2 = gibbsCalculate()
    T = float(temp.get())
    R = 8.314
    tempxB = 0.5
    ## Calculating the mechanical mixing part at 0.5 composition
    tempgmm = round((((1 - tempxB) * g0ElemA) + (tempxB * g0ElemB)) * 0.001, 3)
    tk.Label(master, text = 'Mechanical contribution = ' + str(tempgmm), font = ('Times 14 bold')).place(x = 2, y = 500)
    tk.Label(master, text = 'kJ/mol', font = ('Times 14 bold')).place(x = 300, y = 500)
    ## Calculating the ideal part at 0.5 composition
    tempgid = round((R * T * ((1 - tempxB) * math.log(1 - tempxB) + tempxB * math.log(tempxB))) * 0.001, 3)
    tk.Label(master, text = 'Ideal contribution = ' + str(tempgid), font = ('Times 14 bold')).place(x = 2, y = 530)
    tk.Label(master, text = 'kJ/mol', font = ('Times 14 bold')).place(x = 240, y = 530)
    ## Calculating the excess part at 0.5 composition
    tempgex = round(((1 - tempxB) * tempxB * (L0 + (1 - 2 * tempxB) * L1 + (1 - 2 * tempxB)**2 * L2)) * 0.001, 3)
    tk.Label(master, text = 'Excess contribution = ' + str(tempgex), font = ('Times 14 bold')).place(x = 2, y = 560)
    tk.Label(master, text = 'kJ/mol', font = ('Times 14 bold')).place(x = 240, y = 560)

def gibbsMech():
    g0ElemA, g0ElemB, composition, gmm, gid, gex, L0, L1, L2 = gibbsCalculate()
    T = float(temp.get())
    figure1 = Figure(figsize = (5, 4), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gmm, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('Composition', fontsize = 8)
    plot1.set_ylabel('Gibbs energy (kJ/mol)', fontsize = 8)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 290, y = 10)

def gibbsId():
    g0ElemA, g0ElemB, composition, gmm, gid, gex, L0, L1, L2 = gibbsCalculate()
    T = float(temp.get())
    figure1 = Figure(figsize = (5, 4), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gid, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('Composition', fontsize = 8)
    plot1.set_ylabel('Gibbs energy (kJ/mol)', fontsize = 8)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 290, y = 10)

def gibbsEx():
    g0ElemA, g0ElemB, composition, gmm, gid, gex, L0, L1, L2 = gibbsCalculate()
    T = float(temp.get())
    figure1 = Figure(figsize = (5, 4), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gex, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('Composition', fontsize = 8)
    plot1.set_ylabel('Gibbs energy (kJ/mol)', fontsize = 8)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 290, y = 10)

def gibbsTotal():
    g0ElemA, g0ElemB, composition, gmm, gid, gex, L0, L1, L2 = gibbsCalculate()
    T = float(temp.get())
    gTotal = [gmm[i] + gid[i] + gex[i] for i in range(len(gmm))]
    figure1 = Figure(figsize = (5, 4), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gTotal, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('Composition', fontsize = 8)
    plot1.set_ylabel('Gibbs energy (kJ/mol)', fontsize = 8)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 290, y = 10)

def quitButtonFunction():
    master.quit()
    master.destroy()

## System name
tk.Label(master, text = 'First element', font = ('Times 14 bold')).place(x = 2, y = 100)
elemA = tk.Entry(master, width = 6, font = ('Times 16 bold'))
elemA.place(x = 150, y = 100)

tk.Label(master, text = 'Second element', font = ('Times 14 bold')).place(x = 2, y = 140)
elemB = tk.Entry(master, width = 6, font = ('Times 16 bold'))
elemB.place(x = 150, y = 140)

## Temperature
tk.Label(master, text = 'Temperature', font = ('Times 14 bold')).place(x = 2, y = 180)
temp = tk.Entry(master, width = 6, font = ('Times 16 bold'))
temp.place(x = 150, y = 180)
tk.Label(master, text = 'K', font = ('Times 14 bold')).place(x = 230, y = 180)

## Interaction parameters
tk.Label(master, text = 'L0', font = ('Times 14 bold')).place(x = 2, y = 220)
interL0 = tk.Entry(master, width = 6, font = ('Times 16 bold'))
interL0.place(x = 150, y = 220)
tk.Label(master, text = 'J/mol', font = ('Times 14 bold')).place(x = 230, y = 220)

tk.Label(master, text = 'L1', font = ('Times 14 bold')).place(x = 2, y = 260)
interL1 = tk.Entry(master, width = 6, font = ('Times 16 bold'))
interL1.place(x = 150, y = 260)
tk.Label(master, text = 'J/mol', font = ('Times 14 bold')).place(x = 230, y = 260)

tk.Label(master, text = 'L2', font = ('Times 14 bold')).place(x = 2, y = 300)
interL2 = tk.Entry(master, width = 6, font = ('Times 16 bold'))
interL2.place(x = 150, y = 300)
tk.Label(master, text = 'J/mol', font = ('Times 14 bold')).place(x = 230, y = 300)

## Calculate button
calc = tk.Button(master, text = 'Calculate', bg = 'silver', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsEqui).place(x = 2, y = 420)

## Plot buttons
gmmPlot = tk.Button(master, text = 'Plot\nMech part', bg = 'orange', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsMech).place(x = 142, y = 420)
gidPlot = tk.Button(master, text = 'Plot\nIdeal part', bg = 'orange', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsId).place(x = 282, y = 420)
gexPlot = tk.Button(master, text = 'Plot\nExcess part', bg = 'orange', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsEx).place(x = 422, y = 420)
gTotalPlot = tk.Button(master, text = 'Plot\nTotal', bg = 'deepskyblue', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsTotal).place(x = 562, y = 420)

## Quit button
quitButton = tk.Button(master, text = 'Quit', bg = 'silver', height = 2, width = 9, font = ('Times 12 bold'), command = quitButtonFunction).place(x = 702, y = 420)

## Gibbs energy displayer
##tk.Label(master, text = 'Gibbs energy at equiatomic composition', font = ('Times 12 bold')).place(x = 2, y = 500)
##tk.Label(master, text = 'G_mm').place(x = 2, y = 540)
##tk.Label(master, text = 'G_id').place(x = 2, y = 580)

## Taking it to mainloop
master.mainloop()

