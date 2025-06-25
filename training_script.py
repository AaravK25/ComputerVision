import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import torchvision
import matplotlib.pyplot as plt




transforms = transforms.Compose ([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.3, contrast=0.3),
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(0.5,))
])

datasetsPath= "C:/Users/aarav/OneDrive/Desktop/TrashNet Dataset/trashnet-master"

datasets= datasets.ImageFolder(root= datasetsPath, transform=transforms)

loader = DataLoader(datasets, batch_size=8, shuffle=True)

def show_augmented_batch(loader):
    images, labels = next(iter(loader))
    grid= torchvision.utils.make_grid(images, nrow=4)
    nping= grid.numpy()