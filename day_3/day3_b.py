import argparse
import numpy as np

parser = argparse.ArgumentParser("Find the submarine location")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    lines = f.readlines()

gamma = 0
epsilon = 0

diag_raw = []
for diag_line in lines:
    diag_raw.append([])
    for diag_bit in diag_line:
        if diag_bit != '\n':
            diag_raw[-1].append(int(diag_bit))

diag_mx = np.asarray(diag_raw)
non_zero = np.count_nonzero(diag_mx, axis=0)
nb_lines = diag_mx.shape[0]

oxygen = diag_mx.copy()
co2 = diag_mx.copy()

for col in range(diag_mx.shape[1]):
    if oxygen.shape[0] > 1:
        non_zero_oxygen = np.count_nonzero(oxygen, axis=0)[col]
        if non_zero_oxygen >= oxygen.shape[0] / 2:
            mask = (oxygen[:, col] == 1)
        else:
            mask = (oxygen[:, col] == 0)
        oxygen = oxygen[mask, :]
    if co2.shape[0] > 1:
        non_zero_co2 = np.count_nonzero(co2, axis=0)[col]
        if non_zero_co2 < co2.shape[0] / 2:
            mask = (co2[:, col] == 1)
        else:
            mask = (co2[:, col] == 0)
        co2 = co2[mask, :]
    if co2.shape[0] <= 1 and oxygen.shape[0] <= 1:
        break

oxygen_int = 0
co2_int = 0
for oxygen_bit in oxygen[0]:
    oxygen_int = (oxygen_int << 1) + oxygen_bit
for co2_bit in co2[0]:
    co2_int = (co2_int << 1) + co2_bit

print('oxygen :', oxygen_int, 'co2 :', co2_int) 
print('product :', oxygen_int * co2_int)
