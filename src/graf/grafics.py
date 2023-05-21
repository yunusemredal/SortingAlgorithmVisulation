import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

def draw_bar_chart(normalized_data, colorArray, x_width, offset, spacing_bet_rect, canvas_height,canvas):
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

def draw_scatter_chart(normalized_data, colorArray, canvas_height, canvas_width,canvas,data):
    x_points = np.linspace(0, canvas_width, len(data))
    y_points = np.array(normalized_data) * canvas_height
    for x, y, color in zip(x_points, y_points, colorArray):
        canvas.create_oval(x - 2, canvas_height - y - 2, x + 2, canvas_height - y + 2, fill=color)

def draw_stem_chart(colorArray, canvas_height, canvas_width,canvas,data,normalized_data):
    x_points = np.linspace(0, canvas_width, len(data))
    y_points = np.array(normalized_data) * canvas_height
    for x, y, color in zip(x_points, y_points, colorArray):
        canvas.create_line(x, canvas_height, x, canvas_height - y, fill=color)
