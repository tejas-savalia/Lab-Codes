#%% Imports
import numpy as np
import matplotlib.pyplot as plt
import pickle
import ddm
#%% Read Times
its = pickle.load(open('its.pickle', 'rb'))
mts = pickle.load(open('mts.pickle', 'rb'))
# %%
plt.hist(np.ravel(its[3]))
# %%
m = Model()