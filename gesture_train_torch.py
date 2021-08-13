import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import os

datadir = 'data'
data_transforms = {
    'train': transforms.Compose([
        #transforms.ToPILImage(),
        transforms.Resize((64, 64)),
        transforms.Grayscale(num_output_channels=1),
        transforms.ToTensor()
    ]),
    'test': transforms.Compose([
        #transforms.ToPILImage(),
        transforms.Resize((64, 64)),
        transforms.Grayscale(num_output_channels=1),
        transforms.ToTensor()
    ]),
}

image_datasets = {x : datasets.ImageFolder(os.path.join(datadir, x), data_transforms[x]) for x in ['train', 'test']}
#print(image_datasets)
dataloaders = {x : torch.utils.data.DataLoader(image_datasets[x], batch_size=4, shuffle=True) for x in ['train', 'test']}
#print(dataloaders)
dataset_sizes = {x:len(image_datasets[x]) for x in ['train', 'test']}
#print(dataset_sizes)
class_names = image_datasets['train'].classes
#print(class_names)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def imshow(inp, title):
    inp = inp.numpy().transpose((1, 2, 0))
    plt.imshow(inp)
    plt.title(title)
    plt.show()

inputs, classes = next(iter(dataloaders['train']))
# Make a grid from batch
out = torchvision.utils.make_grid(inputs)

#imshow(out, title=[class_names[x] for x in classes])

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 32, 5)
        self.conv3 = nn.Conv2d(32, 32, 3)
        self.fc1 = nn.Linear(32*1*1, 128)
        self.fc2 = nn.Linear(128, 7)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 32*1*1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x

'''
conv1 = nn.Conv2d(1, 32, 5)
pool = nn.MaxPool2d(2, 2)
conv2 = nn.Conv2d(32, 32, 5)
conv3 = nn.Conv2d(32, 32, 3)
print(inputs.shape)
x = conv1(inputs)
print(x.shape)
x = pool(x)
print(x.shape)
x = conv2(x)
x = pool(x)
x = conv3(x)
x = pool(x)
x = conv3(x)
x = pool(x)
print(x.shape)'''

model = CNN().to(device)

learning_rate = 0.001
epochs = 2
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

print("Training Start")

for epoch in range(epochs):
    print('Epoch {}/{}'.format(epoch, epochs - 1))
    print('-' * 10)
    for phase in ['train', 'test']:
        print(phase)
        if phase == 'train':
            model.train()
        else:
            model.eval()

        running_loss = 0
        running_corrects = 0

        for images,labels in dataloaders[phase]:
            images = images.to(device)
            labels = labels.to(device)

            with torch.set_grad_enabled(phase == 'train'):
                outputs = model(images)
                loss = criterion(outputs, labels)
                _, preds = torch.max(outputs, 1)
                if phase == 'train':
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

            running_loss += loss.item()
            running_corrects += torch.sum(preds == labels.data)

        epoch_loss = running_loss / dataset_sizes[phase]
        epoch_acc = running_corrects.double() / dataset_sizes[phase]

        print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

print('Finished Training')

def make_pred(images, labels):
    #images, labels = next(iter(data))
    images = images.to(device)
    labels = labels.to(device)
    with torch.no_grad():
        logps = model(images)
        _, preds = torch.max(logps, 1)
    #print(labels, preds)
    return preds
preds = make_pred(inputs, classes)
imshow(out, title=(classes, preds))
