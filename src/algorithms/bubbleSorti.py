import time
from tkinter import *
from tkinter import ttk


sorting_stopped = False

def bubbleSort(data, drowData, timeTick, comparisonLabel, timeLabel, root, varG):
    global sorting_stopped

    comparisons = 0
    isSwapped = False
    i = 0

    start_time = time.time()  # Başlangıç zamanını kaydet

    def innerBubbleSort():
        nonlocal i, isSwapped, comparisons

        if i < len(data) - 1:
            isSwapped = False
            for j in range(len(data) - i - 1):
                if sorting_stopped:
                    return

                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    drowData(data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))], varG.get())

                    isSwapped = True
                comparisons += 1
                comparisonLabel.config(text="Karşılaştırma: " + str(comparisons))

            if not isSwapped:
                drowData(data, ['green' for x in range(len(data))], varG.get())
                end_time = time.time()  # Bitiş zamanını kaydet
                elapsed_time = end_time - start_time  # Geçen süreyi hesapla
                timeLabel.config(text="Zamanı: {:.2f} s".format(elapsed_time))
                return

            i += 1
            root.after(timeTick, innerBubbleSort)
        else:
            drowData(data, ['green' for x in range(len(data))], varG.get())
            end_time = time.time()  # Bitiş zamanını kaydet
            elapsed_time = end_time - start_time  # Geçen süreyi hesapla
            timeLabel.config(text="Zamanı: {:.2f} s".format(elapsed_time))

    innerBubbleSort()

def stopSorting():
    global sorting_stopped
    sorting_stopped = True


