import argparse

parser = argparse.ArgumentParser("Find the submarine location")
parser.add_argument('--filename', dest='filename', default='input')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    lines = f.readlines()

depth = 0
horizontal = 0

for command in lines:
    if 'forward' in command:
        horizontal += int(command.split(' ')[1])
    elif 'down' in command:
        depth += int(command.split(' ')[1])
    elif 'up' in command:
        depth -= int(command.split(' ')[1])

print('depth :', depth, 'horizontal :', horizontal) 
print('product :', depth * horizontal)
