# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:36:53 2024

@author: 2acffb24
"""
import matplotlib.pyplot as plt


def plot_figure(rr):
    plt.figure(figsize=(8, 5), dpi=480)
    plt.plot(rr[0], rr[1], marker='o', color='blue', linestyle='-',
             linewidth=2, label='Insertion sort')
    plt.plot(rr[0], rr[2], marker='o', color='red', linestyle='--',
             linewidth=2, label='Selection sort')
    plt.xlabel('Input size n')
    plt.ylabel('Memory used (in MiB)')
    plt.grid(True)
    plt.legend()
    plt.savefig(f'figure_space_2.svg')
    plt.savefig(f'figure_space_2.png')


if __name__ == '__main__':
    list_0 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
    list_1 = [11.769531, 11.824219, 11.9375, 11.964844, 12.113281, 12.226562, 12.296875, 12.367188, 12.4375]
    list_2 = [11.769531, 11.824219, 11.9375, 11.964844, 12.113281, 12.226562, 12.296875, 12.367188, 12.4375]
    list_c = (list_0, list_1, list_2)
    plot_figure(list_c)
