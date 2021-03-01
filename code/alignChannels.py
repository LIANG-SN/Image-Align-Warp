import numpy as np

def alignChannels(red, green, blue):
    """Given 3 images corresponding to different channels of a color image,
    compute the best aligned result with minimum abberations

    Args:
      red, green, blue - each is a HxW(H: height, W: width) matrix corresponding to an HxW image

    Returns:
      rgb_output - HxWx3 color image output, aligned as desired"""
    trans = 30
    h = len(red)
    w = len(red[0])
    alignGreenX, alignGreenY = align2_new(red, green, trans)
    alignBlueX, alignBlueY = align2_new(red, blue, trans)
    result = np.zeros((h + trans*2, w + trans*2, 3))
    result[trans:h+trans, trans:w+trans, 0] = red
    result[trans+alignGreenY:h+trans+alignGreenY, trans + alignGreenX:w+trans+alignGreenX, 1] = green
    result[trans+alignBlueY:h+trans+alignBlueY, trans + alignBlueX:w+trans+alignBlueX, 2] = blue
    
    return result

def align2_new(color1, color2, transRange):
  dist = (ord("L") + ord("I") + ord("A") + ord("N") + ord("G")) * 20010602
  h = len(color1)
  w = len(color1[0])
  alignX = 0
  alignY = 0
  sample1 = np.ones((h + transRange * 2, w + transRange * 2))
  sample1 *= (256)
  sample1[transRange  : transRange + h, transRange  : transRange  + w] = color1
  for i in range(-transRange, transRange):
    for j in range(-transRange, transRange):
      sample2 = np.ones((h + transRange * 2, w + transRange * 2))
      sample2 *= (256)
      sample2[transRange + i : transRange + i + h, transRange  + j : transRange + j + w] = color2
      diff = sample1 - sample2
      dist_t = np.linalg.norm(diff)
      if dist_t < dist:
        dist = dist_t
        alignX = j
        alignY = i

  return alignX, alignY