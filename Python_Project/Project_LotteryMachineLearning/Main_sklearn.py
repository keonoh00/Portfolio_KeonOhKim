'''
This project aims to apply machine learning algorithms to predict the next round of lottery in Korea.
First trial was using "sklearn DecisionTreeRegressor".
This trial will be using "sklearn RandomForestRegressor".

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





from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from tqdm import tqdm
import csv
import numpy as np

error_dict = {}

# Always check the file path before run
current_path = "/Users/keonohkim/Desktop/Github_Portfolio/Python_Project/Project_LotteryMachineLearning/Data.csv"

data = pd.read_csv(current_path)
# Rain Amount Typo
factor = ["Year", "Month", "Day", "Round", "Temperature", "RainAmout"]
target = ["Num1", "Num2", "Num3", "Num4", "Num5", "Num6"]

X = data[factor]
y = data[target]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# From below the max leaf node with lowest error was 2
'''
for_node = []
for node in tqdm(range(2, 100)):
    model_1 = DecisionTreeRegressor(max_leaf_nodes=node, random_state=1)
    model_1.fit(train_X, train_y)
    prediction = model_1.predict(val_X)
    for_node.append([node, mean_absolute_error(val_y, prediction)])

with open('errorDecistion.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(for_node)
'''
Deci = DecisionTreeRegressor(max_leaf_nodes=2, random_state=1)
Deci.fit(train_X, train_y)
DeciPrediction = Deci.predict(val_X)
DeciError = mean_absolute_error(val_y, DeciPrediction)
error_dict["Decistion Tree with max node = 2"] = DeciError

print("\n\nError of DecisionTreeRegressor:  {}".format(DeciError))


Deci_default = DecisionTreeRegressor(random_state=1)
Deci_default.fit(train_X, train_y)
DeciPrediction_default = Deci_default.predict(val_X)
DeciError_default = mean_absolute_error(val_y, DeciPrediction_default )
print("\n\nError of DecisionTreeRegressor with default max_leaf_nodes:  {}".format(DeciError_default))
error_dict["Decistion Tree with default max node"] = DeciError_default


# Used to check the rough range of optimal max node
'''
check_node = []
for node in tqdm(range(2, 10000, 100)):
    model_2 = RandomForestRegressor(max_leaf_nodes=node ,random_state=1)
    model_2.fit(train_X, train_y)
    prediction = model_2.predict(val_X)
    check_node.append([node, mean_absolute_error(val_y, prediction)])

with open('error600.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(check_node)
'''


# From narrowed range finding the best node
# From below code, end at max_leaf_nodes = 2 has lowest mae
'''
opt_node = {}
for leaf in tqdm(range(2, 600)):
    model = RandomForestRegressor(max_leaf_nodes=leaf, random_state=1)
    model.fit(train_X, train_y)
    prediction = model.predict(val_X)
    opt_node[leaf] = mean_absolute_error(val_y, prediction)

best_node = min(opt_node, key=opt_node.get)
print(best_node)
'''

Rand = RandomForestRegressor(max_leaf_nodes=2, random_state=1)
Rand.fit(train_X, train_y)
RandPrediction = Rand.predict(val_X)
RandError = mean_absolute_error(val_y, RandPrediction)
error_dict["Random Forest with max node = 2"] = RandError



print("\n\nError of RandomForestRegressor:  {}".format(RandError))

Rand_default = RandomForestRegressor(random_state=1)
Rand_default.fit(train_X, train_y)
RandPrediction_default = Rand_default.predict(val_X)
RandError_default = mean_absolute_error(val_y, RandPrediction_default)
error_dict["Random Forest with default max node"] = RandError_default


print("\n\nError of RandomForestRegressor with default max_leaf_nodes:  {}".format(RandError_default))

best_prediction = min(error_dict, key=error_dict.get)

print("\n\n\nTherefore best prediction model is {}\n\n\n".format(best_prediction))

in_year = input("Input year: ")
in_month = input("Input month: ")
in_day = input("Input day: ")
in_round = input("Input round: ")
in_temp = input("Input temperature: ")
in_rain = input("Input rain: ")
interest = np.array([in_year, in_month, in_day, in_round, in_temp, in_rain]).reshape(1, -1)

if best_prediction == 'Decistion Tree with max node = 2':
    result = Deci.predict(interest)
elif best_prediction == 'Decistion Tree with default max node':
    result = Deci_default.predict(interest)
elif best_prediction == 'Random Forest with default max node':
    result = Rand_default.predict(interest)
else:
    result = Rand.predict(interest)

print("The Prediction is following:\n{}\n{}\n{}\n{}\n{}\n{}".format(result[0, 0], result[0, 1], result[0, 2], result[0, 3], result[0, 4], result[0, 5]))