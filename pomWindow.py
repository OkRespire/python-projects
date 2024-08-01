#import related packages
import time
from tkinter import *
#TODO: Use classes






class PomWindow:


    WORK_TIME = 25 * 60
    SHORT_REST_TIME = 5 * 60
    LONG_REST_TIME = 15 * 60


    def __init__(self):
        self.win = Tk()
        self.win.title("Pomodoro Timer by Rohane")
        self.win.geometry("800x500")
        
        self.titleLabel = Label(self.win, text = "Pomodoro Timer", font = "Calibri 40")
        self.titleLabel.pack()
        
        self.startButton = Button(self.win, text = "Start", command = self.startTimer)
        self.startButton.pack()

        self.stopButton = Button(self.win, text = "Stop", command = self.stopButton, state = DISABLED)

        self.isWork,self.isLongRest = true, false
        self.workTime, self.restTime = WORK_TIME, SHORT_REST_TIME
        self.completed, self.running = 0, false


 
    def startTimer(self):
        self.running = true


#
# #Actual Timer
# timerLabel = Label(master = window, text = "Set the timer", font = "Calibri 20")
# sec = StringVar()
# Entry(master = window, textvariable = sec, width = 2, font = "Calibri 13").place(x = 500, y = 250)
# sec.set("00")
#
#
#
# min = StringVar()
# Entry(master = window, textvariable = min, width = 2, font = "Calibri 13").place(x = 400,y = 250)
# min.set("00")
#
# hour = StringVar()
# Entry(master = window, textvariable = hour, width = 2, font = "Calibri 13").place(x = 300,y = 250)
# hour.set("00")
#
#
#
#
#
#
# #ensures all the labels and entries are properly displayed in the window
# timerLabel.pack()
#
#
#
#
#
# #run the window
# window.mainloop()
#


#TODO: set the prints to output in the window


#print("You are using" , platform.system())

#print("This is a Pomedoro timer\nThe way that this works is simple, you have 25 minutes of work and 5 minutes of rest\nThis will go on for three times (or as many times as you want) and you will feel much more productive :) ")



#try:
    # times_to_ask = int(input("How many times do you want to restart the pomedoro timer?\nNOTE: putting a blank value will make it so its 3 times "))

# except():
#     times_to_ask = 3
#
# for i in range(times_to_ask):
#     time.sleep(15) #25 minutes in seconds
#     #toast("25 minutes of work completed!")
#     #toast("Now have a 5 minute rest!")
#     time.sleep(300) #5 minutes in seconds
#
#
# print("Congrats! I hope you had a productive session!")
#





