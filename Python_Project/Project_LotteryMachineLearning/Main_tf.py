'''
This project aims to apply machine learning algorithms to predict the next round of lottery in Korea.
First trial was using "sklearn DecisionTreeRegressor".
Second trial will be using "sklearn RandomForestRegressor".
Third trial will be using "Tensorflow neural network"

Korean Lottery
Numbers: 1 - 45

How it works:
1. There will be random selection of 6 numbers from 1 - 45
2. There are no overlapping numbers
3. There is additional bonus number

How to win:
1st: 6 numbers exactly(without the bonus number) match, the order of selection does not matter
2nd: 5 numbers exactly match + Bonus number match
3rd: 5 numbers exactly match
4th: 4 numbers exactly match
5th: 3 numbers exactly match

The random selection is done by VENUS DRAWING SYSTEM
'''

import tensorflow as tf
import pandas as pd
from tqdm import tqdm
import numpy as np


# Preparing data
current_path = "/Users/keonohkim/Desktop/Github_Portfolio/Python_Project/Project_LotteryMachineLearning/Data.csv"

data = pd.read_csv(current_path)

factor = ["Year", "Month", "Day", "Round", "Temperature", "RainAmout"]
target = ["Num1", "Num2", "Num3", "Num4", "Num5", "Num6"]

factor_data = data[factor]
target_data = data[target]


# Building a model
print("Model Building in Progress......")
In = tf.keras.layers.Input(shape=6)
H = tf.keras.layers.Dense(50, activation='swish')(In)
H = tf.keras.layers.Dense(60, activation='swish')(H)
H = tf.keras.layers.Dense(70, activation='swish')(H)
H = tf.keras.layers.Dense(80, activation='swish')(H)
H = tf.keras.layers.Dense(90, activation='swish')(H)
H = tf.keras.layers.Dense(100, activation='swish')(H)
H = tf.keras.layers.Dense(150, activation='swish')(H)
H = tf.keras.layers.Dense(250, activation='swish')(H)
H = tf.keras.layers.Dense(100, activation='swish')(H)
Out = tf.keras.layers.Dense(6)(H)

# Train a model
# epoch is the number of trainings
# Loss indicates the (prediction - actual)^2 which shows the error of the model so lower the better
tf_model = tf.keras.models.Model(In, Out)

tf_model.compile(loss='mse')

# Train a model
# epoch is the number of trainings
# Loss indicates the (prediction - actual)^2 which shows the error of the model so lower the better
# verbose=0 does not return current operation no printing


in_year = input("\n\n\nInput year: ")
in_month = input("\n\n\nInput month: ")
in_day = input("\n\n\nInput day: ")
in_round = input("\n\n\nInput round: ")
in_temp = input("\n\n\nInput temperature: ")
in_rain = input("\n\n\nInput rain: ")
interest = np.array([int(in_year), int(in_month), int(in_day), int(in_round), float(in_temp), float(in_rain)]).reshape(1, 6)

tf_model.fit(factor_data, target_data, epochs=1000)

result = tf_model.predict(interest)

print(f"The Prediction is following:\t{round(result[0, 0])}\t{round(result[0, 1])}\t{round(result[0, 2])}\t{round(result[0, 3])}\t{round(result[0, 4])}\t{round(result[0, 5])}")