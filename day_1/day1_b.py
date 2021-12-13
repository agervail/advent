import argparse

parser = argparse.ArgumentParser("Check if depth increase")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    lines = f.readlines()

radar_inputs = [int(x) for x in lines] 
nb_increased = 0

for i in range(3, len(radar_inputs)):
    previous_sum = radar_inputs[i-1] + radar_inputs[i-2] + radar_inputs[i-3]
    current_sum = radar_inputs[i] + radar_inputs[i-1] + radar_inputs[i-2]
    if previous_sum < current_sum:
        nb_increased += 1

print(nb_increased)


