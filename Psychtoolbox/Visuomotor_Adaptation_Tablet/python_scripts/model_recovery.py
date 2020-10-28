#%% imports
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
from dual_model_with_transfer import dual_model_sudden, dual_model_gradual
from single_model_with_transfer import model_sudden, model_gradual

#%% Import fit parameters
fits_single = pickle.load(open('fit_single_bound_with_transfer.pickle', 'rb'))
fits_dual = pickle.load(open('fit_dual_bound_with_transfer.pickle', 'rb'))

# %% Generate data using fit parameters. Starting with dual state
#Declare storage variables
generated_errors_dual = np.zeros((60, 768))
for participant in range(60):
    if participant%4 == 0 or participant%4 == 1:
        generated_errors_dual[participant][64:] = dual_model_sudden(704, fits_dual[participant][0], fits_dual[participant][1], fits_dual[participant][2], fits_dual[participant][3])[0]
    else:
        generated_errors_dual[participant][64:] = dual_model_gradual(704, fits_dual[participant][0], fits_dual[participant][1], fits_dual[participant][2], fits_dual[participant][3])[0]

generated_errors_single = np.zeros((60, 768))
for participant in range(60):
    if participant%4 == 0 or participant%4 == 1:
        generated_errors_single[participant][64:] = model_sudden(704, fits_single[participant][0], fits_single[participant][1])[0]
    else:
        generated_errors_single[participant][64:] = model_gradual(704, fits_single[participant][0], fits_single[participant][1])[0]

# %% Save these data
with open('dual_with_transfer_generated_errors.pickle', 'wb') as f:
    pickle.dump(np.reshape(generated_errors_dual, (60, 12, 64)), f)
f.close()
with open('single_with_transfer_generated_errors.pickle', 'wb') as f:
    pickle.dump(np.reshape(generated_errors_single, (60, 12, 64)), f)
f.close()
