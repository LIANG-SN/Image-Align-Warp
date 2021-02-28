import numpy as np
def warp(im, A, output_shape):
    """ Warps (h,w) image im using affine (3,3) matrix A
    producing (output_shape[0], output_shape[1]) output image
    with warped = A*input, where warped spans 1...output_size.
    Uses nearest neighbor interpolation."""
    output = np.zeros(output_shape)
    w = output_shape[0]
    h = output_shape[1]
    print(w, h)
    A_inv = np.linalg.inv(A)
    # to do: del for loop
    for i in range (0, h):
        for j in range (0, w):
            t = np.ones((3,1)) # use 3 x 1  or 1 x 3
            t[0] = j
            t[1] = i
            s = np.matmul(A_inv, t)
            sx = (int)(s[0])
            sy = (int)(s[1])
            if sx > 0 and sx < w - 1 and sy > 0 and sy < h - 1 :
                output[j, i] = im[sx, sy] 
    return output
