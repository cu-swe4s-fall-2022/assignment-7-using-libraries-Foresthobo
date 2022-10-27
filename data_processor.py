# remember to import your libraries!
import numpy as np
import pandas as pd


def get_random_matrix(num_rows, num_columns):
    if (num_rows or num_columns) == 0:
        return None
    else:
        return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name, sep=',', head=None):
    try:
        data = pd.read_csv(file_name, sep, header=head)
    except pd.errors.EmptyDataError:
        return (0,)
    return np.shape(data)


def write_matrix_to_file(num_rows, num_columns, file_name):
    data = get_random_matrix(num_rows, num_columns)
    np.savetxt(file_name, data, delimiter=',')
    return file_name
