import time
from tkinter import *
from tkinter import ttk

# Global değişkenler
comparisonCount = 0
startTime = 0
sorting_stopped = False

def mergeSort(data, drawData, timeTick, root, timeLabel, comparisonLabel, varG):
    global comparisonCount
    global startTime
    global sorting_stopped

    comparisonCount = 0
    startTime = time.time()
    sorting_stopped = False

    mergeAlgo(data, 0, len(data) - 1, drawData, timeTick, root, varG)

    # Karmaşıklık zamanını hesapla
    endTime = time.time()
    totalTime = endTime - startTime
    timeLabel.config(text="Zamanı: {:.2f} s".format(totalTime))

    # Karşılaştırma sayısını güncelle
    comparisonLabel.config(text="Karşılaştırma: " + str(comparisonCount))

def mergeAlgo(data, left, right, drawData, timeTick, root, varG):
    global sorting_stopped

    if sorting_stopped:
        return

    if left < right:
        mid = (left + right) // 2
        mergeAlgo(data, left, mid, drawData, timeTick, root, varG)
        mergeAlgo(data, mid + 1, right, drawData, timeTick, root, varG)
        merge(data, left, mid, right, drawData, timeTick, root, varG)

def merge(data, left, mid, right, drawData, timeTick, root, varG):
    global comparisonCount
    global sorting_stopped

    if sorting_stopped:
        return

    drawData(data, ColorArray(len(data), left, mid, right), varG.get())
    root.after(timeTick)
    leftPart = data[left:mid + 1].copy()
    rightPart = data[mid + 1:right + 1].copy()
    leftIdx = rightIdx = 0
    for dataIdx in range(left, right + 1):
        comparisonCount += 1
        if sorting_stopped:
            return
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if left <= x <= right else "white" for x in range(len(data))], varG.get())
    root.after(timeTick)

def ColorArray(length, left, mid, right):
    colorArray = []
    for i in range(length):
        if left <= i <= right:
            if left <= i <= mid:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("blue")
    return colorArray

def stopSorting():
    global sorting_stopped
    sorting_stopped = True


