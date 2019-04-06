"""
Script to make petrophysical analysis over a well log dataset

input: path to CSV file (data), path to JSON file (formations)
output: Petrophysical measurements

JSON example:
[
    {
        "name": "formation_1",
        "high_depth": 0,
        "low_depth": 866.5,
        "fluid_density": 12.4,
        ...
    },

    {
        "name": "formation_2",
        "high_depth": 866.5,
        "low_depth": 1366.5,
        "fluid_density": 10.3,
        ...
    }
]

Author: Sebastian Arango

"""

import pandas as pd
import numpy as np
import json



PATH_TO_CSV = '../data/interim/extracted-1.csv'
MANDATORY_COLUMNS = ['#Depth (#M)', 'GR (API)', 'RT (ohm.m)', 'NPHI (v/v)', 'RHOB (g/cm3)']
REGION_LIMITS = [0, 866.5, 1366.5, 2217, 2785, 3655, 4770.2]
FORMATIONS = [] #List of dictionaries, each being a formation.


data = pd.read_csv(PATH_TO_CSV)

def check_data_columns(data):

    return False if data[MANDATORY_COLUMNS].isnull().any() else True

def region_asignation(FORMATIONS):

    """return {
        'A': data.loc[data['#Depth (#M)'] < 866.5],
        'B': 866.5 <= data.loc[data['#Depth (#M)'] < 1366.5],
        'C': 1366.5 <= data.loc[data['#Depth (#M)'] < 2217],
        'D': 2217 <= data.loc[data['#Depth (#M)'] < 2785],
        'E': 2785 <= data.loc[data['#Depth (#M)'] < 3655,
        'F': 3655 <= data.loc[data['#Depth (#M)'] < 4770.2],
        'G': data.loc[data['#Depth (#M)'] >= 4770.2]"""
        }

    """return {str(i): {
        'data': REGION_LIMITS[i] <= data.loc[data['#Depth (#M)'] < REGION_LIMITS[i+1], 
        'fd': FLUID_DENSITY[i]},
        '' for i in len(REGION_LIMITS)-1}"""

    for formation in FORMATIONS:

        formation['data'] = formation.get('high_depth') <= data.loc[data['#Depth (#M)'] < formation.get('low_depth')
    
    return FORMATIONS

def 



"""

3. Definir parametros iniciales		
Densidad fluido		0.9
DT Fluido		
a		1
m		2.45
n		2.45

"""



