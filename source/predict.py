

import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline



model=pickle.load(open('final_model.sav','rb'))



## input array must be in this order:    dvoa, anya, age, def_avg_qb_hit
def predict(df):
    predictions=model.predict(df)
    return predictions
