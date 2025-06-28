import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import torchvision
import numpy as np
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

loader = DataLoader(datasets, batch_size=64, shuffle=True)

def show_augmented_batch(data):
    images, labels = data
    grid = torchvision.utils.make_grid(images, nrow=8)
    npimg = grid.numpy()
    plt.figure(figsize=(8, 4))
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.title("Augmented Batch")
    plt.axis('off')
    plt.show()

for i, (images, labels) in enumerate(loader):
    print(f"Batch {i+1} with {len(images)} images")
    show_augmented_batch((images, labels))
    
    if i == 2:  # Stop after 3 batches
        break
