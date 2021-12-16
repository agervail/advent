import argparse
import numpy as np

parser = argparse.ArgumentParser("Find the submarine location")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    lines = f.readlines()

vents = []

for l in lines:
    sp = l.split()
    x1, y1 = [int(i) for i in sp[0].split(',')]
    x2, y2 = [int(i) for i in sp[2].split(',')]
    if x1 == x2 or y1 == y2:
        vents.append([(x1, y1), (x2, y2)])

vents_np = np.array(vents)
xmin, ymin = vents_np[:,:,0].min(), vents_np[:,:,1].min()
vents_np[:,:,0] = vents_np[:,:,0] - xmin
vents_np[:,:,1] = vents_np[:,:,1] - ymin

xmax, ymax = vents_np[:,:,0].max(), vents_np[:,:,1].max()
grid = np.zeros((xmax+1,ymax+1))


for v in vents_np:
    x1, y1, x2, y2 = v.flat
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2) 
        for i in range(min_y, max_y + 1):
            grid[x1][i] += 1
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2) 
        for i in range(min_x, max_x + 1):
            grid[i][y1] += 1

print('overlaps :', np.count_nonzero(grid > 1))
