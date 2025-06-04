import numpy as np
import pandas as pd
import torch

def mytranspose(x):
    if isinstance(x, np.ndarray):
        if x.ndim == 1:
            return x.reshape(-1, 1)
        elif x.ndim == 2:
            return np.transpose(x)
        else:
            raise ValueError("Unsupported array shape")
    elif isinstance(x, pd.DataFrame):
        return x.transpose()
    elif isinstance(x, torch.Tensor):
        return x.T
    else:
        raise TypeError("Unsupported data type for transpose")
