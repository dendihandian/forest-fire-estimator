import streamlit as st
import numpy as np
import pandas as pd
from utilities.helper import min_max
from utilities.helper import scaler_DC, scaler_FFMC, scaler_rain, scaler_ISI, scaler_DMC, scaler_RH, scaler_temp, scaler_wind, scaler_area
from utilities.helper import adam_model, adagrad_model, adadelta_model

model_names = (
    'Adam',
    'Adadelta',
    'Adagrad',
)

def predict(parameters, modelname):

    DC = parameters['DC']
    DMC = parameters['DMC']
    FFMC = parameters['FFMC']
    ISI = parameters['ISI']
    temp = parameters['temp']
    RH = parameters['RH']
    wind = parameters['wind']
    rain = parameters['rain']

    inputs = pd.DataFrame({
        'DC' : [scaler_DC.transform(np.array([DC]).reshape(1, -1))[0][0]],
        'DMC' : [scaler_DMC.transform(np.array([DMC]).reshape(1, -1))[0][0]],
        'FFMC' : [scaler_FFMC.transform(np.array([FFMC]).reshape(1, -1))[0][0]],
        'ISI' : [scaler_ISI.transform(np.array([ISI]).reshape(1, -1))[0][0]],
        'temp' : [scaler_temp.transform(np.array([temp]).reshape(1, -1))[0][0]],
        'RH' : [scaler_RH.transform(np.array([RH]).reshape(1, -1))[0][0]],
        'wind' : [scaler_wind.transform(np.array([wind]).reshape(1, -1))[0][0]],
        'rain' : [scaler_rain.transform(np.array([rain]).reshape(1, -1))[0][0]],
    })

    output = None
    views = 0

    if (modelname == model_names[0]):

        output = adam_model.predict(inputs)
        output = output[0]

    elif (modelname == model_names[1]):

        output = adadelta_model.predict(inputs)
        output = output[0]

    elif (modelname == model_names[2]):

        output = adagrad_model.predict(inputs)
        output = output[0]

    # NOTE: some output from the model may have different shape. debug it with st.write(output.shape)

    if (output):

        views = scaler_area.inverse_transform(np.array([output]).reshape(1, -1))[0][0]

    return views

def regression_page():
    with st.container():

        st.header('Burn Area Estimator')

        with st.container():

            col1, col2 = st.columns(2)

            with col1:
                DC = st.number_input('DC', min_value=min_max['DC'][0], max_value=min_max['DC'][1], value=min_max['DC'][0])
                DMC = st.number_input('DMC', min_value=min_max['DMC'][0], max_value=min_max['DMC'][1], value=min_max['DMC'][0])
                FFMC = st.number_input('FFMC', min_value=min_max['FFMC'][0], max_value=min_max['FFMC'][1], value=min_max['FFMC'][0])
                ISI = st.number_input('ISI', min_value=min_max['ISI'][0], max_value=min_max['ISI'][1], value=min_max['ISI'][0])

            with col2:
                temp = st.number_input('temp', min_value=min_max['temp'][0], max_value=min_max['temp'][1], value=min_max['temp'][0])
                RH = st.number_input('RH', min_value=min_max['RH'][0], max_value=min_max['RH'][1], value=min_max['RH'][0])
                wind = st.number_input('wind', min_value=min_max['wind'][0], max_value=min_max['wind'][1], value=min_max['wind'][0])
                rain = st.number_input('rain', min_value=min_max['rain'][0], max_value=min_max['rain'][1], value=min_max['rain'][0])

            modelname = st.selectbox('Model', model_names)
            area = None

            if st.button('Predict'):
                area = predict({
                    'DC': DC,
                    'DMC': DMC,
                    'FFMC': FFMC,
                    'ISI': ISI,
                    'temp': temp,
                    'RH': RH,
                    'wind': wind,
                    'rain': rain,
                }, modelname)

            if area != None:
                st.metric('Area', round(area), delta=None, delta_color="normal")

    # st.write("""__________""")

    # with st.container():
    #     st.header('Model Evaluation')
    #     st.dataframe(regression_metrics)