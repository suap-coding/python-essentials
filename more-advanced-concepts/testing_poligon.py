import gc
import numpy as np
import numba as nb

# @nb.njit
def quartiles_r(dataset):
    dataset.sort()
    if dataset.size == 0:
        return None
    if dataset.size == 1:
        return dataset
    else:
        ds_length = dataset.size
        if ds_length%2:
            mean = dataset[ds_length//2]
        else:
            mean = (dataset[ds_length//2] + dataset[ds_length//2 - 1])/2

        i = 0
        while dataset[i] <= mean:
            i += 1
        
    return i, quartiles_r(dataset[dataset.size/2]) # , quartiles_r(dataset[i:])

    # , quartiles_r([number for number in dataset if number <= mean])[0], quartiles_r([number for number in dataset if number > mean])[0]
# def quartiles_r(dataset):
#     dataset.sort()
#     if len(dataset) == 0:
#         return None
#     if len(dataset) == 1:
#         return dataset
#     else:
#         ds_length = len(dataset)        
#         if ds_length%2:
#             mean = dataset[ds_length//2]
#         else:
#             mean = (dataset[ds_length//2] + dataset[ds_length//2 - 1])/2
#     # return mean, quartiles_r([number for number in dataset if number <= mean])[0], quartiles_r([number for number in dataset if number > mean])[0]

our_data = np.array([1])
# our_data.sort()
print(quartiles_r(our_data))
print(quartiles_r(np.array([1,2,3,4,5])))
print(quartiles_r(np.array([1,7,8,2,3,6,9,4,5,10,1,2,1,4,5])))

