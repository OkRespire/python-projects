#import related packages
import time
import tkinter as tk
#TODO: Use classes


WORK_TIME = 25 * 60
SHORT_REST_TIME = 5 * 60
LONG_REST_TIME = 15 * 60





class PomWindow:


    
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Pomodoro Timer by Rohane")
        self.win.geometry("800x500")
        
        self.titleLabel = tk.Label(self.win, text = "Pomodoro Timer", font = "Calibri 40")
        self.titleLabel.pack()
        
        self.startButton = tk.Button(self.win, text = "Start", command = self.startTimer(), state="normal")
        self.startButton.pack()

        self.stopButton = tk.Button(self.win, text = "Stop", command = self.stopTimer(), state = "disabled")
        self.stopButton.pack()

        self.isWork,self.isLongRest = True, False
        self.workTime, self.restTime = WORK_TIME, SHORT_REST_TIME
        self.completed, self.running = 0, False
        
        self.win.mainloop()

 
    def startTimer(self):
        self.running = True
        self.startButton = tk.Button(state = "active")
        self.stopButton = tk.Button(state = "normal")
    
    def stopTimer(self):
        self.running = False
  
window = PomWindow()



