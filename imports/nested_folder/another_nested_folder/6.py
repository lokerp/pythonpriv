import os

with open(os.path.join('data', 'dataIMT.txt'), 'r') as input_file:
    lines = input_file.readlines()
height_strings = lines[2::3]
heights = list(map(float, height_strings))
max_height = max(heights)
min_height = min(heights)
avg_height = sum(heights) / len(heights)
print(f'Максимальный рост: {max_height}, минимальный: {min_height}, средний: {avg_height}')