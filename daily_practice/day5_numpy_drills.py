import numpy as np

number_list = [10, 20, 30, 40, 50]
array_list = np.array(number_list)
print(array_list.mean())

number_list2 = [[1,2,3],[4,5,6]]
array_numbers2 = np.array(number_list2)
print(array_numbers2.mean(axis=0))

print(array_numbers2.mean(axis=1))

arr = np.array([5, 15, 25, 35, 45])
print(arr > 20)
print(arr[arr>20])
print()
print(len(arr[arr > 20]))
print()
print("Section 2")

arr2 = np.array([2, 4, 4, 4, 5, 5, 7, 9])
mean_arr2 = np.mean(arr2)
std_arr2 = np.std(arr2)
print((arr2- mean_arr2)/std_arr2)

arr3 = np.arange(1, 13)
print(arr3.reshape(3,4))

print(arr3.reshape(4,3))
print()
print("Section 3")
print()
matrix = np.array([[1,2],[3,4],[5,6]])
print(matrix)
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))

result0 = matrix.sum(axis=0)
result1 = matrix.sum(axis=1)

print(result0, result0.shape)
print(result1, result1.shape)

prices = np.array([100, 105, 98, 110, 95])
pct_change = (prices[1:] - prices[:-1]) / prices[:-1]
print(pct_change)
