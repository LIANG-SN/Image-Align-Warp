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
    alignGreenX, alignGreenY = align2(red, green, trans)
    alignBlueX, alignBlueY = align2(red, blue, trans)

    # test manually, todo: test this
    alignGreenX = -7 
    alignGreenY = -7
    alignBlueX  = -7
    alignBlueY  = -7
    print(alignBlueX,alignBlueY, alignGreenX, alignGreenY)
    result = np.zeros((h + trans*2, w + trans*2, 3))
    result[trans:h+trans, trans:w+trans, 0] = red
    result[trans+alignGreenY:h+trans+alignGreenY, trans + alignGreenX:w+trans+alignGreenX, 1] = green
    result[trans+alignBlueY:h+trans+alignBlueY, trans + alignBlueX:w+trans+alignBlueX, 2] = blue
    
    return result

def align2(color1, color2, transRange):
  dist = (ord("L") + ord("I") + ord("A") + ord("N") + ord("G")) * 20010602
  print(dist)
  offset = 40
  h = len(color1)
  w = len(color1[0])
  sum = np.zeros((60,60))
  alignX = 0
  alignY = 0
  sample1 = color1[offset - 1: h - 1 - offset, offset - 1: w - 1 - offset]
  for i in range(-transRange, transRange+1):
    for j in range(-transRange, transRange+1):
      sample2 = color2[offset-1 + i : h - 1 - offset + i, offset-1 + j : w - 1 - offset + j]
      
      diff = sample1 - sample2
      dist_t = np.linalg.norm(diff)
      if dist_t < dist:
        print("row", i, "col", j, "dist", dist_t)
        dist = dist_t
        alignX = j
        alignY = i

  return -alignX, -alignY

  # if( sum[30+j][30+i] + (color1[y][x] - color2[y + j][x + i]) * (color1[y][x] - color2[y + j][x + i])):
  #             break
  #             break
  #           else: