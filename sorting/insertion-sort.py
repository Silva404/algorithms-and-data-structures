
import timeit
from utils import create_list_from_range, draw_graph

list = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


Best_case = []
Worst_case = []

for i in list:
    random_list = create_list_from_range(i)
    best_case = sorted(random_list)
    worst_case = sorted(random_list, reverse=True)
    Best_case.append(timeit.timeit("insertion_sort({})".format(
        best_case), setup="from __main__ import insertion_sort", number=1))
    Worst_case.append(timeit.timeit("insertion_sort({})".format(
        worst_case), setup="from __main__ import insertion_sort", number=1))

draw_graph(list, Best_case, Worst_case, 'insertion-sort-graph')
