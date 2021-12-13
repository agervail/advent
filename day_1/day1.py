import argparse

parser = argparse.ArgumentParser("Check if depth increase")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    lines = f.readlines()

radar_inputs = [int(x) for x in lines] 
nb_increased = 0
for i in range(1, len(radar_inputs)):
    if radar_inputs[i-1] < radar_inputs[i]:
        nb_increased += 1

print(nb_increased)


