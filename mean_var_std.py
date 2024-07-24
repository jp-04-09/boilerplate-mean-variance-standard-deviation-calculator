import numpy as np

def calculate(list):

    my_array = np.array(list)
    # printing the array
    print("The array is : " + str(my_array))
    # Checking lenght and the type of the elements of the array
    list_size = my_array.size
    list_type = my_array.dtype
    if list_size == 9 and np.issubdtype(my_array.dtype, np.number):
        print("the array lenght is: " + str(list_size))
        print("All elements of the array are numbers")
    else:
        raise ValueError("List must contain nine numbers.")
        
    keys_array = np.array(["mean", "variance", "standard deviation", "max", "min", "sum"])
    
    # Calculate statistics for flattened matrix
    mean_flattened_matrix = np.mean(my_array)
    variance_flattened_matrix = np.var(my_array)
    std_dev_flattened_matrix = np.std(my_array)
    max_flattened_matrix = np.max(my_array)
    min_flattened_matrix = np.min(my_array)
    sum_flattened_matrix = np.sum(my_array)

    values_flattened_matrix = np.array([mean_flattened_matrix, variance_flattened_matrix, std_dev_flattened_matrix, max_flattened_matrix, min_flattened_matrix, sum_flattened_matrix])
    
    # Calculate statistics for 3x3 matrix (reshape initial array)
    # axis = 0 column, axis = 1 row
    my_matrix = np.reshape(my_array, (3, 3))
    mean_matrix_col = np.mean(my_matrix, axis = 0)
    mean_matrix_row = np.mean(my_matrix, axis = 1)
    variance_matrix_col = np.var(my_matrix, axis = 0)
    variance_matrix_row = np.var(my_matrix, axis = 1)
    std_dev_matrix_col = np.std(my_matrix, axis = 0)
    std_dev_matrix_row = np.std(my_matrix, axis = 1)
    max_matrix_col = np.max(my_matrix, axis = 0)
    max_matrix_row = np.max(my_matrix, axis = 1)
    min_matrix_col = np.min(my_matrix, axis = 0)
    min_matrix_row = np.min(my_matrix, axis = 1)
    sum_matrix_col = np.sum(my_matrix, axis = 0)
    sum_matrix_row = np.sum(my_matrix, axis = 1)

    # Create the result dictionary
    calculations = {
        'mean': [mean_matrix_col.tolist(), mean_matrix_row.tolist(), mean_flattened_matrix],
        'variance': [variance_matrix_col.tolist(), variance_matrix_row.tolist(), variance_flattened_matrix],
        'standard deviation': [std_dev_matrix_col.tolist(), std_dev_matrix_row.tolist(), std_dev_flattened_matrix],
        'max': [max_matrix_col.tolist(), max_matrix_row.tolist(), max_flattened_matrix],
        'min': [min_matrix_col.tolist(), min_matrix_row.tolist(), min_flattened_matrix],
        'sum': [sum_matrix_col.tolist(), sum_matrix_row.tolist(), sum_flattened_matrix]
    }

    return calculations
