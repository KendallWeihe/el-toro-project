import csv
import pdb
import numpy as np
import time

def measure_csv_package(csv_file):
    time0 = time.time()

    data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            data.append(row)

    time1 = time.time()

    return time1 - time0, data

def measure_numpy_package(csv_file):
    time0 = time.time()
    data = np.genfromtxt(csv_file, delimiter=",")
    time1 = time.time()
    return time1 - time0, data

f = "./Kentucky_Louisville_161221.csv"
csv_time, csv_data = measure_csv_package(f)
np_time, np_data = measure_numpy_package(f)

print("Performance results:")
print("CSV package time: " + str(csv_time))
print("NumPy package time: " + str(np_time))
print("NumPy / CSV ratio: " + str(np_time / csv_time))
