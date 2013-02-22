#!/usr/bin/python

"""
    Generate Hole Array
    Version 0.0.1

    Generates G Code for an array of milled holes

    copyright 2013 Tim Foreman
    twforeman@gmail.com

"""

from Tkinter import *
from math import *
import os

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.EntryFrame = Frame(self,bd=5)
        self.EntryFrame.grid(row=0, column=0)

        self.st00 = Label(self.EntryFrame, text='Hole Array Data')
        self.st00.grid(row=0, column=0, columnspan=2)

        self.st01 = Label(self.EntryFrame, text='Units')
        self.st01.grid(row=1, column=0, sticky=W)
        self.UnitsVar = IntVar()
        Radiobutton(self.EntryFrame, text='IN', value=0, variable=self.UnitsVar).grid(row=1, column=1, sticky = W)
        Radiobutton(self.EntryFrame, text='MM', value=1, variable=self.UnitsVar).grid(row=1, column=1, sticky = E)

        self.sp00 = Label(self.EntryFrame, text=' ')
        self.sp00.grid(row=2)

        self.sp01 = Label(self.EntryFrame, text='Machining Data ')
        self.sp01.grid(row=3, column=0, columnspan=2)

        self.st02 = Label(self.EntryFrame, text='Endmill Diameter')
        self.st02.grid(row=4, column=0, sticky=W)
        self.EndmillDiameterVar = StringVar()
        self.EndmillDiameter = Entry(self.EntryFrame, textvariable=self.EndmillDiameterVar ,width=15)
        self.EndmillDiameter.grid(row=4, column=1)

        self.st03 = Label(self.EntryFrame, text='Step Over Percentage')
        self.st03.grid(row=5, column=0, sticky=W)
        self.StepOverDiameterVar = StringVar()
        self.StepOverDiameter = Entry(self.EntryFrame, textvariable=self.StepOverDiameterVar ,width=15)
        self.StepOverDiameter.grid(row=5, column=1)

        self.st04 = Label(self.EntryFrame, text='Safety Plane Height')
        self.st04.grid(row=6, column=0, sticky=W)
        self.SafetyPlaneHeightVar = StringVar()
        self.SafetyPlaneHeight = Entry(self.EntryFrame, textvariable=self.SafetyPlaneHeightVar ,width=15)
        self.SafetyPlaneHeight.grid(row=6, column=1)

        self.st05 = Label(self.EntryFrame, text='Feed Rate')
        self.st05.grid(row=7, column=0, sticky=W)
        self.FeedRateVar = StringVar()
        self.FeedRate = Entry(self.EntryFrame, textvariable=self.FeedRateVar ,width=15)
        self.FeedRate.grid(row=7, column=1)

        self.st05 = Label(self.EntryFrame, text='Plunge Rate')
        self.st05.grid(row=8, column=0, sticky=W)
        self.PlungeRateVar = StringVar()
        self.PlungeRate = Entry(self.EntryFrame, textvariable=self.PlungeRateVar ,width=15)
        self.PlungeRate.grid(row=8, column=1)

        self.st06 = Label(self.EntryFrame, text='Cut Direction')
        self.st06.grid(row=9, column=0, sticky=W)
        self.CutDirectionVar = IntVar()
        Radiobutton(self.EntryFrame, text='CCW', value=0, variable=self.CutDirectionVar).grid(row=9, column=1, sticky = W)
        Radiobutton(self.EntryFrame, text='CW', value=1, variable=self.CutDirectionVar).grid(row=9, column=1, sticky = E)

        self.sp03 = Label(self.EntryFrame, text=' ')
        self.sp03.grid(row=10)

        self.sp04 = Label(self.EntryFrame, text='Hole Data')
        self.sp04.grid(row=11, column=0, columnspan=2)

        self.st07 = Label(self.EntryFrame, text='Hole Diameter')
        self.st07.grid(row=12, column=0, sticky=W)
        self.HoleDiameterVar = StringVar()
        self.HoleDiameter = Entry(self.EntryFrame, textvariable=self.HoleDiameterVar ,width=15)
        self.HoleDiameter.grid(row=12, column=1)

        self.st08 = Label(self.EntryFrame, text='Hole Depth')
        self.st08.grid(row=13, column=0, sticky=W)
        self.HoleDepthVar = StringVar()
        self.HoleDepth = Entry(self.EntryFrame, textvariable=self.HoleDepthVar ,width=15)
        self.HoleDepth.grid(row=13, column=1)

        self.st09 = Label(self.EntryFrame, text='Plunge Increment')
        self.st09.grid(row=14, column=0, sticky=W)
        self.PlungeIncrementVar = StringVar()
        self.PlungeIncrement = Entry(self.EntryFrame, textvariable=self.PlungeIncrementVar ,width=15)
        self.PlungeIncrement.grid(row=14, column=1)

        self.sp05 = Label(self.EntryFrame, text=' ')
        self.sp05.grid(row=15)

        self.sp06 = Label(self.EntryFrame, text='Array Data')
        self.sp06.grid(row=16, column=0, columnspan=2)

        self.st10 = Label(self.EntryFrame, text='X Origin (first hole)')
        self.st10.grid(row=17, column=0, sticky=W)
        self.XOriginVar = StringVar()
        self.XOrigin = Entry(self.EntryFrame, textvariable=self.XOriginVar ,width=15)
        self.XOrigin.grid(row=17, column=1)

        self.st11 = Label(self.EntryFrame, text='Y Origin (first hole)')
        self.st11.grid(row=18, column=0, sticky=W)
        self.YOriginVar = StringVar()
        self.YOrigin = Entry(self.EntryFrame, textvariable=self.YOriginVar ,width=15)
        self.YOrigin.grid(row=18, column=1)

        self.st12 = Label(self.EntryFrame, text='Z Origin (first hole)')
        self.st12.grid(row=19, column=0, sticky=W)
        self.ZOriginVar = StringVar()
        self.ZOrigin = Entry(self.EntryFrame, textvariable=self.ZOriginVar ,width=15)
        self.ZOrigin.grid(row=19, column=1)

        self.st13 = Label(self.EntryFrame, text='X Count')
        self.st13.grid(row=20, column=0, sticky=W)
        self.XCountVar = StringVar()
        self.XCount = Entry(self.EntryFrame, textvariable=self.XCountVar ,width=15)
        self.XCount.grid(row=20, column=1)

        self.st14 = Label(self.EntryFrame, text='Y Count')
        self.st14.grid(row=21, column=0, sticky=W)
        self.YCountVar = StringVar()
        self.YCount = Entry(self.EntryFrame, textvariable=self.YCountVar ,width=15)
        self.YCount.grid(row=21, column=1)

        self.st15 = Label(self.EntryFrame, text='X Spacing')
        self.st15.grid(row=22, column=0, sticky=W)
        self.XSpacingVar = StringVar()
        self.XSpacing = Entry(self.EntryFrame, textvariable=self.XSpacingVar ,width=15)
        self.XSpacing.grid(row=22, column=1)

        self.st16 = Label(self.EntryFrame, text='Y Spacing')
        self.st16.grid(row=23, column=0, sticky=W)
        self.YSpacingVar = StringVar()
        self.YSpacing = Entry(self.EntryFrame, textvariable=self.YSpacingVar ,width=15)
        self.YSpacing.grid(row=23, column=1)

        self.sp07 = Label(self.EntryFrame, text=' ')
        self.sp07.grid(row=24)

        self.sp08 = Label(self.EntryFrame, text='Output Options')
        self.sp08.grid(row=25, column=0, columnspan=2)

        self.st17 = Label(self.EntryFrame, text='Output File')
        self.st17.grid(row=26, column=0, sticky=W)
        self.OutputFileVar = StringVar()
        self.OutputFile = Entry(self.EntryFrame, textvariable=self.OutputFileVar ,width=15)
        self.OutputFile.grid(row=26, column=1)

        self.DoItButton = Button(self.EntryFrame, text='Generate G Code', command=self.DoIt)
        self.DoItButton.grid(row=27, column=0)

        self.ToFile = Button(self.EntryFrame, text='Save To File', command=self.ToFile)
        self.ToFile.grid(row=27, column=1)

        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=28, column=0, columnspan=2)

        self.TextFrame = Frame(self, bd=5)
        self.TextFrame.grid(row=0, column=1)
        self.GCodeVar = StringVar()
        self.TextBox=Text(self.TextFrame, borderwidth=5, width=30)
        self.TextBox.grid(row=1, column=1, sticky=N)

        self.sp09 = Label(self.TextFrame, text='G Code Output')
        self.sp09.grid(row=0, column=1)

    def DoIt(self):
        self.GCodeVar = self.GenerateCircle(self.XOriginVar, self.YOriginVar, self.HoleDiameterVar / 2.0, 0)
        self.TextBox.insert(self.GCodeVar)

    def GenerateCircle(self, XCenter, YCenter, Radius, Direction):
        if Direction == 0:    # CCW
            self.GCode = 'G03 X{.4f} Y{.4f} I{.4f} J{.4f}\n'.format(XCenter, ( YCenter + Radius ), (-Radius), 0)
        else:
            self.GCode = 'G03 X{.4f} Y{.4f} I{.4f} J{.4f}\n'.format(XCenter, ( YCenter - Radius ), (-Radius), 0)

        return self.GCode


    def ToFile(self):
        noop

app = Application()
app.master.title("Generate Hole Array 0.1.0")
app.mainloop()
