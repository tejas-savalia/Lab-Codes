#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from multiprocessing import Pool
from functools import partial
import pickle
import scipy
import scipy.optimize
from sklearn.metrics import *
import scipy.stats as stat
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d


# # Dual Models

# ## With Transfer (4 Params)

# In[2]:


def dual_model_sudden(num_trials, Af, Bf, As, Bs):
    errors = np.zeros((num_trials))
    rotation = 1.0
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    #rotation_est[0] = est
    for trial in range(num_trials - 1):
        if trial < 640:
            rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial]
        #print(errors[trial])
            fast_est[trial+1] = Af*fast_est[trial] - Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] - Bs*errors[trial]

        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1]
    return errors, rotation_est, fast_est, slow_est

def dual_model_gradual(num_trials, Af, Bf, As, Bs):
    errors = np.zeros((num_trials))
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    rotation = 0
    for trial in range(num_trials - 1):
        if trial < 640:
            if trial%64 == 0:
                rotation = rotation + 10/90.0
            if rotation > 1.0:
                rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial] 
            fast_est[trial+1] = Af*fast_est[trial] - Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] - Bs*errors[trial]

        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1]

    return errors, rotation_est, fast_est, slow_est
#%%
def dual_six_param_sudden(num_trials, Af, Bf, Aft, Bft, As, Bs):
    errors = np.zeros((num_trials))
    rotation = 1.0
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    #rotation_est[0] = est
    for trial in range(num_trials - 1):
        if trial < 640:
            rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial]
        #print(errors[trial])
            fast_est[trial+1] = Aft*fast_est[trial] - Bft*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] - Bs*errors[trial]

        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1]
    return errors, rotation_est, fast_est, slow_est

def dual_six_param_gradual(num_trials, Af, Bf, Aft, Bft, As, Bs):
    errors = np.zeros((num_trials))
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    rotation = 0
    for trial in range(num_trials - 1):
        if trial < 640:
            if trial%64 == 0:
                rotation = rotation + 10/90.0
            if rotation > 1.0:
                rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial] 
            fast_est[trial+1] = Aft*fast_est[trial] - Bft*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] - Bs*errors[trial]

        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1]

    return errors, rotation_est, fast_est, slow_est


# 

# In[ ]:





# # 2 Param Single state model with Transfer Phase

# In[3]:


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
#%%
def mixed_gradual(num_trials, Af, Bf, As, Bs):
    errors = np.zeros((num_trials))
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    rotation = 0
    for trial in range(num_trials - 1):
        if trial < 640:
            if trial%64 == 0:
                rotation = rotation + 10/90.0
            if rotation > 1.0:
                rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            #fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial] 
            fast_est[trial+1] = Af*fast_est[trial] - Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] - Bs*errors[trial]

        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1]

    return errors, rotation_est, fast_est, slow_est

def mixed_sudden(num_trials, Af, Bf, As, Bs):
    errors = np.zeros((num_trials))
    rotation = 1.0
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    #rotation_est[0] = est
    for trial in range(num_trials - 1):
        if trial < 640:
            rotation = 1.0
            errors[trial] = rotation - rotation_est[trial]
            #fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        else:
            rotation = 0
            errors[trial] = rotation_est[trial]
        #print(errors[trial])
            fast_est[trial+1] = Af*fast_est[trial] - Bf*errors[trial]
            slow_est[trial+1] = As*slow_est[trial] - Bs*errors[trial]

        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1]
    return errors, rotation_est, fast_est, slow_est

# # Residual Functions

# ## Single State Models

# In[4]:


def single_residuals_sudden(params, num_trials, data_errors, train_indices):
    #print(train_indices)
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

def single_residuals_gradual(params, num_trials, data_errors, train_indices):
    
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


# ## Dual State Models

# In[5]:


def dual_residuals_sudden(params, num_trials, data_errors, train_indices):
    model_errors = dual_model_sudden(num_trials, params[0], params[1], params[2], params[3])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[4]))
    #residual_error = np.sum(np.square(model_errors_train - data_errors_train))
    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1:
        residual_error = residual_error + 10000000

    return residual_error

def dual_residuals_gradual(params, num_trials, data_errors, train_indices):
    model_errors = dual_model_gradual(num_trials, params[0], params[1], params[2], params[3])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    #residual_error = np.sum(np.square(model_errors_train - data_errors_train))
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[4]))
    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1:
        residual_error = residual_error + 10000000

    return residual_error

#%%

def mixed_residuals_sudden(params, num_trials, data_errors, train_indices):
    model_errors = mixed_sudden(num_trials, params[0], params[1], params[2], params[3])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[4]))

    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1:
        residual_error = residual_error + 10000000

    return residual_error

def mixed_residuals_gradual(params, num_trials, data_errors, train_indices):
    model_errors = mixed_gradual(num_trials, params[0], params[1], params[2], params[3])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[4]))
    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1:
        residual_error = residual_error + 10000000

        
    return residual_error
