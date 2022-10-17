import numpy as np

def calculate(list):
  if (len(list) < 9):
      raise ValueError('List must contain nine numbers.')
  list = np.reshape(list, (3, 3))
  
  def newListMean(num):
    return list.mean(axis= num).tolist()
  
  def newListVar(num):
    return list.var(axis = num).tolist()
    
  def newListStd(num):
    return list.std(axis = num).tolist()
    
  def newListMax(num):
    return list.max(axis = num).tolist()
    
  def newListMin(num):
    return list.min(axis = num).tolist()
    
  def newListSum(num):
    return list.sum(axis = num).tolist()
  
  calculations = {
      'mean': [newListMean(0), newListMean(1), list.mean()],
      'variance': [newListVar(0), newListVar(1), list.var()],
      'standard deviation': [newListStd(0), newListStd(1), list.std()],
      'max': [newListMax(0), newListMax(1), list.max()],
      'min': [newListMin(0), newListMin(1), list.min()],
      'sum': [newListSum(0), newListSum(1), list.sum()] 
    }  
  return calculations