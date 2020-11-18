#%%
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
from all_models import *
import sys

# %%
def main(num_fit_trials):
    curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
    curvatures_smooth = curvatures_smooth/90
    print("parallel curvatures successful")
    print (curvatures_smooth)

    print ("Curvatures Loaded. In Fit routine")
    print (num_fit_trials)

    #%% Parallel run and dump fits
    fits = run_fits_single(curvatures_smooth, int(num_fit_trials[1]))
    with open('fit_single_640.pickle', 'wb') as f:
        pickle.dump(fits, f)
    f.close()
    fits = run_fits_dual(curvatures_smooth, int(num_fit_trials[1]))
    with open('fit_dual_CV_640.pickle', 'wb') as f:
        pickle.dump(fits, f)
    f.close()

if __name__ == '__main__':
    main(sys.argv)