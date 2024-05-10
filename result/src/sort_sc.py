# -- coding: utf-8 --
"""
Created on Tue Apr 30 11:40:12 2024

@author: 2acffb24
"""
import random
import time


def insertionsort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def selectionsort(arr, n):
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if (arr[j] < arr[index]):
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr


def record_time(pc, start_n, end_n, step_n):
    x = [0]
    y_i = [0.0]
    y_s = [0.0]
    for n in range(start_n, end_n + 1, step_n):
        if pc == 'worst':
            array = list(range(n, 0, -1))
        else:
            array = list(range(1, n + 1))
        if pc == 'average':
            random.shuffle(array)
        x.append(n)
        start_time = time.time()
        insertionsort(array[:], n)
        insertion_time = time.time()
        y_i.append((start_time, insertion_time))
        start_time = time.time()
        selectionsort(array[:], n)
        selection_time = time.time()
        y_s.append((start_time, selection_time))
    return x, y_i, y_s


if __name__ == '__main__':
    with open('space_complexity_data_1.txt', mode='w') as scd:
        # cases_list = ['worst', 'best', 'average']
        cases_list = ['average']
        for pc in cases_list:
            record_result = record_time(pc, 1000, 9000, 1000)
            scd.write('%s: %s\n' % (pc, record_result))
