import os

basePath = 'C:\Users\Dell\OneDrive\Documents\Quick Draw ML Internship\Machine_Learning\data'
lr = 1e-4

savePath = 'savedModel'

os.makedirs(savePath, exist_ok=True)

seed = 0

numEpochs = 2

batchSize = {
  'train': 20,
  'test': 40
}

numWorkers = {
  'train': 2,
  'test': 2
}

iterations = {
  'train': 1000,
  'test': 100
}

resize_image = 128
