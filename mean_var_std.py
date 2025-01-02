import numpy as np

def calculate(list):

    if (len(list) < 9):
        raise ValueError("List must contain nine numbers.")

    myArr = np.array(list)
    myArr = myArr.reshape(3,3)

    mean_column = [myArr[:,0:1].mean(), myArr[:,1:2].mean(), myArr[:,2:3].mean()]
    mean_row = [myArr[0:1,:].mean(), myArr[1:2,:].mean(), myArr[2:3,:].mean()]
    mean_flattened = myArr.mean()

    var_column = [myArr[:,0:1].var(), myArr[:,1:2].var(), myArr[:,2:3].var()]
    var_row = [myArr[0:1,:].var(), myArr[1:2,:].var(), myArr[2:3,:].var()]
    var_flattened = myArr.var()

    std_column = [myArr[:,0:1].std(), myArr[:,1:2].std(), myArr[:,2:3].std()]
    std_row = [myArr[0:1,:].std(), myArr[1:2,:].std(), myArr[2:3,:].std()]
    std_flattened = myArr.std()

    max_column = [myArr[:,0:1].max(), myArr[:,1:2].max(), myArr[:,2:3].max()]
    max_row = [myArr[0:1,:].max(), myArr[1:2,:].max(), myArr[2:3,:].max()]
    max_flattened = myArr.max()

    min_column = [myArr[:,0:1].min(), myArr[:,1:2].min(), myArr[:,2:3].min()]
    min_row = [myArr[0:1,:].min(), myArr[1:2,:].min(), myArr[2:3,:].min()]
    min_flattened = myArr.min()

    sum_column = [myArr[:,0:1].sum(), myArr[:,1:2].sum(), myArr[:,2:3].sum()]
    sum_row = [myArr[0:1,:].sum(), myArr[1:2,:].sum(), myArr[2:3,:].sum()]
    sum_flattened = myArr.sum()

    calculations = {
        'mean' : [mean_column, mean_row, mean_flattened],
        'variance' : [var_column, var_row, var_flattened],
        'standard deviation' : [std_column, std_row, std_flattened],
        'max' : [max_column, max_row, max_flattened],
        'min' : [min_column, min_row, min_flattened],
        'sum' : [sum_column, sum_row, sum_flattened]
    }

    return calculations