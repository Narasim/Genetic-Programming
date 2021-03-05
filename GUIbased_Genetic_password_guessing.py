# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 01:29:47 2021

@author: TOSHIBA
"""

import random
import datetime
import tkinter as tk
from tkinter import ttk

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
canvas = tk.Tk()
canvas.title("Genetic Password Guessing")
text_label = ttk.Label(canvas, text = "Genetic Password Guessing")
text_label_1 = ttk.Label(canvas, text = "Enter Your Name: ").grid(column = 0, row = 1)
text_label_2 = ttk.Label(canvas, text = "Guessed Password: ")
text_label_3 = ttk.Label(canvas, text = "Fitness:  ")
text_label_4 = ttk.Label(canvas, text = "Time to Guess ")
text_variable = tk.StringVar()
text_entry = ttk.Entry(canvas, width = 15, textvariable = text_variable)
text_entry.grid(column = 1, row = 1)
def change_greeting():
    temp = str(text_variable.get())
    random.seed()
    target =  temp
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent, target)
    while True:
        child = mutate(bestParent)
        childFitness = get_fitness(child, target)
        if bestFitness >= childFitness:
            continue
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(bestParent, target)
    text_label_2.configure(text = "Guessed Password: " + child)
    text_label_3.configure(text = "Fitness: " + str(fitness))
    text_label_4.configure(text = "Time to Guess: " + str(timeDiff))
def generate_parent(length):
    genes = []
    genes.extend(random.sample(geneSet, length))
    return ''.join(genes)

def get_fitness(guess, target):
    sum = 0
    for i in range(len(guess)):
        if(guess[i] == target[i]):
            sum+=1
    return sum
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    alternate = random.sample(geneSet, 1)
    childGenes[index] = alternate[0]
    return ''.join(childGenes)

event_button = ttk.Button(canvas, text="Click me and see what happens", command = change_greeting).grid(column = 2, row = 1)
text_label.grid(column = 0, row = 0)
text_label_2.grid(column = 0, row = 2)
text_label_3.grid(column = 0, row = 3)
text_label_4.grid(column = 0, row = 4)
canvas.resizable(False, False)
canvas.mainloop()