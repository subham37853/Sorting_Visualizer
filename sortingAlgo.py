from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from QuickSort import quick_sort


root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900,600)
root.config(bg = 'black')

#variables

selected_algo = StringVar()
data = []



#functions

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    spacing = 10
    x_width = (c_width - 30) / (len(data) + 1)
    offset = 30
    
    normalisedData = [i/ max(data) for i in data]
    for i, height in enumerate(normalisedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height*340
        #bottom right
        x1 = (i+1)*x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        canvas.create_text(x0+2,y0, anchor = SW, text = str(data[i]))
    root.update_idletasks()

def StartAlogrithm():
    global data 
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1,drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())



def Generate():
    global data
    print("Algorithm Selected: " + selected_algo.get())
    minVal = int(MinEntry.get())
    maxVal = int(MaxEntry.get())
    size = int(sizeEntry.get())

    data = []

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data, ["blue" for x in range(len(data))])



#frames
UI_frame = Frame(root, width = 600, height = 200, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)
canvas = Canvas(root, width = 600, height = 380, bg = 'white')
canvas.grid(row = 1, column = 0,  padx = 10, pady = 5)

#UserInterface 

# Row 0
Label(UI_frame, text = "Algorithm: ", bg = 'grey').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_algo, values = ['Bubble Sort', 'Quick Sort'])
algMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient= HORIZONTAL, label = "Select Speed [s]")
speedScale.grid(row = 0, column = 2, padx = 5, pady = 5)


Button(UI_frame, text = "Start", command = StartAlogrithm, bg = 'green').grid(row = 0, column = 3, padx = 5, pady = 5)

# Row 1
sizeEntry = Scale(UI_frame, from_ = 3, to = 25,
                  resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column = 0, padx=5, pady=5)

MinEntry = Scale(UI_frame, from_=1, to=30,
                 resolution=1, orient=HORIZONTAL, label="Min Value")
MinEntry.grid(row=1, column=1, padx=5, pady=5)

MaxEntry = Scale(UI_frame, from_=30, to=100,
                 resolution=1, orient=HORIZONTAL, label="Max Value")
MaxEntry.grid(row=1, column = 2, padx=5, pady=5)


Button(UI_frame, text = "Generate", command = Generate, bg = 'white').grid(row = 1, column = 3, padx = 5, pady = 5)


root.mainloop()
