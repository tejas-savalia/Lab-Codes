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
#%%
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

#%% Run this to compile dual state model functions


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


#%% Run this to compile fit routines
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
        rotation = 90/90.0
        for trial in trial_numbers:
            trial = int(trial)
            if trial < last_trial:
                #print (t[trial, 1])
                self.fast_est[trial+1] = Af*self.fast_est[trial] + Bf*errors_pred[trial]
                self.slow_est[trial+1] = As*self.slow_est[trial] + Bs*errors_pred[trial]
                self.rotation_est[trial+1] = self.fast_est[trial+1] + self.slow_est[trial+1]
                errors_pred[trial+1] = rotation - self.rotation_est[trial+1]
            else:
                errors_pred[trial] = rotation - self.rotation_est[last_trial]

        return errors_pred#, rotation_est, fast_est, slow_est

        
    def _loss(self, y_obs, y_pred):
        
        #for i in self.params_:
        #    if i < 0:
        #        return 10000000
        #    if i > 1:
        #        return 10000000
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
        print (self.params_)
        res = scipy.optimize.basinhopping(self._f, x0 = self.params_, minimizer_kwargs={'method': 'Powell', 'bounds':[(1e-15, 1), (1e-15, 1), (1e-15, 1), (1e-15, 1)]})
        #if res.success:
        self.params_ = res.x
        #print (res.x)
        print (res)
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