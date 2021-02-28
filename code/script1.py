from alignChannels import alignChannels
import numpy as np
# Problem 1: Image Alignment

# 1. Load images (all 3 channels)
# load as H * W matrix
red = np.load('../data/red.npy')
green = np.load('../data/green.npy')
blue = np.load('../data/blue.npy')

# test
print("width:", len(blue[0]))
print("height:", len(blue))
# 2. Find best alignment
rgbResult = alignChannels(red, green, blue) / 256.0

# 3. save result to rgb_output.jpg (IN THE "results" FOLDER)
import matplotlib.pyplot as plot
h = len(red)
w = len(red[0])
raw = np.zeros((h, w, 3))
raw[:, :, 0] = red[:, :]
raw[:, :, 1] = green[:, :]
raw[:, :, 2] = blue[:, :]
raw[:, :, :] /= 256.0
plot.imsave('../results/raw.jpg', raw)
plot.imsave('../results/rgb_output.jpg', rgbResult)