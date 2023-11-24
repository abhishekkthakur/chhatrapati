import tkinter as tk
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
import sgteDatabase

## Creating a new tkinter window
master = tk.Tk()
master.title('Gibbs energy calculator')
master.geometry('1150x800')             ## First is width

def gibbsMech():
    if (len(elemA.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element A')
        return
    else:
        tempElemA = str(elemA.get())
    if (len(elemB.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element B')
        return
    else:
        tempElemB = str(elemB.get())
    if (len(temp.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing temperature')
        return
    else:
        T = float(temp.get())
    g0ElemA, g0ElemB = sgteDatabase.gibbsCalculate(tempElemA, tempElemB, T)

    ## Calculating the mechanical Gibbs energy for the entire composition range
    composition = []
    gmm = []
    tempxB = 0.01
    while (tempxB < 1.0):
        tempgmm = (1 - tempxB) * g0ElemA + tempxB * g0ElemB
        gmm.append(tempgmm * 0.001)
        composition.append(tempxB)
        tempxB = tempxB + 0.01
    figure1 = Figure(figsize = (6, 5), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gmm, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('$X_{}$'.format(tempElemB), fontsize = 12)
    plot1.set_ylabel('Mechanical Gibbs energy (kJ/mol)', fontsize = 12)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 500, y = 160)

def gibbsId():
    if (len(elemA.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element A')
        return
    else:
        tempElemA = str(elemA.get())
    if (len(elemB.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element B')
        return
    else:
        tempElemB = str(elemB.get())
    if (len(temp.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing temperature')
        return
    else:
        T = float(temp.get())
    g0ElemA, g0ElemB = sgteDatabase.gibbsCalculate(tempElemA, tempElemB, T)

    ## Calculating the ideal Gibbs energy for the entire composition range
    R = 8.314
    composition = []
    gid = []
    tempxB = 0.01
    while (tempxB < 1.0):
        tempgid = R * T * ((1 - tempxB) * math.log(1 - tempxB) + tempxB * math.log(tempxB))
        gid.append(tempgid * 0.001)
        composition.append(tempxB)
        tempxB = tempxB + 0.01
    figure1 = Figure(figsize = (6, 5), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gid, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('$X_{}$'.format(tempElemB), fontsize = 12)
    plot1.set_ylabel('Ideal Gibbs energy (kJ/mol)', fontsize = 12)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 500, y = 160)

def gibbsEx():
    if (len(elemA.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element A')
        return
    else:
        tempElemA = str(elemA.get())
    if (len(elemB.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element B')
        return
    else:
        tempElemB = str(elemB.get())
    if (len(temp.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing temperature')
        return
    else:
        T = float(temp.get())
    if (radioVar.get() == 'selectedModel'):
        messagebox.showwarning('Information needed', 'Please select a model')
        return
    elif (radioVar.get() == 'regularSolutionModel'):
        if (len(regularL0.get()) == 0):
            messagebox.showwarning('Information needed', 'Missing L0 parameter')
            return
        else:
            L0 = float(regularL0.get())
            L1 = 0
            L2 = 0
    elif (radioVar.get() == 'subRegularSolutionModel'):
        if (len(subRegularL0.get()) == 0):
            messagebox.showwarning('Information needed', 'Missing L0 parameter')
            return
        else:
            L0 = float(subRegularL0.get())
        if (len(subRegularL1.get()) == 0):
            L1 = 0
        else:
            L1 = float(subRegularL1.get())
        if (len(subRegularL2.get()) == 0):
            L2 = 0
        else:
            L2 = float(subRegularL2.get())
            
    g0ElemA, g0ElemB = sgteDatabase.gibbsCalculate(tempElemA, tempElemB, T)

    ## Calculating the ideal Gibbs energy for the entire composition range
    R = 8.314
    composition = []
    gex = []
    tempxB = 0.01
    while (tempxB < 1.0):
        tempgex = (1 - tempxB) * tempxB * (L0 + (1 - 2 * tempxB) * L1 + (1 - 2 * tempxB)**2 * L2)
        gex.append(tempgex * 0.001)
        composition.append(tempxB)
        tempxB = tempxB + 0.01
    figure1 = Figure(figsize = (6, 5), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gex, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('$X_{}$'.format(tempElemB), fontsize = 12)
    plot1.set_ylabel('Excess Gibbs energy (kJ/mol)', fontsize = 12)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 500, y = 160)

def gibbsTotal():
    if (len(elemA.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element A')
        return
    else:
        tempElemA = str(elemA.get())
    if (len(elemB.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing element B')
        return
    else:
        tempElemB = str(elemB.get())
    if (len(temp.get()) == 0):
        messagebox.showwarning('Information needed', 'Missing temperature')
        return
    else:
        T = float(temp.get())
    if (radioVar.get() == 'selectedModel'):
        messagebox.showwarning('Information needed', 'Please select a model')
        return
    elif (radioVar.get() == 'regularSolutionModel'):
        if (len(regularL0.get()) == 0):
            messagebox.showwarning('Information needed', 'Missing L0 parameter')
            return
        else:
            L0 = float(regularL0.get())
            L1 = 0
            L2 = 0
    elif (radioVar.get() == 'subRegularSolutionModel'):
        if (len(subRegularL0.get()) == 0):
            messagebox.showwarning('Information needed', 'Missing L0 parameter')
            return
        else:
            L0 = float(subRegularL0.get())
        if (len(subRegularL1.get()) == 0):
            L1 = 0
        else:
            L1 = float(subRegularL1.get())
        if (len(subRegularL2.get()) == 0):
            L2 = 0
        else:
            L2 = float(subRegularL2.get())
            
    g0ElemA, g0ElemB = sgteDatabase.gibbsCalculate(tempElemA, tempElemB, T)

    ## Calculating Gibbs energy for the entire composition range
    R = 8.314
    composition = []
    gtotal = []
    tempxB = 0.01
    while (tempxB < 1.0):
        tempgmm = (1 - tempxB) * g0ElemA + tempxB * g0ElemB
        tempgid = R * T * ((1 - tempxB) * math.log(1 - tempxB) + tempxB * math.log(tempxB))
        tempgex = (1 - tempxB) * tempxB * (L0 + (1 - 2 * tempxB) * L1 + (1 - 2 * tempxB)**2 * L2)
        tempgtotal = tempgmm + tempgid + tempgex
        gtotal.append(tempgtotal * 0.001)
        composition.append(tempxB)
        tempxB = tempxB + 0.01
    figure1 = Figure(figsize = (6, 5), dpi = 100)
    plot1 = figure1.add_subplot(1, 1, 1)
    plot1.plot(composition, gtotal, color = 'black', linewidth = 2.0)
    plot1.set_xlabel('$X_{}$'.format(tempElemB), fontsize = 12)
    plot1.set_ylabel('Total Gibbs energy (kJ/mol)', fontsize = 12)
    canvas = FigureCanvasTkAgg(figure1, master)
    canvas.get_tk_widget().place(x = 500, y = 160)

def regularSolution():
    regularL0.config(state = NORMAL)
    subRegularL0.config(state = DISABLED)
    subRegularL1.config(state = DISABLED)
    subRegularL2.config(state = DISABLED)

def subRegularSolution():
    subRegularL0.config(state = NORMAL)
    subRegularL1.config(state = NORMAL)
    subRegularL2.config(state = NORMAL)
    regularL0.config(state = DISABLED)

def resetButtonFunction():
    elemA.delete(0, END)
    elemB.delete(0, END)
    temp.delete(0, END)
    regularL0.delete(0, END)
    subRegularL0.delete(0, END)
    subRegularL1.delete(0, END)
    subRegularL2.delete(0, END)
    radioVar.set('selectedModel')
    regularL0.config(state = DISABLED)
    subRegularL0.config(state = DISABLED)
    subRegularL1.config(state = DISABLED)
    subRegularL2.config(state = DISABLED)
    
def quitButtonFunction():
    master.quit()
    master.destroy()

## Title label
tk.Label(master, text = 'Thermodynamic calculator', font = ('Times 28 bold')).place(x = 350, y = 2)

## Creating frame for element A and B and for temperature
frame1 = Frame(master, bg = 'moccasin', highlightthickness = 3, highlightbackground = 'black', height = 130, width = 260).place(x = 20, y = 100)

## System name
tk.Label(frame1, text = 'Element A', bg = 'moccasin', font = ('Times 14 bold')).place(x = 25, y = 110)
elemA = tk.Entry(frame1, width = 6, font = ('Times 16 bold'))
elemA.place(x = 170, y = 110)

tk.Label(frame1, text = 'Element B', bg = 'moccasin', font = ('Times 14 bold')).place(x = 25, y = 150)
elemB = tk.Entry(frame1, width = 6, font = ('Times 16 bold'))
elemB.place(x = 170, y = 150)

## Temperature
tk.Label(frame1, text = 'Temperature', bg = 'moccasin', font = ('Times 14 bold')).place(x = 25, y = 190)
temp = tk.Entry(frame1, width = 6, font = ('Times 16 bold'))
temp.place(x = 170, y = 190)
tk.Label(master, text = 'K', bg = 'moccasin', font = ('Times 14 bold')).place(x = 245, y = 190)

## Creating frame for regular solution model
frame2 = Frame(master, bg = 'moccasin', highlightthickness = 3, highlightbackground = 'black', height = 200, width = 260).place(x = 20, y = 250)

## Creating radio buttons for different thermodynamic models
radioVar = StringVar(frame2, 'selectedModel')

radioRegular = tk.Radiobutton(frame2, bg = 'moccasin', variable = radioVar, value = 'regularSolutionModel', text = 'Regular solution model', font = ('Times 12 bold'), command = regularSolution).place(x = 25, y = 260)
tk.Label(frame2, bg = 'moccasin', text = 'L0', font = ('Times 11 bold')).place(x = 60, y = 290)
regularL0 = tk.Entry(frame2, width = 6, font = ('Times 11 bold'))
regularL0.place(x = 90, y = 290)
regularL0.config(state = DISABLED)
tk.Label(frame2, bg = 'moccasin', text = 'J/mol', font = ('Times 11 bold')).place(x = 150, y = 290)


radioSubRegular = tk.Radiobutton(frame2, bg = 'moccasin', variable = radioVar, value = 'subRegularSolutionModel', text = 'Sub regular solution model', font = ('Times 12 bold'), command = subRegularSolution).place(x = 25, y = 330)
tk.Label(frame2, bg = 'moccasin', text = 'L0', font = ('Times 11 bold')).place(x = 60, y = 360)
subRegularL0 = tk.Entry(frame2, width = 6, font = ('Times 11 bold'))
subRegularL0.place(x = 90, y = 360)
subRegularL0.config(state = DISABLED)
tk.Label(frame2, bg = 'moccasin', text = 'J/mol', font = ('Times 11 bold')).place(x = 150, y = 360)

tk.Label(frame2, bg = 'moccasin', text = 'L1', font = ('Times 11 bold')).place(x = 60, y = 390)
subRegularL1 = tk.Entry(frame2, width = 6, font = ('Times 11 bold'))
subRegularL1.place(x = 90, y = 390)
subRegularL1.config(state = DISABLED)
tk.Label(frame2, bg = 'moccasin', text = 'J/mol', font = ('Times 11 bold')).place(x = 150, y = 390)

tk.Label(frame2, bg = 'moccasin', text = 'L2', font = ('Times 11 bold')).place(x = 60, y = 420)
subRegularL2 = tk.Entry(frame2, width = 6, font = ('Times 11 bold'))
subRegularL2.place(x = 90, y = 420)
subRegularL2.config(state = DISABLED)
tk.Label(frame2, bg = 'moccasin', text = 'J/mol', font = ('Times 11 bold')).place(x = 150, y = 420)

## Frame to contain plots
frame3 = Frame(master, highlightthickness = 3, highlightbackground = 'black', height = 600, width = 650).place(x = 475, y = 80)

## Plot buttons
gmmPlot = tk.Button(master, text = 'Plot\nMech part', bg = 'gainsboro', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsMech).place(x = 20, y = 480)
gidPlot = tk.Button(master, text = 'Plot\nIdeal part', bg = 'gainsboro', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsId).place(x = 120, y = 480)
gexPlot = tk.Button(master, text = 'Plot\nExcess part', bg = 'gainsboro', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsEx).place(x = 220, y = 480)
gTotalPlot = tk.Button(master, text = 'Plot\nTotal', bg = 'gainsboro', height = 2, width = 9, font = ('Times 12 bold'), command = gibbsTotal).place(x = 320, y = 480)

## Reset button
resetButton = tk.Button(master, text = 'Reset', bg = 'silver', height = 2, width = 9, font = ('Times 12 bold'), command = resetButtonFunction).place(x = 20, y = 550)
## Quit button
quitButton = tk.Button(master, text = 'Quit', bg = 'silver', height = 2, width = 9, font = ('Times 12 bold'), command = quitButtonFunction).place(x = 120, y = 550)
'''
## Gibbs energy displayer
##tk.Label(master, text = 'Gibbs energy at equiatomic composition', font = ('Times 12 bold')).place(x = 2, y = 500)
##tk.Label(master, text = 'G_mm').place(x = 2, y = 540)
##tk.Label(master, text = 'G_id').place(x = 2, y = 580)

## Taking it to mainloop
'''
master.mainloop()

