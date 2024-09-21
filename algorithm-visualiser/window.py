# import related packages
from tkinter import messagebox
import tkinter as tk
import quicksort


# set a new window class
class Window:
    def __init__(self) -> None:
        # setting up window of the program
        self.root = tk.Tk()
        self.root.title("Sorting algorithm visualiser")
        self.root.geometry("400x300")

        self.completed, self.running = False, False

        self.acceptableInput = tk.Label(
            self.root,
            text="Enter a list of numbers. seperate the values with commas (,)",
        )
        self.acceptableInput.pack()

        self.startButton = tk.Button(
            self.root, text="Start", command=self.updateWindow, state="normal"
        )
        self.startButton.pack()
        self.listInput = tk.Entry(self.root)
        self.userInput = tk.StringVar()
        self.listInput["textvariable"] = self.userInput

        self.listInput.pack()
        self.userInput = True

        self.root.mainloop()

        pass

    def updateWindow(self) -> None:
        if self.userInput:
            self.convertedList = self.convertToList()
            self.userInput = False

        quicksort.quickSort(self.convertedList)

    def convertToList(self) -> list:
        # get the list content
        listContents = self.listInput.get().split(",")

        # iterate through the list and convert them all to integers
        listContents = [int(num) for num in listContents]
        print(listContents)
        return listContents
