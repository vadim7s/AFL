# combined prediction script
#game prediction with saved model

################################################
#
# requires h2o running !!!! run h2o.bat first
#
################################################


import sys
sys.path.insert(1,'J:\\AFL')
import afl_functions as afl

import pandas as pd
import h2o
import math

fixture = afl.get_fixtureAFL()
fixture.to_csv('J:\\AFL\\ToScore.csv',index=False) #check to make sure this file is for the round required

from h2o.automl import H2OAutoML
h2o.init()


model_path = 'J:\\AFL\\ModelGiving422018trainedON20112017\\StackedEnsemble_AllModels_0_AutoML_20181106_085551'
saved_model = h2o.load_model(model_path)

scoring_data = afl.get_data(season_from=2019,season_to=2019,proxy=False,train_mode=False)

hf_score = h2o.H2OFrame(scoring_data)
prediction=saved_model.predict(hf_score)

prediction = prediction.as_data_frame(use_pandas=True)
prediction.to_csv('J:\\AFL\\PredictionRun.csv')
scoring_data.to_csv('J:\\AFL\\temp.csv')