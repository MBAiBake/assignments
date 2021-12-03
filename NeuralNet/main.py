import numpy as np
from neural import NeuralNet
import csv
from csv import reader
import pandas as pd
from numpy import asarray
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

xor_data = [
    #   input     output    corresponding example
    ([0.0, 0.0],  [0.0]),  #[0, 0] => 0
    ([0.0, 1.0],  [1.0]),  #[0, 1] => 1
    ([1.0, 0.0],  [1.0]),  #[1, 1] => 1
    ([1.0, 1.0],  [0.0])   #[1, 0] => 0
]

nn = NeuralNet(2,5,1)
nn.train(xor_data,0.5,0.1,1000,100)

for i in nn.test_with_expected(xor_data):
    print(f"desired: {i[1]}, actual: {i[2]}")

#Wine Data Analysis
nwine = pd.read_csv("wine.data",header=None,dtype=None)
nwinedf = pd.DataFrame(nwine)
print(nwinedf)

sclr = MinMaxScaler()
new_df = sclr.fit_transform(nwinedf[[0,1,2,3,4,5,6,7,8,9,10,11,12,13]])

final_df = pd.DataFrame(new_df)
print(final_df)

input_dat = []
for i in final_df.index:
    input_dat.append(([final_df[1][i],
                       final_df[2][i],
                       final_df[3][i],
                       final_df[4][i],
                       final_df[5][i],
                       final_df[6][i],
                       final_df[7][i],
                       final_df[8][i],
                       final_df[9][i],
                       final_df[10][i],
                       final_df[11][i],
                       final_df[12][i],
                       final_df[13][i]],
                      [final_df[0][i]]))

print(input_dat)

nn2 = NeuralNet(13,5,1)
nn2.train(input_dat,0.5,0.1,10000,1000)

for i in nn2.test_with_expected(input_dat):
    print(f"desired: {i[1]}, actual: {i[2]}")