import os

lr = 1e-3

savePath = 'savedModel'

os.makedirs(savePath, exist_ok=True)

seed = 0
numEpochs = 3
basePath = {
  'train': 'C:/Users\Dell\OneDrive\Documents\Quick Draw Game ML Internship\Machine Learning\GoogleDataImages_train',
  'test': 'C:/Users\Dell\OneDrive\Documents\Quick Draw Game ML Internship\Machine Learning\GoogleDataImages_test'
}
batchSize = {
  'train': 10,
  'test': 20
}

numWorkers = {
  'train': 2,
  'test': 2
}

iterations = {
  'train': 1000,
  'test': 100
}

resize = 32
