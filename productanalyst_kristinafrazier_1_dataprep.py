# Load and Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

prequals = pd.read_csv('prequals.csv')
intellicron_prequals = pd.read_csv('intellicron_prequals.csv')

def data_prep():
    # Convert date columns to date time
    prequals['prequal_date'] = pd.to_datetime(prequals['prequal_date'])
    intellicron_prequals['assignment_date'] = pd.to_datetime(intellicron_prequals['assignment_date'])

    # Assign a new column to identify intellicron prequals
    intellicron_prequals['group'] = 'experiment'

    # Add intellicron identifier to prequals
    prequals_new = prequals.merge(intellicron_prequals, how='left', left_on='prequal_id', right_on='prequal_id',suffixes=('_left', '_right'))

    # Drop extra id columns
    prequals_new = prequals_new.drop(columns = ['Unnamed: 0_left','Unnamed: 0_right'])

    # Assign control label to non-intellicron records
    prequals_new.group.replace(to_replace = {np.NaN:'control'}, inplace = True)

    # Split data before and after intellicron ('2019-06-16')
    df = prequals_new[prequals_new.prequal_date >= '2019-06-16']

    return df

df = data_prep()

df.to_csv('intellicron_prequals_2.csv', index = False)

print('Fini!')
