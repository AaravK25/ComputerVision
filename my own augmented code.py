import torch
import torchvision
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import numpy as np
import matplotlib.pyplot as plt

transforms = transforms.Compose ([
    
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(0.5),
    transforms.RandomRotation(23),
    transforms.ColorJitter(brightness=0.3, contrast=0.3),
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(0.5,))

])

datasetPath= "C:/Users/aarav/OneDrive/Desktop/TrashNet Dataset/trashnet-master"

dataset= datasets.ImageFolder(root= datasetPath, transform=transforms)

loader= DataLoader(dataset, batch_size=64, shuffle= True)

def augmented_batch(data):
    images, labels= data
    grid= torchvision.utils.make_grid(images, labels, nrow= 8)
    npimg= grid.numpy()
    plt.figure(figsize=(8,4))
    plt.imshow(np.transpose(npimg,(1,2,0)))
    plt.title("Augmented Batch")
    plt.axis(False)
    plt.show

for i,(images, labels) in enumerate(loader):
    print(f"Batch{i+1} with {len(images)} images")
    augmented_batch((images, labels))

    if i == 2:
        break




