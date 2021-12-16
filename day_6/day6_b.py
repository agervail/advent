import argparse
import numpy as np
import copy

parser = argparse.ArgumentParser("Find the submarine location")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

fishes_raw = np.fromfile(args.filename, sep=',', dtype=int)


fishes = [0] * 9
for fish in fishes_raw:
    fishes[fish] += 1

for i in range(256):
    old_fishes = copy.deepcopy(fishes)
    for f in range(1, 9):
        fishes[f-1] = old_fishes[f]
    fishes[6] += old_fishes[0]
    fishes[8] = old_fishes[0]

print(sum(fishes))
