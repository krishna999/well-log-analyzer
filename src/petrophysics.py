"""
Script to make petrophysical analysis over a well log dataset

input: CSV file
output: Petrophysical measurements

Author: Sebastian Arango

"""

import pandas as pd
import numpy as np 



PATH_TO_CSV = '../data/interim/extracted-1.csv'
MANDATORY_COLUMNS = ['#Depth (#M)', 'GR (API)', 'RT (ohm.m)', 'NPHI (v/v)', 'RHOB (g/cm3)']
REGION_LIMITS = [0, 866.5, 1366.5, 2217, 2785, 3655, 4770.2]


data = pd.read_csv(PATH_TO_CSV)

def check_data_columns(data):

    return False if data[MANDATORY_COLUMNS].isnull().any() else True

def region_asignation(data):

    """return {
        'A': data.loc[data['#Depth (#M)'] < 866.5],
        'B': 866.5 <= data.loc[data['#Depth (#M)'] < 1366.5],
        'C': 1366.5 <= data.loc[data['#Depth (#M)'] < 2217],
        'D': 2217 <= data.loc[data['#Depth (#M)'] < 2785],
        'E': 2785 <= data.loc[data['#Depth (#M)'] < 3655,
        'F': 3655 <= data.loc[data['#Depth (#M)'] < 4770.2],
        'G': data.loc[data['#Depth (#M)'] >= 4770.2]"""
        }

    return {str(i): {
        'data': REGION_LIMITS[i] <= data.loc[data['#Depth (#M)'] < REGION_LIMITS[i+1], 'fd': } for i in len(REGION_LIMITS)-1}

def 



"""

3. Definir parametros iniciales		
Densidad fluido		0.9
DT Fluido		
a		1
m		2.45
n		2.45

"""



