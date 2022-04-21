import cv2
import matplotlib.pyplot as plt
import numpy as np


img= cv2.imread('Fotos/image.jpg')
lab=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

resized_merged = cv2.resize(lab, (1280, 720))
cv2.imshow('Imagen lab completo', resized_merged)

l, a, b = cv2.split(lab)
resized_l = cv2.resize(l, (1280, 720))
cv2.imshow('luminosidad', resized_l)
resized_a = cv2.resize(a, (1280, 720))
cv2.imshow('verde a magenta', resized_a)
resized_b = cv2.resize(b, (1280, 720))
cv2.imshow('azul a amarillo', resized_b)



cv2.waitKey(0)
