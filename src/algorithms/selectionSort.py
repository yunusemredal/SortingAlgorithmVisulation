"""
import time
from tkinter import *
from tkinter import ttk

# Global değişkenler
comparisonCount = 0
startTime = 0

def selectionSort(data, drowData, timeTick, root,timeLabel, comparisonLabel,varG):
    global comparisonCount
    global startTime

    comparisonCount = 0
    startTime = time.time()

    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            comparisonCount += 1
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drowData(data, ['yellow' if x == i or x == min_idx else 'red' for x in range(len(data))],varG.get())
        root.after(timeTick)

    endTime = time.time()
    totalTime = endTime - startTime
    timeLabel.config(text="Zamanı: {:.2f} s".format(totalTime))

    comparisonLabel.config(text="Karşılaştırma: " + str(comparisonCount))
"""
import time
from tkinter import *
from tkinter import ttk

# Global değişkenler
comparisonCount = 0
sorting_stopped = False

def selectionSort(data, drowData, timeTick, root, timeLabel, comparisonLabel, varG):
    global comparisonCount
    global sorting_stopped

    comparisonCount = 0
    sorting_stopped = False
    startTime = time.time()

    for i in range(len(data)):
        if sorting_stopped:
            return

        min_idx = i
        for j in range(i + 1, len(data)):
            comparisonCount += 1
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drowData(data, ['yellow' if x == i or x == min_idx else 'red' for x in range(len(data))], varG.get())
        root.after(timeTick)

    endTime = time.time()
    totalTime = endTime - startTime
    timeLabel.config(text="Zamanı: {:.2f} s".format(totalTime))

    comparisonLabel.config(text="Karşılaştırma: " + str(comparisonCount))

def stopSorting():
    global sorting_stopped
    sorting_stopped = True if not sorting_stopped else False
