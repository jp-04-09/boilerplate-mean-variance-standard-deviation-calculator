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


    return calculations