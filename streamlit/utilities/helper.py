import pickle
from tensorflow.keras.models import load_model

min_max = pickle.load(open('serialization/utilities/min_and_max.pickle', 'rb')) # NOTE: you can debug the min_max using st.json(min_max)
regression_metrics = pickle.load(open('serialization/dataframes/regression_metrics.pickle', 'rb'))

scaler_DC = pickle.load(open('serialization/utilities/scaler_DC.pickle', 'rb'))
scaler_DMC = pickle.load(open('serialization/utilities/scaler_DMC.pickle', 'rb'))
scaler_FFMC = pickle.load(open('serialization/utilities/scaler_FFMC.pickle', 'rb'))
scaler_ISI = pickle.load(open('serialization/utilities/scaler_ISI.pickle', 'rb'))
scaler_temp = pickle.load(open('serialization/utilities/scaler_temp.pickle', 'rb'))
scaler_RH = pickle.load(open('serialization/utilities/scaler_RH.pickle', 'rb'))
scaler_wind = pickle.load(open('serialization/utilities/scaler_wind.pickle', 'rb'))
scaler_rain = pickle.load(open('serialization/utilities/scaler_rain.pickle', 'rb'))
scaler_area = pickle.load(open('serialization/utilities/scaler_area.pickle', 'rb'))

adam_model = load_model('serialization/models/regression_models/adam_model.h5')
adagrad_model = load_model('serialization/models/regression_models/adagrad_model.h5')
adadelta_model = load_model('serialization/models/regression_models/adadelta_model.h5')