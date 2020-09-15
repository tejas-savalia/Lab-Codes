#%%
import numpy as np
import matplotlib.pyplot as plt
import pickle

fits = pickle.load(open('fit_dual_bound_bootstrap.pickle', 'rb'))

#%%
params = {0:'Af', 1:'Bf', 2:'As', 3:'Bs', 4: 'Fits'}
for param in range(5):
    fig, axes = plt.subplots(2, 2)
    fig.suptitle(params.get(param))
    axes[0, 0].hist(fits[0::4, param], bins = 50)
    axes[0, 0].set_title('Sudden Speed')
    #axes[0, 0].set_xlim([0, 1])
    axes[0, 1].hist(fits[1::4, param], bins = 50)
    axes[0, 1].set_title('Sudden Accuracy')
    #axes[0, 1].set_xlim([0, 1])
    axes[1, 0].hist(fits[2::4, param], bins = 50)
    axes[1, 0].set_title('Gradual Speed')
    #axes[1, 0].set_xlim([0, 1])
    axes[1, 1].hist(fits[3::4, param], bins = 50)
    axes[1, 1].set_title('Gradual Accuracy')
    #axes[1, 1].set_xlim([0, 1])
    plt.tight_layout()
# %%
plt.hist(fits[2::4, 3])