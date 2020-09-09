# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:57:00 2020

@author: Tejas
"""
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
from sklearn.base import BaseEstimator 
from sklearn.base import RegressorMixin
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import matplotlib.pyplot as plt
import math

#%% Helpers

def z_transform(array):
    return (array-np.mean(array))/np.std(array)
# %%Calculate Curvatures

def calc_angle(current_point, next_point, final_point):
    #vec1 = next_point - current_point
    vec1 = np.subtract(next_point, current_point)
#    vec2 = final_point - current_point
    vec2 = np.subtract(final_point, current_point)
    vec1 = vec1.astype('float64')
    vec2 = vec2.astype('float64')
    cos_theta = np.dot(vec1, vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))
    theta = np.degrees(np.arccos(cos_theta))
    return theta

def calc_curvature(data, block, trial, percentage_trajectory):
    traj = scipy.io.loadmat('data/data{data}/actual_trajectories/trajectories{block}.mat'.format(block=str(block), data=str(data)))
    trajx, trajy = traj['x'][0][trial][0], traj['y'][0][trial][0]
    #targetx, targety = trajx[-1], trajy[-1]
    partial_trajx, partial_trajy = get_partial_traj(data, block, trial, percentage_trajectory)
    #print (partial_trajx)
    #print (partial_trajy)
    angles = list([0])
    for i in range(len(partial_trajx[:-1])):
        #print (trajx[i], trajy[i])
        angles.append(calc_angle(np.array([partial_trajx[i], partial_trajy[i]]), np.array([partial_trajx[i+1], partial_trajy[i+1]]), np.array([trajx[-1], trajy[-1]])))
    return np.nanmedian(angles)
    #return calc_angle(np.array([partial_trajx[0], partial_trajy[0]]), np.array([partial_trajx[-1], partial_trajy[-1]]), np.array([trajx[-1], trajy[-1]]))

def calc_curvature_wrapper(params):
    return calc_curvature(params[0], params[1], params[2], params[3])

def get_traj(data, block, trial):
    traj = scipy.io.loadmat('data/data{data}/actual_trajectories/trajectories{block}.mat'.format(block=str(block), data=str(data)))
    x_traj = traj['x'][0][trial][0]
    y_traj = traj['y'][0][trial][0]
    return x_traj, y_traj

def get_partial_traj(data, block, trial, percentage_trajectory):
    traj = get_traj(data, block, trial)
    #dist_cutoff = percentage_trajectory*np.sqrt(traj[0][-1]**2 + traj[0][-1]**2, dtype = float)
    #for i in range(len(traj[0])):
        #dist_from_start = np.sqrt(traj[0][i]**2 + traj[1][i]**2, dtype = float)
        #if dist_from_start > dist_cutoff:
        #    break
    i = int(len(traj[0])/2)
    partial_trajx = traj[0][:i]
    partial_trajy = traj[1][:i]
        
            
    return partial_trajx, partial_trajy

#%% Run this to compile dual state model functions

def dual_model_sudden(num_trials, Af, Bf, As, Bs):
    errors = np.zeros((num_trials))
    rotation = 90
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    #rotation_est[0] = est
    for trial in range(num_trials - 1):
        errors[trial] = rotation - rotation_est[trial]
        #print(errors[trial])
        fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
        slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation - rotation_est[num_trials-1]
    return errors, rotation_est, fast_est, slow_est

def dual_model_gradual(num_trials, Af, Bf, As, Bs):
    errors = np.zeros((num_trials))
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    rotation = 0
    for trial in range(num_trials - 1):
        if trial%64 == 0:
            rotation = rotation + 10
        if rotation > 90:
            rotation = 90
        errors[trial] = rotation - rotation_est[trial]
        #print(errors[trial])
        fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
        slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation - rotation_est[num_trials-1]
    return errors, rotation_est, fast_est, slow_est

def residuals_sudden(params, num_trials, data_errors):
    model_errors = dual_model_sudden(num_trials, params[0], params[1], params[2], params[3])[0]
    residual_error = np.sum(np.square(model_errors - data_errors))
    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    return residual_error

def residuals_gradual(params, num_trials, data_errors):
    model_errors = dual_model_gradual(num_trials, params[0], params[1], params[2], params[3])[0]
    residual_error = np.sum(np.square(model_errors - data_errors))
    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    return residual_error

def dual_model_transfer(num_trials, Af, Bf, As, Bs, est):
    errors = np.zeros((num_trials))
    rotation = 0
    fast_est = np.zeros((num_trials))
    slow_est = np.zeros((num_trials))
    rotation_est = np.zeros((num_trials))
    rotation_est[0] = est
    for trial in range(num_trials - 1):
        errors[trial] = rotation_est[trial] - rotation
        #print(errors[trial])
        fast_est[trial+1] = Af*fast_est[trial] + Bf*errors[trial]
        slow_est[trial+1] = As*slow_est[trial] + Bs*errors[trial]
        rotation_est[trial+1] = fast_est[trial+1] + slow_est[trial+1]
        #print (rotation_est)
    errors[num_trials-1] = rotation_est[num_trials-1] - rotation
    return errors, rotation_est, fast_est, slow_est

def residuals_sudden_transfer(params, num_trials, data_errors, est):
    model_errors = dual_model_transfer(num_trials, params[0], params[1], params[2], params[3], est)[0]
    residual_error = np.sum(np.square(model_errors - data_errors))
    if params[0] > params[2]:
        residual_error = residual_error + 10000000
    if params[1] < params[3]:
        residual_error = residual_error + 10000000
    if params[0] < 0 or params[1] < 0 or params[2] < 0 or params[3] < 0:
        residual_error = residual_error + 10000000
    if params[0] > 1 or params[1] > 1 or params[2] > 1 or params[3] > 1:
        residual_error = residual_error + 10000000
    
    return residual_error

#%% Run this to compile fit routines
    
def fit_participant(participant, curvatures, num_fits):

    for fit_parts in range(num_fits):

        starting_points = np.array([[0.6, 0.5, 0.7, 0.1]])
        for initial_point in starting_points:
            if participant%4 == 0 or participant%4 == 1:      
                #fits = scipy.optimize.minimize(residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3]], args = (640, np.nan_to_num(np.ravel(curvatures[participant][1:-1]), nan = np.nanmedian(curvatures[participant][1:-1]))), method = 'Nelder-Mead')            
                fits = scipy.optimize.basinhopping(residuals_sudden, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3]], minimizer_kwargs={'args': (640, np.nan_to_num(np.ravel(curvatures[participant][1:-1]), nan = np.nanmedian(curvatures[participant][1:-1]))), 'method': 'Nelder-Mead'})

                #if fits.fun < fit_V[participant][fit_parts]:
                Af = fits.x[0]#fit_Af[participant][fit_parts] = fits.x[0]
                Bf = fits.x[1]#fit_Bf[participant][fit_parts] = fits.x[1]
                As = fits.x[2]#fit_As[participant][fit_parts] = fits.x[2]
                Bs = fits.x[3]#fit_Bs[participant][fit_parts] = fits.x[3]
                V = fits.fun#fit_V[participant][fit_parts] = fits.fun
                #fit_success[participant][fit_parts] = fits.success                
            else:
                #fits = scipy.optimize.minimize(residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3]], args = (640, np.nan_to_num(np.ravel(curvatures[participant][1:-1]), nan = np.nanmedian(curvatures[participant][1:-1]))), method = 'Nelder-Mead')         
                fits = scipy.optimize.basinhopping(residuals_gradual, x0 = [initial_point[0], initial_point[1], initial_point[2], initial_point[3]], minimizer_kwargs={'args': (640, np.nan_to_num(np.ravel(curvatures[participant][1:-1]), nan = np.nanmedian(curvatures[participant][1:-1]))), 'method': 'Nelder-Mead'})
                #if fits.fun < fit_V[participant][fit_parts]:
                Af = fits.x[0]#fit_Af[participant][fit_parts] = fits.x[0]
                Bf = fits.x[1]#fit_Bf[participant][fit_parts] = fits.x[1]
                As = fits.x[2]#fit_As[participant][fit_parts] = fits.x[2]
                Bs = fits.x[3]#fit_Bs[participant][fit_parts] = fits.x[3]
                V = fits.fun#fit_V[participant][fit_parts] = fits.fun
                #fit_success[participant][fit_parts] = fits.success
    return Af, Bf, As, Bs, V

def run_fits_dual(curvatures, num_trials, part_size):
    func = partial(fit_participant, curvatures = curvatures, num_fits = 1)
    pool = Pool()
    res = np.reshape(np.array(pool.map(func, range(60))), (60, 5))
    #return fit_Af, fit_Bf, fit_As, fit_Bs, fit_V
    return res   
#%%
class dual(BaseEstimator, RegressorMixin):
    def __init__(self, params = [ 0.8, 0.4, 0.9, 0.2]):
        super().__init__()
        self.params_ = params
#        self.Bf = Bf
#        self.As = As
#        self.Bs = Bs
        
    def _model_sudden(self, t, params):
        Af = params[0]
        Bf = params[1]
        As = params[2]
        Bs = params[3]
        #num_trials = len(t[:, 1])
        #print(num_trials)
        trial_numbers = t[:, 0]
        last_trial = int(max(trial_numbers))
        errors_pred = np.zeros(len(trial_numbers))
        rotation = 90
        for trial in trial_numbers:
            trial = int(trial)
            if trial < trial_numbers[-1]:
                #print (t[trial, 1])
                self.fast_est[trial+1] = Af*self.fast_est[trial] + Bf*t[trial, 1]
                self.slow_est[trial+1] = As*self.slow_est[trial] + Bs*t[trial, 1]
                self.rotation_est[trial+1] = self.fast_est[trial+1] + self.slow_est[trial+1]
                errors_pred[trial+1] = rotation - self.rotation_est[trial+1]
            else:
                errors_pred[trial] = rotation - self.rotation_est[last_trial]

        return errors_pred#, rotation_est, fast_est, slow_est

        
    def _loss(self, y_obs, y_pred):
        
        for i in self.params_:
            if i < 0:
                return 10000000
            if i > 1:
                return 10000000
        if self.params_[0] > self.params_[2]:
            return 1000000
        if self.params_[1] < self.params_[3]:
            return 1000000
        
        return np.sum((y_pred - y_obs)**2)
    
    #Function to be minimized
    def _f(self, params, *args):
        X_data = self._train_data
        y_obs = self._train_target
        num_train_data = len(X_data[:, 0])
        self.fast_est = np.zeros(num_train_data)
        self.slow_est = np.zeros(num_train_data)
        self.rotation_est = np.zeros(num_train_data)
        self.errors = np.zeros(num_train_data)
        y_pred = self._model_sudden(X_data, params)
        l = self._loss(y_pred, y_obs)
        return l
    
    def fit(self, X, Y):
        self._train_data = X
        self._train_target = Y
        #param_initial_values = [0.6, 0.5, 0.7, 0.1]
        res = scipy.optimize.basinhopping(self._f, x0 = self.params_, minimizer_kwargs={'method': 'Nelder-Mead'})
        #if res.success:
        self.params_ = res.x
        return self
    
    def predict(self, X):
        
        return self._model_sudden(X, self.params_)

#%%
curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
d = dual()
X = np.column_stack((np.arange(639), np.ravel(curvatures_smooth[16][1:-1])[:-1]))
Y = np.ravel(curvatures_smooth[16][1:-1])[1:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, shuffle = False)
d.fit(X, Y)


#%%
Y_pred = d.predict(X_train)

print(r2_score(Y_pred,Y_train))
#%%
def main():
    
    #%%Parallelize curvature calculations
        
#    paramlist = list(itertools.product(range(1000, 1060), range(12), range(64), range(1, 2)))
    #if __name__ == '__main__':
    curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
    
    print("parallel curvatures successful")
    print (curvatures_smooth)
    
    #with open('curvatures_smooth.pickle', 'wb') as f:
    #    pickle.dump(curvatures_smooth, f)
    #f.close()
    print ("Curvatures Loaded. In Fit routine")
    
    #%% Parallel run and dump fits
    fits = run_fits_dual(curvatures_smooth, 640, 640)
    with open('fit_dual_bound.pickle', 'wb') as f:
        pickle.dump(fits, f)
    f.close()
        
    
    #%% Run this to save parameters
    
if __name__ == '__main__':
    main()