#%%
def dual_six_params_residuals_sudden(params, num_trials, data_errors, train_indices):
    model_errors = dual_six_param_sudden(num_trials, params[0], params[1], params[2], params[3], params[4], params[5])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[6]))
    #residual_error = np.sum(np.square(model_errors_train - data_errors_train))
    if params[0] > params[4] or params[2] > params[4]:
        residual_error = residual_error + 10000000
    if params[1] < params[3] or params[3] < params[5]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0 or params[4] < 0 or params[5] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1 or params[4] > 1 or params[5] > 1:
        residual_error = residual_error + 10000000

    return residual_error

def dual_six_params_residuals_gradual(params, num_trials, data_errors, train_indices):
    model_errors = dual_six_param_gradual(num_trials, params[0], params[1], params[2], params[3], params[4], params[5])[0]
    model_errors_train = np.take(model_errors, train_indices)
    data_errors_train = np.take(data_errors, train_indices)
    #residual_error = np.sum(np.square(model_errors_train - data_errors_train))
    residual_error = -2*sum(stat.norm.logpdf(data_errors_train, model_errors_train, params[6]))
    if params[0] > params[4] or params[2] > params[4]:
        residual_error = residual_error + 10000000
    if params[1] < params[3] or params[3] < params[5]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0 or params[4] < 0 or params[5] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1 or params[4] > 1 or params[5] > 1:
        residual_error = residual_error + 10000000

    return residual_error

# ## Fit functions

# In[6]:


def dual_test_fit(participant, curvatures, num_fit_trials, train_indices):
    train_length = num_fit_trials - int(np.floor(num_fit_trials/10.0))
    
    #train_indices = np.random.choice(num_fit_trials, train_length, replace = False)
    starting_points = np.array([[0.9, 0.3, 0.99, 0.01, 0.05]])
    for initial_point in starting_points:
        if participant%4 == 0 or participant%4 == 1:      
            fits = scipy.optimize.basinhopping(dual_residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3], initial_point[4]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})

            Af = fits.x[0]
            Bf = fits.x[1]
            As = fits.x[2]
            Bs = fits.x[3]
            epsilon = fits.x[4]
            V = fits.fun
        else:
            fits = scipy.optimize.basinhopping(dual_residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3], initial_point[4]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})
            Af = fits.x[0]
            Bf = fits.x[1]
            As = fits.x[2]
            Bs = fits.x[3]
            epsilon = fits.x[4]
            V = fits.fun
            
        print (participant, V)
    return Af, Bf, As, Bs, V, epsilon, train_indices


# In[7]:


def single_test_fit(participant, curvatures, num_fit_trials, train_indices):
    train_length = num_fit_trials - int(np.floor(num_fit_trials/10.0))
    #train_indices = np.random.choice(num_fit_trials, train_length, replace = False)
    starting_points = np.array([[0.9, 0.2, 0.5]])
    for initial_point in starting_points:
        if participant%4 == 0 or participant%4 == 1:      
            fits = scipy.optimize.basinhopping(single_residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})

            A = fits.x[0]
            B = fits.x[1]
            epsilon = fits.x[2]
            V = fits.fun
        else:
            fits = scipy.optimize.basinhopping(single_residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})
            
            A = fits.x[0]
            B = fits.x[1]
            epsilon = fits.x[2]
            V = fits.fun
        print (participant, V)
    return A, B, V, epsilon, train_indices

#%%
def dual_six_params_test_fit(participant, curvatures, num_fit_trials, train_indices, starting_points):
    #train_length = num_fit_trials - int(np.floor(num_fit_trials/10.0))
    #train_indices = np.random.choice(num_fit_trials, train_length, replace = False)
    #starting_points = np.array([[0.9, 0.3, 0.9, 0.3, 0.99, 0.01, 0.05]])
    #print("here", starting_points)
    bounds = [(0, 1), (0, 1),(0, 1),(0, 1),(0, 1),(0, 1),(0, 1)]
    #for initial_point in starting_points:
    if participant%4 == 0 or participant%4 == 1:      
        fits = scipy.optimize.basinhopping(dual_six_params_residuals_sudden, x0 = [starting_points[0], starting_points[1], starting_points[2], starting_points[3], starting_points[4], starting_points[5], starting_points[6]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})

        Af = fits.x[0]
        Bf = fits.x[1]
        Aft = fits.x[2]
        Bft = fits.x[3]
        As = fits.x[4]
        Bs = fits.x[5]
        epsilon = fits.x[6]
        V = fits.fun
    else:
        fits = scipy.optimize.basinhopping(dual_six_params_residuals_gradual, x0 = [starting_points[0], starting_points[1], starting_points[2], starting_points[3], starting_points[4], starting_points[5], starting_points[6]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})
        Af = fits.x[0]
        Bf = fits.x[1]
        Aft = fits.x[2]
        Bft = fits.x[3]
        As = fits.x[4]
        Bs = fits.x[5]
        epsilon = fits.x[6]
        V = fits.fun
        
    print (participant, V)
    return Af, Bf, Aft, Bft, As, Bs, V, epsilon, train_indices


