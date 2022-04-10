import random
import matplotlib
import matplotlib.pyplot as plt
import timeit


list = [1000,2000,3000,4000,5000,8000,11000,15000]

def create_list_from_range(size):
    list = []
    while(len(list) < size):
        list.append(random.randint(1,1*size))
    return list

def bubble_sort(arr):
    arrLen = len(arr)
    for j in range(arrLen-1):
        for i in range(arrLen-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]


matplotlib.use('Agg')
def draw_graph(x,y,z):    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,z, label = "Pior Tempo")    
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.xlabel('Tamanho')
    plt.ylabel('tempo')      
    fig.savefig('graph.png')

Best_case = []
Worst_case = []

for i in list:
  random_list = create_list_from_range(i)
  best_case = sorted(random_list)
  worst_case = sorted(random_list, reverse=True)
  Best_case.append(timeit.timeit("bubble_sort({})".format(best_case),setup="from __main__ import bubble_sort",number=1))
  Worst_case.append(timeit.timeit("bubble_sort({})".format(worst_case),setup="from __main__ import bubble_sort",number=1))

draw_graph(list,Best_case,Worst_case)