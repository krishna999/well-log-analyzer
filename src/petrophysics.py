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
        "fluid_dt": 8.93,
        "a": 7.45,
        "m": 3.2,
        "n": 2.83
    },

    {
        "name": "formation_2",
        "high_depth": 866.5,
        "low_depth": 1366.5,
        "fluid_density": 10.3,
        "a": 7.45,
        "m": 3.2,
        "n": 2.83
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

formations = [] #List of dictionaries, each being a formation.


data = pd.read_csv(PATH_TO_CSV)

def check_data_columns(data):

    return False if data[MANDATORY_COLUMNS].isnull().any() else True


def region_asignation(formations):

    for i, formation in enumerate(formations):

        formations[i]['data'] = formation.get('high_depth') <= data.loc[data['#Depth (#M)'] < formation.get('low_depth')

    return formations


def calculate_clay_value(data):

    clay_values = []

    if not data['GR (API)'].isnull().any():

        lower, upper = np.percentile(data['GR (API)'], [2, 98])

        clay_values.append((data['GR (API)'].values - lower) / (upper - lower))

    if not data['NPHI (v/v)'].isnull().any():

        neutron_sh = data.loc[data['GR (API)']==upper]

        clay_values.append((data['NPHI (v/v)'].values) / neutron_sh





"""

3. Definir parametros iniciales		
Densidad fluido		0.9
DT Fluido		
a		1
m		2.45
n		2.45

"""