# In[7]:


def mixed_test_fit(participant, curvatures, num_fit_trials, train_indices):
    train_length = num_fit_trials - int(np.floor(num_fit_trials/10.0))
    
    #train_indices = np.random.choice(num_fit_trials, train_length, replace = False)
    starting_points = np.array([[0.9, 0.3, 0.99, 0.01, 0.05]])
    bounds = [(0, 1), (0, 1), (0, 1), (0, 1),(0, 1)]
    for initial_point in starting_points:
        if participant%4 == 0 or participant%4 == 1:      
            fits = scipy.optimize.basinhopping(mixed_residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3], initial_point[4]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})

            Af = fits.x[0]
            Bf = fits.x[1]
            As = fits.x[2]
            Bs = fits.x[3]
            epsilon = fits.x[4]
            V = fits.fun
        else:
            fits = scipy.optimize.basinhopping(mixed_residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3], initial_point[4]], minimizer_kwargs={'args': (num_fit_trials, np.nan_to_num(np.ravel(curvatures[participant][1:]), nan = np.nanmedian(curvatures[participant][1:])), train_indices), 'method':'Nelder-Mead'})
            Af = fits.x[0]
            Bf = fits.x[1]
            As = fits.x[2]
            Bs = fits.x[3]
            epsilon = fits.x[4]
            V = fits.fun
            
        print (participant, V)
    return Af, Bf, As, Bs, V, epsilon, train_indices

# # Running Fit routines

# In[8]:


def run_fits_dual(curvatures, num_fit_trials, num_fits):
    train_indices = pickle.load(open('train_indices_704.pickle', 'rb'))
    pool = Pool()
    res = np.zeros(num_fits, dtype = object)
    for i in range(num_fits):
        c_obj = np.zeros(60, dtype = object)
        for participant in range(60):
            c_obj[participant] = curvatures
        participant_args = [x for x in zip(range(60), c_obj[range(60)],  np.repeat(num_fit_trials, 60), train_indices[i])]
        res[i] = np.reshape(np.array(pool.starmap(dual_test_fit, participant_args)), (60, 7))
        print ("Mean Res in dual: ", i, np.mean(res[i][:, -3]))

    return res   

def run_fits_single(curvatures, num_fit_trials, num_fits):
    train_indices = pickle.load(open('train_indices_704.pickle', 'rb'))
    print(train_indices[0].shape)
    pool = Pool()
    res = np.zeros(num_fits, dtype = object)
    for i in range(num_fits):
        c_obj = np.zeros(60, dtype = object)
        for participant in range(60):
            c_obj[participant] = curvatures
        participant_args = [x for x in zip(range(60), c_obj[range(60)],  np.repeat(num_fit_trials, 60), train_indices[i])]
        res[i] = np.reshape(np.array(pool.starmap(single_test_fit, participant_args)), (60, 5))
        print ("Mean Res in dual: ", i, np.mean(res[i][:, -3]))
    return res   


# In[ ]:
def run_fits_mixed(curvatures, num_fit_trials, num_fits):
    #func = partial(single_test_fit, curvatures = curvatures, num_fits = 1, num_fit_trials = num_fit_trials)
    train_indices = pickle.load(open('train_indices_704.pickle', 'rb'))
    pool = Pool()
    res = np.zeros(num_fits, dtype = object)
    for i in range(num_fits):
        c_obj = np.zeros(60, dtype = object)
        for participant in range(60):
            c_obj[participant] = curvatures
        participant_args = [x for x in zip(range(60), c_obj[range(60)],  np.repeat(num_fit_trials, 60), train_indices[i])]
        res[i] = np.reshape(np.array(pool.starmap(mixed_test_fit, participant_args)), (60, 7))
        print ("Mean Res in dual: ", i, np.mean(res[i][:, -3]))

    return res   
def run_fits_dual_six_params(curvatures, num_fit_trials, num_fits):
    train_indices = pickle.load(open('train_indices_704.pickle', 'rb'))
    #train_indices = pickle.load(open('ti.pickle', 'rb'))
    starting_points  = pickle.load(open('sp.pickle', 'rb'))
    pool = Pool()
    res = np.zeros(num_fits, dtype = object)
    for i in range(num_fits):
        c_obj = np.zeros(60, dtype = object)
        for participant in range(60):
            c_obj[participant] = curvatures
        participant_args = [x for x in zip(range(60), c_obj[range(60)],  np.repeat(num_fit_trials, 60), train_indices[i], starting_points[i])]
        res[i] = np.reshape(np.array(pool.starmap(dual_six_params_test_fit, participant_args)), (60, 9))
        print ("Mean Res in dual: ", i, np.mean(res[i][:, -3]))

    return res   



