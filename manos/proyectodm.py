# -*- coding: utf-8 -*-
"""Proyectodm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zA1bXNVn-_jbPCspk77-LkabWnLGXZII
"""

#!pip install mediapipe

# from google.colab import drive
#drive.mount('/content/drive')
#import os
#ruta_de_acceso = '/content/drive/MyDrive/Detector_de_manoss'
#os.chdir(ruta_de_acceso)
import SeguimientoManos as sm
import cv2
import mediapipe as mp
import time
import math

#from google.colab.patches import cv2_imshow
IMAGE_FILENAMES = ['e1.jpg']
DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480

def resize_and_show(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  #cv2.imshow('Imagen',img)
  #cv2.waitKey(0)


# Preview the images.
images = {name: cv2.imread(name) for name in IMAGE_FILENAMES}
for name, image in images.items():
 # print(name)
  resize_and_show(image)
#sm.main
# Detectamos la mano
detector = sm.detectormanos(Confdeteccion=0.5)

image = detector.encontrarmanos(image, dibujar=True)
#resize_and_show(image)

## Reconocimiento:
posmano, cuadro, nnum= detector.encontrarposicion(image, dibujar=False)
resize_and_show(image)
print(posmano)
detector.dedosarriba()
print(detector.vocal())

## Mostrar resultado
# Rectangulo
# cv2.rectangle(image, (20,25), (85, 90), (0, 0, 0), cv2.FILLED)
# Palabra vocal

cv2.putText(image, "Vocal:", (20,250), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 100), 4)
cv2.putText(image, detector.vocal(), (30,350), cv2.FONT_HERSHEY_PLAIN, 8, (0, 255, 100), 6)
resize_and_show(image)

# Lectura de la camara (no probado)
cap = cv2.VideoCapture(0)

while True:
  # Lectura de la videocaptura
  ret, image = cap.read()
 
  # Leemos teclado
  #t = cv2.waitKey(1)
  # Encontramos las manos
  image = detector.encontrarmanos(image, dibujar=False)
  
  # Posiciones mano 1
  posmano, cuadro, nnum= detector.encontrarposicion(image, dibujar=False)
  resize_and_show(image)
  detector.dedosarriba()
  detector.vocal()
  cv2.putText(image, "Vocal:", (20,250), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 100), 4)
  cv2.putText(image, detector.vocal(), (30,350), cv2.FONT_HERSHEY_PLAIN, 8, (0, 255, 100), 6)
  cv2.imshow("Manos", image)
  k = cv2.waitKey(1)
  if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


