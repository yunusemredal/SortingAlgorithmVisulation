
import time
from tkinter import *
from tkinter import ttk

# Global değişkenler
comparisonCount = 0
sorting_stopped = False

def partition(data, head, tail, drowData, timeTick, root, comparisonLabel, varG):
    global comparisonCount
    border = head
    pivot = data[tail]

    drowData(data, ColorArray(len(data), head, tail, border, border), varG.get())
    root.after(timeTick)
    for j in range(head, tail):
        if sorting_stopped:
            return

        if data[j] < pivot:
            drowData(data, ColorArray(len(data), head, tail, border, j, True), varG.get())
            root.after(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drowData(data, ColorArray(len(data), head, tail, border, j), varG.get())
        root.after(timeTick)

        # Karşılaştırma sayısını güncelle
        comparisonCount += 1
        comparisonLabel.config(text="Karşılaştırma: " + str(comparisonCount))

    drowData(data, ColorArray(len(data), head, tail, border, True), varG.get())
    root.after(timeTick)
    data[border], data[tail] = data[tail], data[border]

    return border

def quickSort(data, head, tail, drowData, timeTick, root, comparisonLabel, varG):
    global sorting_stopped

    if sorting_stopped:
        return

    if head < tail:
        partitionIdx = partition(data, head, tail, drowData, timeTick, root, comparisonLabel, varG)

        quickSort(data, head, partitionIdx - 1, drowData, timeTick, root, comparisonLabel, varG)
        quickSort(data, partitionIdx + 1, tail, drowData, timeTick, root, comparisonLabel, varG)

def ColorArray(dataLen, head, tail, border, currIdx, isSwapping=False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('blue')
        if i == tail:
            colorArray[i] = 'orange'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border and i == currIdx:
                colorArray[i] = 'green'
    return colorArray

def stopSorting():
    global sorting_stopped
    sorting_stopped = True