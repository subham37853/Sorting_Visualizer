import time

def partition(data, head, tail, drawData, timeTik):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTik)
    for j in range(head , tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTik)

            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTik)
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTik)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawData, timeTik):
    if head < tail:
        partitionIndex = partition(data,head, tail, drawData, timeTik)

        #left sort
        quick_sort(data, head, partitionIndex-1, drawData, timeTik)
        #right sort
        quick_sort(data, partitionIndex+1, tail, drawData, timeTik)

def getColorArray(datalen, head, tail, border, curr_ind, isSwapping = False):
    colorArray = []
    for i in range(datalen):
        if i >= head and i <= tail:
            colorArray.append('grey')
        else:
            colorArray.append('white')
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == curr_ind:
            colorArray[i] = 'yellow'
        if isSwapping:
            if i == border or i == curr_ind:
                colorArray[i] = 'green' 
    return colorArray
