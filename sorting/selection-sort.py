
import timeit
from utils import create_list_from_range, draw_graph

list = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]


def selection_sort(arr):
    arrLen = len(arr)
    for j in range(arrLen - 1):
        min_idx = j
        for i in range(arrLen):
            if (arr[i] < arr[min_idx]):
                min_idx = i
            if (arr[j] > arr[min_idx]):
                aux = arr[min]
                arr[min] = arr[i]
                arr[i] = aux
    return arr


Best_case = []
Worst_case = []

for i in list:
    random_list = create_list_from_range(i)
    best_case = sorted(random_list)
    # If we have n values in our array, Selection Sort has a time complexity of O(n²) in the worst case. In the best case, 
    # we already have a sorted array but we need to go through the array O(n²) times to be sure! 
    # Therefore Selection Sort's best and worst case time complexity are the same.
    worst_case = sorted(random_list, reverse=True)
    Best_case.append(timeit.timeit("selection_sort({})".format(
        best_case), setup="from __main__ import selection_sort", number=1))
    Worst_case.append(timeit.timeit("selection_sort({})".format(
        worst_case), setup="from __main__ import selection_sort", number=1))

draw_graph(list, Best_case, Worst_case, 'selection-sort-graph')
