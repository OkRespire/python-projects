# import related packages
from tkinter import messagebox
import tkinter as tk


# set constants for the timer to use
WORK_TIME = 25 * 60
SHORT_REST_TIME = 5 * 60
LONG_REST_TIME = 15 * 60


class PomWindow:
    # setup the timer's window
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
        self.timerLabel.pack(pady=40)  # timer is at the center of the window

        self.startButton = tk.Button(
            self.win, text="Start", command=self.startTimer, state="normal"
        )  # when button is pressed, start timer
        self.startButton.pack()

        self.stopButton = tk.Button(
            self.win, text="Stop", command=self.stopTimer, state="disabled"
        )  # when button is pressed, stop timer
        self.stopButton.pack()

        self.win.mainloop()

    def startTimer(self):
        self.running = True
        self.startButton.config(state="disabled")  # sets the button to disabled
        self.stopButton.config(state="normal")
        self.titleLabel.config(
            text="Time to work!" if self.isWork else "Time to rest!"
        )  # changes the label depending if you are on work or rest
        self.updateTimer()  # updates timer

    def stopTimer(self):
        self.startButton.config(state="normal")
        self.stopButton.config(state="disabled")
        self.titleLabel.config(text="Paused.")
        self.running = False  # sets the flag to false

    def updateTimer(self):
        if self.running:
            if self.isWork:
                self.workTime -= 1  # decrements timer
                if self.workTime == 0:  # if worktime reaches 0
                    messagebox.showinfo(
                        "Work Complete!",
                        "Now is the time to have a short rest!"
                        if self.completed % 4 != 0
                        else "Now is the time to take a long rest!",
                    )  # shows a message box when it is over - notifying user
                    self.completed += 1  # adds one to the completed counter
                    self.isWork = False  # work time is now rest time
                    self.restTime = (
                        SHORT_REST_TIME if self.completed % 4 != 0 else LONG_REST_TIME
                    )  # decides if the rest time used is short or long - long only used when 4 rounds are completed
                    self.titleLabel.config(text="Time to Rest!")

            else:
                self.restTime -= 1  # decrements rest timer
                if self.restTime == 0:  # when rest time is over
                    self.isWork = True  # work time commences
                    self.workTime = WORK_TIME
                    messagebox.showinfo(
                        "Rest Complete!", "Time to work!"
                    )  # message box notifies user that rest is over
                    self.titleLabel.config(text="Time to Work!")

            minutes, seconds = divmod(
                self.workTime if self.isWork else self.restTime, 60
            )  # sets minutes and seconds from the raw seconds value

            self.timerLabel.config(
                text="{:02d}:{:02d}".format(minutes, seconds)
            )  # formats the timer into a readable value

            self.win.after(1000, self.updateTimer)  # updates the window every second.


PomWindow()
