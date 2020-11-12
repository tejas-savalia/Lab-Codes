# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:20:50 2020

@author: Tejas
"""

import numpy as np
import scipy.io
from multiprocessing import Pool
from functools import partial
import pickle
import scipy
import scipy.optimize
from sklearn.metrics import *
import scipy.stats as stat
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d



#%% Run this to compile dual state model functions

def model_sudden(num_trials, A, B):
    errors = np.zeros((num_trials))
    rotation = 90/90.0
    rotation_est = np.zeros((num_trials))
    for trial in range(num_trials - 1):
        if trial < 640:
            rotation = 90/90.0
            errors[trial] = rotation - rotation_est[trial]
            rotation_est[trial+1] = A*rotation_est[trial] + B*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial]
            rotation_est[trial+1] = A*rotation_est[trial] - B*errors[trial]
        #errors[trial] = rotation - rotation_est[trial]
    errors[num_trials-1] = rotation_est[num_trials-1]
    return errors, rotation_est

def model_gradual(num_trials, A, B):
    errors = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    rotation = 0
    for trial in range(num_trials - 1):
        if trial < 640:
            if trial%64 == 0:
                rotation = rotation + 10/90.0
            if rotation > 1.0:
                rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            rotation_est[trial+1] = A*rotation_est[trial] + B*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial]
            rotation_est[trial+1] = A*rotation_est[trial] - B*errors[trial]

    errors[num_trials-1] = rotation_est[num_trials-1]
    return errors, rotation_est

def residuals_sudden(params, num_trials, data_errors, train_indices):
    model_errors = model_sudden(num_trials, params[0], params[1])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    #residual_error = np.sum(np.square(model_errors_train - data_errors_train))
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[2]))

    if params[0] < 0 or params[1] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1:
        residual_error = residual_error + 10000000

    return residual_error

def residuals_gradual(params, num_trials, data_errors, train_indices):
    model_errors = model_gradual(num_trials, params[0], params[1])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    #residual_error = np.sum(np.square(model_errors_train - data_errors_train))
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[2]))
    if params[0] < 0 or params[1] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1:
        residual_error = residual_error + 10000000
    return residual_error



#%% Run this to compile fit routines
    
def fit_participant(participant, curvatures, num_fits):
    train_indices = np.random.choice(704, 634, replace = False)
    for fit_parts in range(num_fits):

        starting_points = np.array([[0.9, 0.2, 0.5]])
        for initial_point in starting_points:
            if participant%4 == 0 or participant%4 == 1:      
                #fits = scipy.optimize.minimize(residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3]], args = (640, np.nan_to_num(np.ravel(curvatures[participant][1:-1]), nan = np.nanmedian(curvatures[participant][1:-1]))), method = 'Nelder-Mead')            
                fits = scipy.optimize.basinhopping(residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2]], minimizer_kwargs={'args': (704, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})

                #if fits.fun < fit_V[participant][fit_parts]:
                A = fits.x[0]#fit_Af[participant][fit_parts] = fits.x[0]
                B = fits.x[1]#fit_Bf[participant][fit_parts] = fits.x[1]
                epsilon = fits.x[2]
                V = fits.fun#fit_V[participant][fit_parts] = fits.fun
                #fit_success[participant][fit_parts] = fits.success                
            else:
                #fits = scipy.optimize.minimize(residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3]], args = (640, np.nan_to_num(np.ravel(curvatures[participant][1:-1]), nan = np.nanmedian(curvatures[participant][1:-1]))), method = 'Nelder-Mead')         
                fits = scipy.optimize.basinhopping(residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2]], minimizer_kwargs={'args': (704, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})
                #if fits.fun < fit_V[participant][fit_parts]:
                A = fits.x[0]#fit_Af[participant][fit_parts] = fits.x[0]
                B = fits.x[1]#fit_Bf[participant][fit_parts] = fits.x[1]
                epsilon = fits.x[2]
                V = fits.fun#fit_V[participant][fit_parts] = fits.fun
                #fit_success[participant][fit_parts] = fits.success
            print (participant, V)
    return A, B, V, epsilon, train_indices

def run_fits_single(curvatures, num_trials, part_size):
    func = partial(fit_participant, curvatures = curvatures, num_fits = 1)
    pool = Pool()
    res = np.zeros(100, dtype = object)
    for i in range(100):        
	res[i] = np.reshape(np.array(pool.map(func, range(60))), (60, 5))
        print ('mean fits: ', np.mean(res[i][:, 2]))
    #return fit_Af, fit_Bf, fit_As, fit_Bs, fit_V
    return res   

def main():
    
    curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
    curvatures_smooth = curvatures_smooth/90
    print("parallel curvatures successful")
    print (curvatures_smooth)
    
    print ("Curvatures Loaded. In Fit routine")

    #%% Parallel run and dump fits
    fits = run_fits_single(curvatures_smooth, 640, 640)
    with open('fit_single_ll_transfer_test_rep.pickle', 'wb') as f:
        pickle.dump(fits, f)
    f.close()
        
    
    #%% Run this to save parameters
    
if __name__ == '__main__':
    main()
    
