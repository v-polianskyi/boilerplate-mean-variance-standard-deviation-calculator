import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  rows = np.array([list[:3],list[3:6],list[6:]])
  
  columns = np.array([
    [rows[0,0],rows[1,0],rows[2,0]],
    [rows[0,1],rows[1,1],rows[2,1]],      
    [rows[0,2],rows[1,2],rows[2,2]]
  ])
  
  mean = [
    [np.mean(columns[0]), np.mean(columns[1]), np.mean(columns[2])],
    [np.mean(rows[0]), np.mean(rows[1]), np.mean(rows[2])],
    np.mean(list)]

  var = [
    [np.var(columns[0]), np.var(columns[1]), np.var(columns[2])],
    [np.var(rows[0]), np.var(rows[1]), np.var(rows[2])],
    np.var(list)]

  std = [
    [np.std(columns[0]), np.std(columns[1]), np.std(columns[2])],
    [np.std(rows[0]), np.std(rows[1]), np.std(rows[2])],
    np.std(list)]

  max = [
    [np.max(columns[0]), np.max(columns[1]), np.max(columns[2])],
    [np.max(rows[0]), np.max(rows[1]), np.max(rows[2])],
    np.max(list)]

  min = [
    [np.min(columns[0]), np.min(columns[1]), np.min(columns[2])],
    [np.min(rows[0]), np.min(rows[1]), np.min(rows[2])],
    np.min(list)]

  sum = [
    [np.sum(columns[0]), np.sum(columns[1]), np.sum(columns[2])],
    [np.sum(rows[0]), np.sum(rows[1]), np.sum(rows[2])],
    np.sum(list)]
  
  calculations = {
    'mean': mean,
    'variance': var,
    'standard deviation': std,
    'max': max,
    'min': min,
    'sum': sum
  }
  
  return calculations
