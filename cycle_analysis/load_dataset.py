import numpy as np
import pandas as pd
import sklearn.preprocessing 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import sklearn.model_selection 
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pickle

data = pd.read_csv("C:/Users/daniella/DC/cycle_analysis/FedCycleData071012 (2).csv")


# Create an empty DataFrame to store the filtered data
filtered_data = pd.DataFrame(columns=['ClientID', 'Cycle Length 1', 'Cycle Length 2', 'Cycle Length 3', 'Luteal Phase Length 1', 'Luteal Phase Length 2', 'Luteal Phase Length 3'])

# Create a dictionary to store aggregated information for each client ID
aggregated_data = {}

# Iterate through each row in the data DataFrame
for index, row in data.iterrows():
    client_id = row['ClientID']
    cycle_lengths = []
    luteal_lengths = []
    
    for i in range(1, 6):
        cycle_col = 'LengthofCycle'
        luteal_col = 'LengthofLutealPhase'
        
        cycle_length = row[cycle_col]
        luteal_length = row[luteal_col]
        
        if cycle_length != ' ' and luteal_length != ' ':
            cycle_lengths.append(int(cycle_length))
            luteal_lengths.append(int(luteal_length))
    
    if len(cycle_lengths) > 3 and len(luteal_lengths) > 3:
        if client_id not in aggregated_data:
            aggregated_data[client_id] = {
                'cycle_lengths': [],
                'luteal_lengths': []
            }
        aggregated_data[client_id]['cycle_lengths'].extend(cycle_lengths)
        aggregated_data[client_id]['luteal_lengths'].extend(luteal_lengths)

# Populate the filtered_data DataFrame from the aggregated_data dictionary
for client_id, lengths in aggregated_data.items():
    cycle_lengths = lengths['cycle_lengths']
    luteal_lengths = lengths['luteal_lengths']

    filtered_data = filtered_data._append([
        {
        'ClientID': client_id,
        'Cycle Length 1': cycle_lengths[0] if len(cycle_lengths) > 0 else None,
        'Cycle Length 2': cycle_lengths[1] if len(cycle_lengths) > 1 else None,
        'Cycle Length 3': cycle_lengths[2] if len(cycle_lengths) > 2 else None,
        'Cycle Length 4': cycle_lengths[3], 
        'Luteal Phase Length 1': luteal_lengths[0] if len(luteal_lengths) > 0 else None,
        'Luteal Phase Length 2': luteal_lengths[1] if len(luteal_lengths) > 1 else None,
        'Luteal Phase Length 3': luteal_lengths[2] if len(luteal_lengths) > 2 else None,
        'Luteal Phase Length 4': luteal_lengths[3] 
        }, 
    ], ignore_index=True)



target_data = []

# Iterate through each row in filtered_data dataframe
for index, row in filtered_data.iterrows():
    client_id = row['ClientID']
    last_cycle_length = row['Cycle Length 4']
    last_luteal_length = row['Luteal Phase Length 4']
    target_data.append([client_id, last_cycle_length, last_luteal_length])



# Create a new dataframe from the target_data list
target_data_columns = ['ClientID', 'Last Cycle Length', 'Last Luteal Phase Length']
target_data_df = pd.DataFrame(target_data, columns=target_data_columns)

'''
print("Target Data:")
print(target_data_df)
'''

filtered_data.drop(columns = ['Cycle Length 4', 'Luteal Phase Length 4'], inplace=True)

'''
print("Filtered Data:")
print(filtered_data)
'''

encoder = LabelEncoder()
filtered_data['ClientID'] = encoder.fit_transform(filtered_data['ClientID'])

encoded_client_ids = encoder.transform([item[0] for item in target_data])
for i, item in enumerate(target_data):
    item[0] = encoded_client_ids[i]


X = filtered_data.copy()
y = target_data.copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

y_train = np.array(y_train)[:, 1:].astype(float)
y_test = np.array(y_test)[:, 1:].astype(float)

print("Training Data:")
print(X_train)
print("Testing Data:")
print(X_test)
print("Training Target")
print(y_train)
print("Testing Target")
print(y_test)

linear_regressor = LinearRegression()

multi_output_regressor = MultiOutputRegressor(linear_regressor)


multi_output_regressor.fit(X_train, y_train)
predictions = multi_output_regressor.predict(X_test)

#Evalute the model's performance
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

#Calculate R-squared for each target variable
r2_cycle_length = r2_score(y_test[:, 0], predictions[:, 0])
r2_luteal_phase = r2_score(y_test[:, 1], predictions[:, 1])

print("R-squared for Cycle Length:", r2_cycle_length)
print("R-squared for Luteal Phase Length:", r2_luteal_phase)

with open('model.pkl', 'wb') as f:
    pickle.dump(multi_output_regressor, f)