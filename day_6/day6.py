import argparse
import numpy as np

parser = argparse.ArgumentParser("Find the submarine location")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

fishes = np.fromfile(args.filename, sep=',', dtype=int)
for i in range(80):
    zero_fishes = fishes == 0
    nb_zero_fishes = np.count_nonzero(zero_fishes)
    fishes -= 1
    fishes[zero_fishes] = 6
    fishes = np.append(fishes, np.full(nb_zero_fishes,8))

print(len(fishes))
