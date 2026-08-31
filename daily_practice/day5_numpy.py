import numpy as np

number_floats = [1.5, 2.0, 3.2, 4.8]

floats_array = np.array(number_floats)

print(floats_array.dtype)
print(floats_array.shape)

doubled_array = floats_array*2
print(doubled_array)

# Double brackets build 2D rows: [[row1], [row2]]
more_numbers = [[1, 2, 3], [4, 5, 6]]

numbers_array = np.array(more_numbers)

print(numbers_array.shape)

print(np.sum(numbers_array, axis=0))
print(np.sum(numbers_array, axis=1))

mask = floats_array > 2.5
print(mask)
filter_floats = floats_array[mask]
print(filter_floats)

print(floats_array[1])

row_to_add = [10,20,30]

array_row = np.array(row_to_add)

broadcast_result = numbers_array + array_row
print(broadcast_result)
print(broadcast_result.shape)

scores = [70.0, 85.0, 90.0, 55.0, 100.0]
mean_score = np.mean(scores)

print(mean_score)

array_scores = np.array(scores)
array_meanscore = np.array(mean_score)

centered_scores = array_scores - array_meanscore

print(centered_scores)

import time

# Create a list and a numpy array with 1 million numbers
big_list = list(range(1_000_000))
big_array = np.array(big_list)

# 1. Standard Python For-Loop
start_time = time.time()
loop_result = [x * 2 for x in big_list]
loop_duration = time.time() - start_time

# 2. NumPy Vectorized Operation
start_time = time.time()
vector_result = big_array * 2
vector_duration = time.time() - start_time

print(f"Python Loop Time:     {loop_duration:.4f} seconds")
print(f"NumPy Vectorized Time: {vector_duration:.4f} seconds")