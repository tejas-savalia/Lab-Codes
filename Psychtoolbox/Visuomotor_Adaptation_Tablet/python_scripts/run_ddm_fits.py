import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ddm import Model, Sample
from ddm import Model
from ddm.models import DriftConstant, NoiseConstant, BoundConstant, OverlayNonDecision, ICRange
from ddm.functions import fit_adjust_model, display_model
from ddm import Fittable
from ddm.models import LossRobustBIC, LossRobustLikelihood, LossSquaredError
from ddm.functions import fit_adjust_model, fit_model
import seaborn as sns
import pickle
import scipy.io
from multiprocessing import Pool

def fit_ddm_participant(participant):
    df_errors = pd.read_csv('Curvature_Errors.csv')
    incorrect_thresold = np.array([9/90, 15/90, 20/90, 30/90, 45/90])
    model_fits_4param = np.zeros((12, len(incorrect_thresold)), dtype = object)
    for block in range(12):
        print("Participant: ", participant)
        print("Block: ", block)
        for ic in range(len(incorrect_thresold)):
            df_rt = pd.read_csv('RTs.csv')            
            df_rt['Correct'] = df_errors['Errors'] < incorrect_thresold[ic]            
            df_rt = df_rt[df_rt['Participant_Id'] == participant]
            df_rt = df_rt[df_rt["ITs"] > .001]
            df_rt = df_rt[df_rt["ITs"] < 5]
            df_rt = df_rt.drop(['Trial', 'Unnamed: 0', 'Participant_Id', 'Rotation', 'Emphasis', 'MTs'], axis = 1)

            samp = Sample.from_pandas_dataframe(df_rt[df_rt['Block'] == block], rt_column_name="ITs", correct_column_name="Correct")
            model_fit = Model(name='Simple model (fitted)',
                          drift=DriftConstant(drift=Fittable(minval=-20, maxval=20)),
                          noise=NoiseConstant(noise=Fittable(minval = 0, maxval = 5)),                      
                          bound=BoundConstant(B=Fittable(minval = 0, maxval = 20)),
                          overlay=OverlayNonDecision(nondectime=Fittable(minval = 0, maxval = 1)),
                          dx=.001, dt=.01, T_dur=5)

            try:
                fit_adjust_model(samp, model_fit,
                             fitting_method="differential_evolution",
                             lossfunction=LossRobustLikelihood, verbose=False)
            except:
                print ("In except: ")
                print (participant, block)
            model_fits_4param[block][ic] = model_fit
    return model_fits_4param

def main():
    pool = Pool()
    res = np.zeros(60, dtype = object)
    res = pool.map(fit_ddm_participant, range(60))
    pickle.dump(res, open('ddm_fits.pickle', 'wb'))

if __name__ == '__main__':
    main()
