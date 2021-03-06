import RiskParser as rp
import os
import sys
model_path = os.path.abspath( os.path.join('..', 'ComponentModels') )
sys.path.append(model_path)
from ANN import ANN
from Dtree import Dtree
from KNN import KNN
from LogR import LogR
from NaiveEnsemble import NaiveEnsemble
from helper import *
import numpy as np

in_file = "../Data/broward_norm.csv"
inputs, outputs = rp.parse_data(in_file, 5, 9, 11) #'output' is COMPAS's guess...not 'reality'
or_list = get_OR(inputs, outputs)
for i in range(len(or_list)):
    print(or_list[i])
data_dists, min_dist, max_dist, avg_dist = get_distances(inputs)
i = 0
MIN_CUTOFF = 2.0
while(i < len(data_dists) and data_dists[i][0] <= MIN_CUTOFF):
    # print(data_dists[i])
    i += 1
print("Min:", min_dist, "\tMax:", max_dist, "\tMean:", avg_dist, "\tMedian:", (data_dists[len(data_dists)//2])[0] )
print( "N below cutoff:", i, "out of", len(data_dists), " ({:6.4f})".format(i/len(data_dists)) )

#outlier finding
# q1 = np.percentile(inputs, 25, axis = 0)
# q3 = np.percentile(inputs, 75, axis = 0)
# IQR = np.subtract(q3, q1)
# diff = np.multiply(IQR, 1.5)
#
# lows =  np.add(q1, -diff)
# highs = np.add(q3,  diff)
# print(lows)
# print(highs)
