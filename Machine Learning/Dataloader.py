from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import os
import numpy as np
from PIL import Image

import Config


class dataloader(Dataset):
    splitType = ''

    def __init__(self):

        self.allClasses = sorted(os.listdir(Config.basePath))

        self.allData = {}

        for imgClass in self.allClasses:
            self.allData[imgClass] = []
            imgPath = sorted(os.listdir(Config.basePath + '/' + imgClass + '/image/'))
            for image in imgPath:
                image = self.process(Config.basePath + '/' + imgClass + '/image/' + image)
                self.allData[imgClass].append(image)

    def process(self, path):

        # image = Image.fromarray(plt.imread(path)[:, :, 3])
        # image = Image.open(path).convert('RGB')
        # print(image.size)
        image = Image.open(path)
        arr = np.asarray(image)
        image = Image.fromarray(arr[:, :, 3])
        image = image.resize((32, 32))
        image = (np.array(image) > 0.1).astype(np.float32)[None, :, :]
        transforms.RandomHorizontalFlip()
        transforms.RandomRotation(20)
        # image = image.resize((128, 128))
        # print(type(image))
        # image = (np.array(image) > 0.1).astype(np.float32)[None, :, :]
        # print(type(image))
        # image.show()
        # print(np.shape(image), type(image))

        return image

    def __getitem__(self, item):

        classID = np.random.randint(len(self.allData))
        className = self.allClasses[classID]
        image_id = np.random.randint(len(self.allData[className]))
        image = self.allData[className][image_id]
        # print('image=', type(image), image.shape)

        return image, classID

    def __len__(self):
        return Config.iterations[self.splitType]


def _worker_init_fn(worker_id):
    np.random.seed(worker_id)


def getDataLoader(type_='train'):
    dataloader.splitType = type_

    return DataLoader(
        dataloader(),
        batch_size=Config.batchSize[type_],
        num_workers=Config.numWorkers[type_],
        worker_init_fn=_worker_init_fn
    )
