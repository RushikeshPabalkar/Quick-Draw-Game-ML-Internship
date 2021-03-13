from torch.utils.data import Dataset, DataLoader, dataloader
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import Config


class dataLoader(Dataset):

    def __init__(self):

      self.allClasses = sorted(os.listdir(Config.basePath))

      self.allData = {}
      for classI in self.allClasses:
          self.allData[classI] = []
          imagePath = sorted(os.listdir(Config.basePath + '/' + classI + '/' '/image/'))
          for image in imagePath:
              image = self.process(Config.basePath + '/' + classI + '/image/' + image)
              self.allData[classI].append(image)

    def process(self, path):
        image = Image.fromarray(plt.imread(path)[:, :, 3])
        image = image.resize(Config.resize_image, Config.resize_image)
        image = (np.array(image) > 0.1).astype(np.float32)[None, :, :]
        return image

    def __getitem__(self, item):

        classID = np.random.randint(len(self.allData))
        className = self.allClasses[classID]
        image_id = np.random(len(self.allData[className]))
        image = self.allData[className][image_id]

        return image, classID

    def __len(self):

        return Config.iterations[self.type]

    def _worker_init_fn(worker_id):

        np.random.seed(worker_id)

    def getDataLoader(type_='train'):

        return DataLoader(
            dataloader(),
            batch_size=Config.batchSize[type_],
            num_worker=Config.numWorkers[type_],
            worker_init_fn=_worker_init_fn

        )
