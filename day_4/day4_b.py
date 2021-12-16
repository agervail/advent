import argparse
import numpy as np

parser = argparse.ArgumentParser("Find the submarine location")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    lines = f.readlines()

num_drawns = [int(x) for x in lines[0].split(',')]

grids = []

def read_one_grid(grid_text):
    grid = []
    for l, vals in enumerate(grid_text):
        grid.append([int(x) for x in vals.split()])
    return grid

end_of_grids = False
nb_grids = 0 
while(not end_of_grids):
    current_index = nb_grids * 6 + 2
    if current_index >= len(lines):
        break
    grids.append(read_one_grid(lines[current_index : current_index + 5]))
    nb_grids += 1

check_grid = np.zeros((len(grids),5,5))
grids = np.asarray(grids)
nb_grids_range = range(grids.shape[0])
old_winner_grids = 0
winner_grids = 0

for num in num_drawns:
    check_grid[grids == num] = 1
    good_line = np.nonzero(check_grid.all(axis=2))
    good_col = np.nonzero(check_grid.all(axis=1))
    old_winner_grids = winner_grids
    winner_grids = np.isin(nb_grids_range, good_line[0]) + np.isin(nb_grids_range, good_col[0])
    if(np.all(winner_grids)):
        last_to_win = np.where(old_winner_grids == False)
        break
        
non_zero_tot = grids[last_to_win][(check_grid[last_to_win] == 0).nonzero()].sum()
print('non_zero_tot :', non_zero_tot, 'product :', non_zero_tot * num)
        

