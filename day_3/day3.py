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

for b in non_zero:
    if b > nb_lines / 2:
        gamma = (gamma << 1) + 1
        epsilon = (epsilon << 1)
    else:
        gamma = (gamma << 1)
        epsilon = (epsilon << 1) + 1


print('gamma :', gamma, 'epsilon :', epsilon) 
print('product :', gamma * epsilon)
