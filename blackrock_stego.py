#!/usr/bin/python3

import numpy as np
from PIL import Image


data = np.array(Image.open('imageEmbedded.png'))
data = data[...,0] # we'll only try the red plane to start
data2 = data
for i in range(len(data)):
    for j in range(len(data[0])):
        assert data2[i][j] == data[i][j]
        data2[i][j] = 255 if data[i][j] & 0b00000011 != 0 else 0
        # if the 2 last bits aren't 0, view as black
        # otherwise, white
        # note that 2 msb didn't return anything different

Image.fromarray(data2).save('extracted.png')