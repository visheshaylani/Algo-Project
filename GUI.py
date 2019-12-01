import tkinter as tk
import os
import sys
from PIL import ImageTk,Image

def dijkstrafunction():
    os.system('python dijkstra.py')
    
def pirmsfunction():
    os.system('python prims.py')
    
def bellmanFordfunction():
    os.system('python bellman_Ford.py')
    
def kruskalfunction():
    os.system('python kruskal.py')
    
def floydfunction():
    os.system('python floyd.py')

def clusterfunction():
    os.system('python clustering.py')

def originalfunction():
    os.system('python original.py')
    
path=("graph.jpg")

root = tk.Tk()
root.geometry('450x300')
root.configure(background='white')
img = ImageTk.PhotoImage(Image.open(path))
panel =tk.Label(root,image = img)


panel.place(x=0,y=0)
button = tk.Button(root, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
#button.pack(side=tk.LEFT)
button.place(x=200,y=197)
slogan = tk.Button(root,
                   text="Dijkstra",
                   command=dijkstrafunction)
#slogan.pack(side=tk.LEFT)
slogan.place(x=200,y=27)
slogan = tk.Button(root,
                   text="Pirms",
                   command=pirmsfunction)
slogan.place(x=200,y=85)
slogan = tk.Button(root,
                   text="bellman_Ford",
                   command=bellmanFordfunction)
slogan.place(x=200,y=55)
slogan = tk.Button(root,
                   text="kruskal",
                   command=kruskalfunction)
slogan.place(x=200,y=112)
slogan = tk.Button(root,
                   text="Floyd_Warshall",
                   command=floydfunction)
slogan.place(x=200,y=139)
slogan = tk.Button(root,
                   text="Local Clustering Coefficient",
                   command=clusterfunction)
slogan.place(x=200,y=166)
slogan = tk.Button(root,
                   text="Original Graph",
                   command=originalfunction)
slogan.place(x=200,y=0)

root.mainloop()