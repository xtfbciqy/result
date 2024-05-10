# -- coding: utf-8 --
"""
Created on Tue Apr 30 11:40:12 2024

@author: 2acffb24
"""
import matplotlib.pyplot as plt
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
        start_time = time.time()
        insertionsort(array[:], n)
        insertion_time = time.time() - start_time
        start_time = time.time()
        selectionsort(array[:], n)
        selection_time = time.time() - start_time
        x.append(n)
        y_i.append(insertion_time)
        y_s.append(selection_time)
    return x, y_i, y_s


def plot_figure(pc, rr):
    plt.figure(figsize=(8, 5), dpi=480)
    plt.plot(rr[0], rr[1], marker='o', color='blue', linestyle='-',
             linewidth=2, label='Insertion sort')
    plt.plot(rr[0], rr[2], marker='o', color='red', linestyle='--',
             linewidth=2, label='Selection sort')
    plt.xlabel('Input size n')
    plt.ylabel('Operating time (s)')
    plt.grid(True)
    plt.legend()
    plt.savefig(f'figure_{pc}.svg')
    plt.savefig(f'figure_{pc}.png')


if __name__ == '__main__':
    with open('SortingData.txt') as f:
        original_array = [int(line) for line in f]
        n = len(original_array)
    with open('insertionsort.txt', mode='w') as t0:
        for i in insertionsort(original_array[:], n):
            t0.write('%4d\n' % i)
    with open('selectionsort.txt', mode='w') as t1:
        for i in selectionsort(original_array[:], n):
            t1.write('%4d\n' % i)
    with open('time_complexity_data.txt', mode='w') as tcd:
        cases_list = ['worst', 'best', 'average']
        for pc in cases_list:
            record_result = record_time(pc, 1000, 20000, 1000)
            plot_figure(pc, record_result)
            tcd.write('%s: %s\n' % (pc, record_result))
