import argparse
import numpy as np
parser = argparse.ArgumentParser()

parser.add_argument('--grid', type=str)
parser.add_argument('--value_policy', type=str)
args = parser.parse_args()

gridfile = open(args.grid, 'r')
vpfile = open(args.value_policy, 'r')

data = gridfile.readlines()
maze = [[] for x in data]
i = 0
for words in data:
    maze[i] = words.split()
    i += 1

data = vpfile.readlines()
policy = [0 for x in data]
i = 0
for words in data:
    words = words.split()
    policy[i] = float(words[1])
    i += 1

maze = np.array(maze)
y_size, x_size = np.shape(maze)
end = []
for i in range(y_size):
    for j in range(x_size):
        if maze[i][j] == '2':
            start = (i, j)
        if maze[i][j] == '3':
            end.append((i, j))
i, j = start
while True:
    if (i, j) in end:
        break
    else:
        move = policy[i*x_size+j]
        if move == 0:
            print('West', end='\n')
            j = j-1
        elif move == 1:
            print('North', end='\n')
            i = i-1
        elif move == 2:
            print('East', end='\n')
            j = j+1
        elif move == 3:
            print('South', end='\n')
            i = i+1
