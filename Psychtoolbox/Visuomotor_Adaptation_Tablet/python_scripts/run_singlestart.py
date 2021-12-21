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
from fits_single_param_start import *
#from transfer_models import *
import sys

# %%
def main(num_fit_trials):
    curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
    curvatures_smooth = curvatures_smooth/90.0
    #curvatures_smooth = pickle.load(open('mean_drawn_grouperrors.pickle', 'rb'))
    
    fits = run_fits_singlestart(curvatures_smooth, int(num_fit_trials[1]))
    with open('fit_single_start_640.pickle', 'wb') as f:
        pickle.dump(fits, f)
    f.close()
    #fits = run_fits_single(curvatures_smooth, int(num_fit_trials[1]), int(num_fit_trials[2]), int(num_fit_trials[3]))
    #with open('fit_single_meaned_CV_640.pickle', 'wb') as f:
    #    pickle.dump(fits, f)
    #f.close()



if __name__ == '__main__':
    main(sys.argv)
