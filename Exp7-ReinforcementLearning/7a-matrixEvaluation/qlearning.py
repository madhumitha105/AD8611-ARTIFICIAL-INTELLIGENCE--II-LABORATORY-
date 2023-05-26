import numpy as np 
import pylab as pl 
import networkx as nx  

edges = [(0, 1), (1, 5), (5, 6), (5, 4), (1, 2),  
         (1, 3), (9, 10), (2, 4), (0, 6), (6, 7), 
         (8, 9), (7, 8), (1, 7), (3, 9)]    

goal = 10 
G = nx.Graph() 
G.add_edges_from(edges) 
pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos) 
nx.draw_networkx_edges(G, pos) 
nx.draw_networkx_labels(G, pos) 
pl.show() 

MATRIX_SIZE = 11 
M = np.matrix(np.ones(shape =(MATRIX_SIZE, MATRIX_SIZE))) 
M *= -1    

for point in edges: 
    print(point) 
    if point[1] == goal: 
        M[point] = 100 
    else: 
        M[point] = 0    
    if point[0] == goal: 
        M[point[::-1]] = 100 
    else: 
        M[point[::-1]]= 0 
        # reverse of point  
 
M[goal, goal]= 100 
print(M) 
