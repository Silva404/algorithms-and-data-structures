from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import timeit


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if (arr[j])