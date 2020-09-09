# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:39:33 2020

@author: Tejas
"""
#%% Imports
import numpy as np
import matplotlib.pyplot as plt
#import scipy.io
#from ipywidgets import interact, interactive, fixed, interact_manual
#import ipywidgets as widgets
#import scipy.stats as stat
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
#from multiprocessing import Pool
#from scipy import stats
#import math
#from scipy.ndimage import gaussian_filter1d
#import statsmodels.api as sm
#from statsmodels.formula.api import ols
#import itertools
#from functools import partial
import pickle
#import scipy
#import scipy.optimize
from dual_model_rts import get_times
#from dual_model_alpha import dual_model_sudden, dual_model_gradual
from dual_model import dual_model_sudden, dual_model_gradual

#%% Load Fits and curvatures
curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
its, mts = get_times()
#fits = pickle.load(open('fit_dual_bound_alphaed.pickle', 'rb'))
#Af, Bf, As, Bs, alpha, V = fits[:, 0], fits[:, 1], fits[:, 2], fits[:, 3], fits[:, 4], fits[:, 5]

#%% Plotting functions

def plot_data_vs_fits_dual_alphaed(Af, Bf, As, Bs, alpha):
    print (alpha)
    plt.figure(figsize = (20, 10))
    errors_predict = np.zeros((60, 704))
    fast = np.zeros((60, 704))
    slow = np.zeros((60, 704))
    rotation_est = np.zeros((60, 704))
    for participant in range(60):
        if participant % 4 == 0 or participant%4 == 1:
            errors_predict[participant][:640], rotation_est[participant][:640], fast[participant][:640], slow[participant][:640] = dual_model_sudden(640,  Af[participant], Bf[participant], As[participant], Bs[participant], alpha[participant])

        else:    
            errors_predict[participant][:640], rotation_est[participant][:640], fast[participant][:640], slow[participant][:640] = dual_model_gradual(640,  Af[participant], Bf[participant], As[participant], Bs[participant], alpha[participant])

        errors_predict[participant][640:], rotation_est[participant][640:], fast[participant][640:], slow[participant][640:] = dual_model_sudden(64, Af[participant], Bf[participant], As[participant], Bs[participant], alpha[participant])
        #rotation_est[participant][640:] = -rotation_est[participant][640:]
    #print (rotation_est[participant-2][639], rotation_est[participant-2][640])
    #print (rotation_est[1][640:])    
    for participant in range(4):
        if participant % 4 == 0 or participant%4 == 1:
            plt.subplot(4, 1, participant + 1 )
            #plt.plot(np.nanmean(errors_predict[participant::4], axis = 0))
            plt.plot(np.nanmean(rotation_est[participant::4], axis = 0))
            plt.plot(np.nanmean(alpha[participant::4]*fast[participant::4], axis = 0))
            plt.plot(np.nanmean((1-alpha[participant::4])*slow[participant::4], axis = 0))
            #plt.plot(np.append(np.ravel(np.nanmean(curvatures_smooth[participant::4], axis = 0)[1:-1]), np.ravel(np.nanmean(curvatures_smooth[participant::4], axis = 0)[11])))
        else:
            plt.subplot(4, 1, participant + 1 )
            #plt.plot(np.nanmean(errors_predict[participant::4], axis = 0))    
            plt.plot(np.nanmean(rotation_est[participant::4], axis = 0))
            plt.plot(np.nanmean(alpha[participant::4]*fast[participant::4], axis = 0))
            plt.plot(np.nanmean((1 - alpha[participant::4])*slow[participant::4], axis = 0))
            #plt.plot(np.append(np.ravel(np.nanmean(curvatures_smooth[participant::4], axis = 0)[1:-1]), np.ravel(np.nanmean(curvatures_smooth[participant::4], axis = 0)[11])))
        plt.ylim((-100, 150))
        
        
def plot_data_vs_fits_dual(Af, Bf, As, Bs):
    plt.figure(figsize = (20, 10))
    errors_predict = np.zeros((60, 704))
    fast = np.zeros((60, 704))
    slow = np.zeros((60, 704))
    rotation_est = np.zeros((60, 704))
    corr_coef = np.zeros(60)
    for participant in range(60):
        if participant % 4 == 0 or participant%4 == 1:
            errors_predict[participant][:640], rotation_est[participant][:640], fast[participant][:640], slow[participant][:640] = dual_model_sudden(640, Af[participant], Bf[participant], As[participant], Bs[participant])
            corr_coef[participant] = np.ma.corrcoef(errors_predict[participant][:640], np.ravel(curvatures_smooth[participant])[64:704])[0, 1]
        else:    
            errors_predict[participant][:640], rotation_est[participant][:640], fast[participant][:640], slow[participant][:640] = dual_model_gradual(640, Af[participant], Bf[participant], As[participant], Bs[participant])
            corr_coef[participant] = np.ma.corrcoef(errors_predict[participant][:640], np.ravel(curvatures_smooth[participant])[64:704])[0, 1]

        errors_predict[participant][640:], rotation_est[participant][640:], fast[participant][640:], slow[participant][640:] = dual_model_sudden(64, Af[participant], Bf[participant], As[participant], Bs[participant])
        #rotation_est[participant][640:] = -rotation_est[participant][640:]
    #print (rotation_est[participant-2][639], rotation_est[participant-2][640])
    #print (rotation_est[1][640:])    
    fig, ax = plt.subplots(4, dpi = 300, sharex = True, constrained_layout = True, figsize = (25, 15))
    plt.setp(ax, ylim=(-100, 100))
    legend_size = 15
    
    for participant in range(4):
        if participant % 4 == 0 or participant%4 == 1:
            #plt.plot(np.nanmean(errors_predict[participant::4], axis = 0))
            l1, = ax[participant].plot(np.append(np.nanmean(rotation_est[participant::4], axis = 0)[:640], -np.nanmean(rotation_est[participant::4], axis = 0)[640:] + np.nanmean(rotation_est[participant::4], axis = 0)[639]))
            l2, = ax[participant].plot(np.append(np.nanmean(fast[participant::4], axis = 0)[:640], -np.nanmean(fast[participant::4], axis = 0)[640:] + np.nanmean(fast[participant::4], axis = 0)[639]))
            l3, = ax[participant].plot(np.append(np.nanmean(slow[participant::4], axis = 0)[:640], -np.nanmean(slow[participant::4], axis = 0)[640:] + np.nanmean(slow[participant::4], axis = 0)[639]))
            l4, = ax[participant].plot(np.append(np.ravel(np.nanmean(90 - curvatures_smooth[participant::4], axis = 0)[1:-1]), np.ravel(np.nanmean(curvatures_smooth[participant::4], axis = 0)[11])))
            ax[participant].legend([l1, l2, l3, l4], ['Rotation Est', 'Fast Est', 'Slow Est', 'Rotation Est Data'], prop={'size': legend_size})
        else:
            #plt.subplot(4, 1, participant + 1 )
            #plt.plot(np.nanmean(errors_predict[participant::4], axis = 0))
            l1, = ax[participant].plot(np.append(np.nanmean(rotation_est[participant::4], axis = 0)[:640], -np.nanmean(rotation_est[participant::4], axis = 0)[640:] + np.nanmean(rotation_est[participant::4], axis = 0)[639]))
            l2, = ax[participant].plot(np.append(np.nanmean(fast[participant::4], axis = 0)[:640], -np.nanmean(fast[participant::4], axis = 0)[640:] + np.nanmean(fast[participant::4], axis = 0)[639]))
            l3, = ax[participant].plot(np.append(np.nanmean(slow[participant::4], axis = 0)[:640], -np.nanmean(slow[participant::4], axis = 0)[640:] + np.nanmean(slow[participant::4], axis = 0)[639]))
            cs = np.zeros((704))
            csm = np.nanmean(curvatures_smooth[participant::4], axis = 0)
            for i in range(9):
                cs[i*64:(i+1)*64] = (i+1)*10 - csm[i+1]
            cs[576:640] = 90 - csm[10]
            cs[640:] = csm[11]
            l4, = ax[participant].plot(cs)
            #plt.plot(np.append(np.ravel(np.nanmean(90 - curvatures_smooth[participant::4], axis = 0)[1:-1]), -np.ravel(np.nanmean(curvatures_smooth[participant::4], axis = 0)[11])))
            ax[participant].legend([l1, l2, l3, l4], ['Rotation Est', 'Fast Est', 'Slow Est', 'Rotation Est Data'], prop = {'size' : legend_size})
        ax[participant].plot(np.zeros(704), color = 'black')
        ax[0].set_ylabel('Sudden \n Speed', fontsize = 15)
        ax[1].set_ylabel('Sudden \n Accuracy', fontsize = 15)
        ax[2].set_ylabel('Gradual \n Speed', fontsize = 15)
        ax[3].set_ylabel('Gradual \n Accuracy', fontsize = 15)
        return corr_coef
        
#%% Load Parameters for Dual bound model
fits = pickle.load(open('fit_dual_bound.pickle', 'rb'))
Af, Bf, As, Bs, V = fits[:, 0], fits[:, 1], fits[:, 2], fits[:, 3], fits[:, 4]
#V, Af, Bf, As, Bs = V[:, 0], Af[:, 0], Bf[:, 0], As[:, 0], Bs[:, 0]
#%%
corr_coef = plot_data_vs_fits_dual(Af, Bf, As, Bs)

#%%
cc = np.corrcoef(np.mean(np.mean(curvatures_smooth[2::4, 1:4, :], axis = 2), axis = 1), np.mean(np.mean(its[2::4, 1:4, :], axis = 2), axis = 1))
plt.scatter(np.mean(np.mean(curvatures_smooth[2::4, 1:4, :], axis = 2), axis = 1), np.mean(np.mean(its[2::4, 1:4, :], axis = 2), axis = 1))
plt.text(60, 2.25, 'Sudden Accuracy: -2.3')
plt.xlabel('Angular Error')
plt.ylabel('RT')