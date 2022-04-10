import random
import os
import sys
import matplotlib
import matplotlib.pyplot as plt

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def create_list_from_range(size):
    list = []
    while(len(list) < size):
        list.append(random.randint(1,1*size))
    return list


matplotlib.use('Agg')
def draw_graph(x,y,z, name):    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,z, label = "Pior Tempo")    
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.xlabel('Tamanho')
    plt.ylabel('tempo')      
    fig.savefig(f'sorting/graphs/{name}.png')