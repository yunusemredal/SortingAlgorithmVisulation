import time
from tkinter import *
from tkinter import ttk
sorting_stopped = False
def insertionSort(data, drowData, timeTick, root, timeLabel, comparisonLabel, varG):
    global comparisonCount
    global startTime

    comparisonCount = 0
    startTime = time.time()

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            comparisonCount += 1
            data[j + 1] = data[j]
            j -= 1
            drowData(data, ['yellow' if x == j + 1 else 'red' for x in range(len(data))], varG.get())
            root.update()
            root.after(timeTick)

            # Animasyonu durdurma kontrolü
            if sorting_stopped:
                return

        data[j + 1] = key

        # Animasyonu durdurma kontrolü
        if sorting_stopped:
            return

    # Karmaşıklık zamanını hesapla
    endTime = time.time()
    totalTime = endTime - startTime
    timeLabel.config(text="Zamanı: {:.2f} s".format(totalTime))

    # Karşılaştırma sayısını güncelle
    comparisonLabel.config(text="Karşılaştırma: " + str(comparisonCount))

def stopSorting():
    global sorting_stopped
    sorting_stopped = True


