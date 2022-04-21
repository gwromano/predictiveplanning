#Kyles ML model
# Initial imports
import tensorflow as tf
from tensorflow import keras
import os
import csv
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse


 # Loading a csv file from github and storing the path to a local instance
csv_path = tf.keras.utils.get_file(
    origin='https://github.com/kyleorman/PredPlanning/raw/main/toiletpaper.csv',
    fname = 'toiletpaper.csv',
    extract=False)
    
df = pd.read_csv(csv_path)
#df

#df.index = pd.to_datetime(df['Day'], format='%m-%d-%Y')
df.index = pd.to_datetime(df['Day'])

qnt = df['Quantity']
qnt.plot()
#qnt

# Function to plot predictions vs actuals for a model
def plot_predictions1(model, X, y, start=0, end=100):
  predictions = model.predict(X).flatten()
  df = pd.DataFrame(data={'Predictions':predictions, 'Actuals':y})
  plt.plot(df['Predictions'][start:end])
  plt.plot(df['Actuals'][start:end])
  plt.ylabel("Quantity")
  plt.xlabel("Index of Reserved Test Data")
  plt.legend(['Predictions', 'Actuals'])
  #plt.savefig("figure.jpg")
  ax = df.plot.line()
  ax.figure.savefig('panda-file.pdf')
  return df, mse(y, predictions)


# Mapping seconds (of arbitrary value) based on the timestamp
qnt_df = pd.DataFrame({'Quantity':qnt})
qnt_df['Seconds'] = qnt_df.index.map(pd.Timestamp.timestamp)
#qnt_df

day = 60*60*24
year = 365.2425*day

qnt_df['Year sin'] = np.sin(qnt_df['Seconds'] * (2 * np.pi / year))
qnt_df['Year cos'] = np.cos(qnt_df['Seconds'] * (2 * np.pi / year))
qnt_df.head()

qnt_df = qnt_df.drop('Seconds', axis=1)
qnt_df.head()

def df_to_X_y2(df, window_size=7):
  df_as_np = df.to_numpy()
  X = []
  y = []
  for i in range(len(df_as_np)-window_size):
    row = [r for r in df_as_np[i:i+window_size]]
    X.append(row)
    label = df_as_np[i+window_size][0]
    y.append(label)
  return np.array(X), np.array(y)

X2, y2 = df_to_X_y2(qnt_df)
X2.shape, y2.shape

# Added size of the train/val/test range to generalize based on number of items 
q_80 = int(len(qnt_df)*.80)
q_90 = int(len(qnt_df)*.90)

X2_train, y2_train = X2[:q_80], y2[:q_80]
X2_val, y2_val = X2[q_80:q_90], y2[q_80:q_90]
X2_test, y2_test = X2[q_90:], y2[q_90:]
X2_train.shape, y2_train.shape, X2_val.shape, y2_val.shape, X2_test.shape, y2_test.shape

qnt_training_mean = np.mean(X2_train[:, :, 0])
qnt_training_std = np.std(X2_train[:, :, 0])
                           
def preprocess(X):
  X[:, :, 0] = (X[:, :, 0] - qnt_training_mean) / qnt_training_std
  return X

preprocess(X2_train)
preprocess(X2_val)
preprocess(X2_test)

model3 = Sequential()
model3.add(InputLayer((7, 3)))
# Return sequences return the hidden state output for each input time step so
# the model is effectively passing through 2 GRU instances
model3.add(GRU(32,return_sequences=True))
model3.add(GRU(64))
model3.add(Dense(32, 'relu'))
model3.add(Dense(32, 'relu'))
model3.add(Dense(32, 'relu'))
model3.add(Dense(1, 'linear'))

model3.summary()

cp3 = ModelCheckpoint('model3/', save_best_only=True)
model3.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

model3.fit(X2_train, y2_train, validation_data=(X2_val, y2_val), epochs=1000, callbacks=[cp3])

plot_predictions1(model3, X2_test, y2_test)