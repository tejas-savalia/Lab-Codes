import pandas as pd
import pickle
def read_pickle_file(file):
    pickle_data = pd.read_pickle(file)
    return pickle_data

curvatures_smooth = pd.read_pickle("curvatures_smooth.pickle")
curvatures_smooth
