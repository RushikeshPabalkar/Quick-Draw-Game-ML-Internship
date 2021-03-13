import os

basePath = 'C:/Users\Dell\OneDrive\Documents\Quick Draw ML Internship\Machine_Learning\GoogleDataImages_train'
lr = 1e-4

savePath = 'savedModel'

os.makedirs(savePath, exist_ok=True)

seed = 0
numEpochs = 20

batchSize = {
    'train': 10,
    'test': 20
}

numWorkers = {
    'train': 8,
    'test': 8
}

iterations = {
    'train': 1000,
    'test': 100
}
resize = 32
