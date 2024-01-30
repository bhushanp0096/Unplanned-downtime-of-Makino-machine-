# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:02:26 2023

@author: Berger
"""
import streamlit as st
import pickle
import numpy as np

# Load the trained Random Forest model
model = pickle.load(open('randomforest.pkl', 'rb'))


# Define the machine IDs and assembly line numbers dictionaries
machine_ids = {'Makino-L3-Unit1-2015': 0, 'Makino-L2-Unit1-2015': 1, 'Makino-L1-Unit1-2013': 2}
assembly_line_nos = {'Shopfloor-L3': 0, 'Shopfloor-L2': 1, 'Shopfloor-L1': 2}

# Define the main function
def main():
    st.title(("Makino Machine Downtime Prediction"))

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Machino Machine Downtime ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    # Create the input fields for user input
    Hydraulic_Pressure = st.number_input('Hydraulic Pressure')
    Coolant_Pressure = st.number_input('Coolant Pressure')
    Air_System_Pressure = st.number_input('Air System Pressure')
    Coolant_Temperature = st.number_input('Coolant Temperature')
    Hydraulic_Oil_Temperature = st.number_input('Hydraulic Oil Temperature')
    Spindle_Bearing_Temperature = st.number_input('Spindle Bearing Temperature')
    Spindle_Vibration = st.number_input('Spindle Vibration')
    Tool_Vibration = st.number_input('Tool Vibration')
    Spindle_Speed = st.number_input('Spindle Speed')
    Voltage = st.number_input('Voltage')
    Torque = st.number_input('Torque')
    Cutting = st.number_input('Cutting')
    Machine_ID = st.selectbox('Machine ID', list(machine_ids.keys()))
    Assembly_Line_No = st.selectbox('Assembly Line No', list(assembly_line_nos.keys()))

    if st.button('Predict'):
        machine_id = machine_ids[Machine_ID]
        assembly_line_no = assembly_line_nos[Assembly_Line_No]
        input_data = np.array([[Hydraulic_Pressure, Coolant_Pressure, Air_System_Pressure, Coolant_Temperature, Hydraulic_Oil_Temperature, Spindle_Bearing_Temperature, Spindle_Vibration, Tool_Vibration, Spindle_Speed, Voltage, Torque, Cutting,machine_id, assembly_line_no]])
    
        prediction = model.predict(input_data)

        # Display the predicted value   
        if prediction[0] == 0:
            st.write('Machine Failure')
        else:
            st.write('No Machine Failure')

# Call the main function
if __name__ == '__main__':
    main()