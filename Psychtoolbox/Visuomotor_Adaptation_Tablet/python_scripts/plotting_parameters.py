# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:48:29 2020

@author: Tejas
"""
import numpy as np
import matplotlib.pyplot as plt
import pickle
import scipy.stats as stat

#%% Plot one parameter vs other for all conditions
def plot_fits(fit_A, fit_B, x_label, y_label):
    x = np.array([np.nanmean(fit_A[0::4]), np.nanmean(fit_A[1::4]), np.nanmean(fit_A[2::4]), np.nanmean(fit_A[3::4])])
    y = np.array([np.nanmean(fit_B[0::4]), np.nanmean(fit_B[1::4]), np.nanmean(fit_B[2::4]), np.nanmean(fit_B[3::4])])
    x_err = np.array([stat.sem(fit_A[0::4]), stat.sem(fit_A[1::4]), stat.sem(fit_A[2::4]), stat.sem(fit_A[3::4])])
    y_err = np.array([stat.sem(fit_B[0::4]), stat.sem(fit_B[1::4]), stat.sem(fit_B[2::4]), stat.sem(fit_B[3::4])])
    #x_err = np.array([stat.tstd(fit_A[0::4, :], axis = 0), stat.tstd(fit_A[1::4, :], axis = 0), stat.tstd(fit_A[2::4, :], axis = 0), stat.tstd(fit_A[3::4, :], axis = 0)])
    #y_err = np.array([stat.tstd(fit_B[0::4, :], axis = 0), stat.tstd(fit_B[1::4, :], axis = 0), stat.tstd(fit_B[2::4, :], axis = 0), stat.tstd(fit_B[3::4, :], axis = 0)])

    #x_conf_interval = np.array(stat.norm.interval(0.83, loc = x, scale = x_err))
    #y_conf_interval = np.array(stat.norm.interval(0.83, loc = y, scale = y_err))
    x_CI = x - np.array(stat.norm.interval(0.95, loc = x, scale = x_err))[0, :], np.array(stat.norm.interval(0.95, loc = x, scale = x_err))[1, :] - x
    y_CI = y - np.array(stat.norm.interval(0.95, loc = y, scale = y_err))[0, :], np.array(stat.norm.interval(0.95, loc = y, scale = y_err))[1, :] - y

    print (np.shape(x_CI))
    #print (x_conf_interval[:, 0])
    #plt.errorbar(x, y, xerr = x_err, yerr = y_err, linestyle = 'None', capsize = 3)
    plot0 = plt.errorbar(x[0], y[0], xerr = [x_CI[0][0], x_CI[1][0]], yerr = [y_CI[0][0], y_CI[1][0]], capsize = 3)
    plot1 = plt.errorbar(x[1], y[1], xerr = [x_CI[0][1], x_CI[1][1]], yerr = [y_CI[0][1], y_CI[1][1]], capsize = 3)
    plot2 = plt.errorbar(x[2], y[2], xerr = [x_CI[0][2], x_CI[1][2]], yerr = [y_CI[0][2], y_CI[1][2]], capsize = 3)
    plot3 = plt.errorbar(x[3], y[3], xerr = [x_CI[0][3], x_CI[1][3]], yerr = [y_CI[0][3], y_CI[1][3]], capsize = 3)

    #plot0 = plt.scatter(fit_A[0::4], fit_B[0::4])
    #plot1 = plt.scatter(fit_A[1::4], fit_B[1::4])
    #plot2 = plt.scatter(fit_A[2::4], fit_B[2::4])
    #plot3 = plt.scatter(fit_A[3::4], fit_B[3::4])

    plt.legend((plot0, plot1, plot2, plot3), ('Sudden Speed', 'Sudden Accuracy', 'Gradual Speed', 'Gradual Accuracy'))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
#%% Plot one parameter vs other for emphasis or rotation
def plot_fits_rotation(fit_A, fit_B, x_label, y_label):
    x = np.array([np.mean(np.concatenate((fit_A[0::4], fit_A[1::4])), axis = 0),np.mean(np.concatenate((fit_A[2::4], fit_A[3::4])), axis = 0)])
    y = np.array([np.mean(np.concatenate((fit_B[0::4], fit_B[1::4])), axis = 0),np.mean(np.concatenate((fit_B[2::4], fit_B[3::4])), axis = 0)])
    x_err = np.array([stat.sem(np.concatenate((fit_A[0::4], fit_A[1::4])), axis = 0),stat.sem(np.concatenate((fit_A[2::4], fit_A[3::4])), axis = 0)])
    y_err = np.array([stat.sem(np.concatenate((fit_B[0::4], fit_B[1::4])), axis = 0), stat.sem(np.concatenate((fit_B[2::4], fit_B[3::4])), axis = 0)])
    #x_err = np.array([stat.tstd(np.concatenate((fit_A[0::4], fit_A[1::4])), axis = 0),stat.tstd(np.concatenate((fit_A[2::4], fit_A[3::4])), axis = 0)])
    #y_err = np.array([stat.tstd(np.concatenate((fit_B[0::4], fit_B[1::4])), axis = 0), stat.tstd(np.concatenate((fit_B[2::4], fit_B[3::4])), axis = 0)])

    x_CI = x - np.array(stat.norm.interval(0.95, loc = x, scale = x_err))[0, :], np.array(stat.norm.interval(0.95, loc = x, scale = x_err))[1, :] - x
    y_CI = y - np.array(stat.norm.interval(0.95, loc = y, scale = y_err))[0, :], np.array(stat.norm.interval(0.95, loc = y, scale = y_err))[1, :] - y

    #x_conf_interval = np.array(stat.norm.interval(0.95, loc = x, scale = x_err))
    #y_conf_interval = np.array(stat.norm.interval(0.95, loc = y, scale = y_err))
    #plt.errorbar(x, y, xerr = x_err, yerr = y_err, linestyle = 'None', capsize = 3)
    #plot0 = plt.errorbar(x[0], y[0], xerr = x_err[0], yerr = y_err[0], capsize = 3)
    #plot0 = plt.scatter(np.concatenate((fit_A[0::4], fit_A[1::4])), np.concatenate((fit_B[0::4], fit_B[1::4])))

    #plot1 = plt.errorbar(x[1], y[1], xerr = x_err[1], yerr = y_err[1], capsize = 3)
    #plot1 = plt.scatter(np.concatenate((fit_A[2::4], fit_A[3::4])), np.concatenate((fit_B[2::4], fit_B[3::4])))
    plot0 = plt.errorbar(x[0], y[0], xerr = [x_CI[0][0], x_CI[1][0]], yerr = [y_CI[0][0], y_CI[1][0]], capsize = 3)
    plot1 = plt.errorbar(x[1], y[1], xerr = [x_CI[0][1], x_CI[1][1]], yerr = [y_CI[0][1], y_CI[1][1]], capsize = 3)

    #plot0 = plt.errorbar(x[0], y[0], xerr = x_conf_interval[:, 0], yerr = y_conf_interval[:, 0], capsize = 3)
    #plot1 = plt.errorbar(x[1], y[1], xerr = x_conf_interval[:, 1], yerr = y_conf_interval[:, 1], capsize = 3)
    #plot2 = plt.errorbar(x[2], y[2], xerr = x_conf_interval[:, 2], yerr = y_conf_interval[:, 2], capsize = 3)
    #plot3 = plt.errorbar(x[3], y[3], xerr = x_conf_interval[:, 3], yerr = y_conf_interval[:, 3], capsize = 3)

    plt.legend((plot0, plot1), ('Sudden', 'Gradual'))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
def plot_fits_emphasis(fit_A, fit_B, x_label, y_label):
    x = np.array([np.nanmean(fit_A[0::2, :], axis = 0), np.nanmean(fit_A[1::2, :], axis = 0)])#, np.nanmean(fit_A[2::4, :], axis = 0), np.nanmean(fit_A[3::4, :], axis = 0)])
    y = np.array([np.nanmean(fit_B[0::2, :], axis = 0), np.nanmean(fit_B[1::2, :], axis = 0)])#, np.nanmean(fit_B[2::4, :], axis = 0), np.nanmean(fit_B[3::4, :], axis = 0)])

    #x = np.array([np.nanmean(fit_A[0::2, :] - fit_A[1::2, :], axis = 0)])#, np.nanmean(fit_A[1::2, :], axis = 0)])#, np.nanmean(fit_A[2::4, :], axis = 0), np.nanmean(fit_A[3::4, :], axis = 0)])
    #y = np.array([np.nanmean(fit_B[0::2, :] - fit_B[1::2, :], axis = 0)])#, np.nanmean(fit_B[1::2, :], axis = 0)])#, np.nanmean(fit_B[2::4, :], axis = 0), np.nanmean(fit_B[3::4, :], axis = 0)])

    x_err = np.array([stat.sem(fit_A[0::2, :], axis = 0), stat.sem(fit_A[1::2, :], axis = 0)])#, stat.sem(fit_A[2::4, :], axis = 0), stat.sem(fit_A[3::4, :], axis = 0)])
    y_err = np.array([stat.sem(fit_B[0::2, :], axis = 0), stat.sem(fit_B[1::2, :], axis = 0)])#, stat.sem(fit_B[2::4, :], axis = 0), stat.sem(fit_B[3::4, :], axis = 0)])

    #x_err = np.array([stat.tstd(fit_A[0::2, :], axis = 0), stat.tstd(fit_A[1::2, :], axis = 0)])#, stat.sem(fit_A[2::4, :], axis = 0), stat.sem(fit_A[3::4, :], axis = 0)])
    #y_err = np.array([stat.tstd(fit_B[0::2, :], axis = 0), stat.tstd(fit_B[1::2, :], axis = 0)])#, stat.sem(fit_B[2::4, :], axis = 0), stat.sem(fit_B[3::4, :], axis = 0)])

    #x_conf_interval = np.array(stat.norm.interval(0.83, loc = x, scale = x_err))
    #y_conf_interval = np.array(stat.norm.interval(0.83, loc = y, scale = y_err))

    x_CI = x - np.array(stat.norm.interval(0.95, loc = x, scale = x_err))[0, :], np.array(stat.norm.interval(0.95, loc = x, scale = x_err))[1, :] - x
    y_CI = y - np.array(stat.norm.interval(0.95, loc = y, scale = y_err))[0, :], np.array(stat.norm.interval(0.95, loc = y, scale = y_err))[1, :] - y
    plot0 = plt.errorbar(x[0], y[0], xerr = [x_CI[0][0], x_CI[1][0]], yerr = [y_CI[0][0], y_CI[1][0]], capsize = 3)
    plot1 = plt.errorbar(x[1], y[1], xerr = [x_CI[0][1], x_CI[1][1]], yerr = [y_CI[0][1], y_CI[1][1]], capsize = 3)


    #plot0 = plt.errorbar(x[0], y[0], xerr = x_err[0], yerr = y_err[0], capsize = 3)
    #plot1 = plt.errorbar(x[1], y[1], xerr = x_err[1], yerr = y_err[1], capsize = 3)
    #plot0 = plt.errorbar(x[0], y[0], xerr = x_conf_interval[:, 0], yerr = y_conf_interval[:, 0], capsize = 3)
    #plot1 = plt.errorbar(x[1], y[1], xerr = x_conf_interval[:, 1], yerr = y_conf_interval[:, 1], capsize = 3)
    #plot2 = plt.errorbar(x[2], y[2], xerr = x_conf_interval[:, 2], yerr = y_conf_interval[:, 2], capsize = 3)
    #plot3 = plt.errorbar(x[3], y[3], xerr = x_conf_interval[:, 3], yerr = y_conf_interval[:, 3], capsize = 3)
    print (x[0], y[0])
    plt.legend((plot0, plot1), ('Speed', 'Accuracy'))#, 'Gradual Speed', 'Gradual Accuracy'))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
#%%
f = open('fit_dual_bound_alphaed.pickle', 'rb')
fits = pickle.load(f)
