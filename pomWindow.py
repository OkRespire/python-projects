# import related packages
from tkinter import messagebox
import tkinter as tk

# TODO: USE THE RIGHT VALUES WHEN FINISHING
WORK_TIME = 2
SHORT_REST_TIME = 5
LONG_REST_TIME = 15


class PomWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Pomodoro Timer by Rohane")
        self.win.geometry("400x300")
        self.isWork = (True,)
        self.workTime, self.restTime = WORK_TIME, SHORT_REST_TIME
        self.completed, self.running = 0, False

        self.titleLabel = tk.Label(self.win, text="Pomodoro Timer", font="Calibri 20")
        self.titleLabel.pack()
        self.timerLabel = tk.Label(self.win, text="", font=("TkDefaultFont", 40))
        self.timerLabel.pack(pady=40)

        self.startButton = tk.Button(
            self.win, text="Start", command=self.startTimer, state="normal"
        )
        self.startButton.pack()

        self.stopButton = tk.Button(
            self.win, text="Stop", command=self.stopTimer, state="disabled"
        )
        self.stopButton.pack()

        self.win.mainloop()

    def startTimer(self):
        self.running = True
        self.startButton.config(state="disabled")
        self.stopButton.config(state="normal")
        self.titleLabel.config(text="Time to work!" if self.isWork else "Time to rest!")
        self.updateTimer()

    def stopTimer(self):
        self.startButton.config(state="normal")
        self.stopButton.config(state="disabled")
        self.titleLabel.config(text="Paused.")
        self.running = False

    def updateTimer(self):
        if self.running:
            if self.isWork:
                self.workTime -= 1
                if self.workTime == 0:
                    messagebox.showinfo(
                        "Work Complete!",
                        "Now is the time to have a short rest!"
                        if self.completed % 4 == 0
                        else "Now is the time to take a long rest!",
                    )
                    self.completed += 1
                    self.isWork = False
                    self.restTime = (
                        SHORT_REST_TIME if self.completed % 4 != 0 else LONG_REST_TIME
                    )
                    self.titleLabel.config(text="Time to Rest!")

            else:
                self.restTime -= 1
                if self.restTime == 0:
                    self.isWork = True
                    self.workTime = WORK_TIME
                    messagebox.showinfo("Rest Complete!", "Time to work!")
                    self.titleLabel.config("Time to Work!")

            minutes, seconds = divmod(
                self.workTime if self.isWork else self.restTime, 60
            )

            self.timerLabel.config(text="{:02d}:{:02d}".format(minutes, seconds))

            self.win.after(1000, self.updateTimer)


PomWindow()
