import numpy as np
def calculate(list):
  if len(list) == 9:
    arr=np.array(list)
    matr=arr.reshape(3,3)
    calculations={
      'mean':[np.mean(matr,axis=0).tolist(),np.mean(matr,axis=1).tolist(),np.mean(arr)],
      'variance':[np.var(matr,axis=0).tolist(),np.var(matr,axis=1).tolist(),np.var(arr)],
      'standard deviation':[np.std(matr,axis=0).tolist(),np.std(matr,axis=1).tolist(),np.std(arr)],
      'max':[np.max(matr,axis=0).tolist(),np.max(matr,axis=1).tolist(),np.max(arr)],
      'min':[np.min(matr,axis=0).tolist(),np.min(matr,axis=1).tolist(),np.min(arr)],
      'sum':[np.sum(matr,axis=0).tolist(),np.sum(matr,axis=1).tolist(),np.sum(arr)]
    }
  else:
    raise ValueError('List must contain nine numbers.')
  return calculations