
import timeit
from utils import create_list_from_range, draw_graph

list = [1000,2000,3000,4000,5000,8000,11000,15000]

def bubble_sort(arr):
    arrLen = len(arr)
    for j in range(arrLen-1):
        for i in range(arrLen-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]

Best_case = []
Worst_case = []

for i in list:
  random_list = create_list_from_range(i)
  best_case = sorted(random_list)
  # The worst situation for bubble sort is when the list's smallest element is in the last position. 
  # In this situation, the smallest element will move down one place on each pass through the list, 
  # meaning that the sort will need to make the maximum number of passes through the list, namely n - 1.
  worst_case = sorted(random_list, reverse=True)
  Best_case.append(timeit.timeit("bubble_sort({})".format(best_case),setup="from __main__ import bubble_sort",number=1))
  Worst_case.append(timeit.timeit("bubble_sort({})".format(worst_case),setup="from __main__ import bubble_sort",number=1))

draw_graph(list,Best_case,Worst_case, 'bubble-sort-graph')