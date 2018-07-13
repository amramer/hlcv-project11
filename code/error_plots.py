#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 18:32:35 2018

@author: ishwar
"""

import numpy as np
import matplotlib.pyplot as plt

train_eval = "/home/ishwar/Volume/masters/hlcv18/project/data/full_all_04_07_2018/eval_metrics.txt"
test_eval = "/home/ishwar/Volume/masters/hlcv18/project/data/full_all_04_07_2018/eval_metrics_test.txt"

title = "Evaluation Metrics for Tumor Segmentation on BraTS 2017"

pltfile = "/home/ishwar/Volume/masters/hlcv18/project/data/full_all_04_07_2018/eval_plot.jpg"

def plot_train_test_metric(train, test, metric,ax = None, ylim = [0, 0.5]):
    
    """Plot train and test evaluation metric on prescribed axis"""

    
    if(len(train) != len(test)):
        raise ValueError("Length of Train and test evaluation metrics different")
        
    if(ax is None):
        fig = plt.figure()
        ax = fig.add_subplot(111)

    nepochs = len(train)
    
    ax.plot(range(nepochs), train, 'b-', label = "train")
    ax.plot(range(nepochs), test, 'r-', label = "test")
    ax.set_title(metric)
    ax.set_xlabel("Epochs")
    ax.set_ylabel(metric)
    ax.minorticks_on()
    ax.grid(linestyle = '--')
    ax.set_xlim([0, len(train)-1])
    ax.set_ylim(ylim)
    

# Import error metrics
train_metrics = np.loadtxt(train_eval)
test_metrics = np.loadtxt(test_eval)

# Get individual metrics
sdice_train = train_metrics[:,0]
hdice_train = train_metrics[:,1]
iou_train = train_metrics[:,2]

sdice_test = test_metrics[:,0]
hdice_test = test_metrics[:,1]
iou_test = test_metrics[:,2]

# Plot every value in 3 subpltos
fig = plt.figure(1)

# plot 1-softdice
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
plot_train_test_metric(train = sdice_train, test = sdice_test, metric = r'$1-dice$', ax = ax1, ylim = [0, 0.5])
plot_train_test_metric(train = hdice_train, test = hdice_test, metric = r'$hdice$', ax = ax2, ylim = [0, 1])
plot_train_test_metric(train = iou_train, test = iou_test, metric = r'$iou$', ax = ax3, ylim = [0,1])
ax1.legend()
plt.suptitle(title)
fig.set_figheight(9)
fig.set_figwidth(9)
fig.savefig(pltfile)