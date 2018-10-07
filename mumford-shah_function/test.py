#!/usr/bin/env python
# coding=utf-8
import cv2
from MumfordShahMinimizer import *
#Use it on a grayscale image:
def gray(input):
    img = cv2.imread("image.jpg", 0)
    solver = MumfordShahMinimizer(img)
    img, edges = solver.minimize()
#on a color image:
def color(input):
    img = cv2.imread("image.jpg", 1)
    result, edges = [], []
    for c in cv2.split(img):
        solver = MumfordShahMinimizer(c, alpha = 1000, beta = 0.01, epsilon = 0.01)

        f, v = solver.minimize()
        result.append(f)
        edges.append(v)

    img = cv2.merge(result)
    edges = np.maximum(*edges)
if __name__=='__main__':
    color("image.jpg")
