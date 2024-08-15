# import related packages
import time
import tkinter as tk
# TODO: Use classes


WORK_TIME = 25 * 60
SHORT_REST_TIME = 5 * 60
LONG_REST_TIME = 15 * 60


class PomWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Pomodoro Timer by Rohane")
        self.win.geometry("200x100")
        self.isWork, self.isLongRest = True, False
        self.workTime, self.restTime = WORK_TIME, SHORT_REST_TIME
        self.completed, self.running = 0, False

        self.titleLabel = tk.Label(self.win, text="Pomodoro Timer", font="Calibri 20")
        self.titleLabel.pack()

        self.startButton = tk.Button(
            self.win, text="Start", command=self.startTimer, state="normal"
        )
        self.startButton.pack()

        self.stopButton = tk.Button(
            self.win, text="Stop", command=self.stopTimer, state="disabled"
        )
        self.stopButton.pack()

        self.minuteEntry = tk.Entry(self.win)
        self.minuteEntry.pack()
        self.minuteVal = tk.StringVar()
        self.minuteVal.set("25")
        self.minuteEntry["textvariable"] = self.minuteVal

        self.secondEntry = tk.Entry(self.win)
        self.secondEntry.pack()
        self.secondVal = tk.StringVar()
        self.secondVal.set("00")
        self.secondEntry["textvariable"] = self.secondVal

        self.win.mainloop()

    def startTimer(self):
        self.running = True
        self.startButton.config(state="disabled")
        self.stopButton.config(state="normal")
        self.updateTimer()

    def stopTimer(self):
        self.running = False

    def updateTimer(self):
        if self.running:
            self.win.after(1000, self.updateTimer)


window = PomWindow()
