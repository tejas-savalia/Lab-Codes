#%%
from psychopy.misc import fromFile
import numpy as np
import matplotlib.pyplot as plt
#%%
datFile = fromFile('data/0_vm_20xx_2020_Sep_23_1343.psydat')
# %%
trialHandler = datFile.loops[5]
trialHandlerParams = dir(datFile.loops[3])
# %%
for j in range(2):
    for i in range(4):
        plt.plot(trialHandler.data['rotated_mouse.x'][j][i], trialHandler.data['rotated_mouse.y'][j][i])
# %%
