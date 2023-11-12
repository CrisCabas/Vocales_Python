import SeguimientoManos as sm
import cv2
import mediapipe as mp
import time
import math

cap = cv2.VideoCapture(0)
detector = sm.detectormanos(Confdeteccion=0.5)

while True:
        ret, image = cap.read()
        #Una vez que obtengamos la imagen la enviaremos
        image = detector.encontrarmanos(image)
        posmano, cuadro, nnum= detector.encontrarposicion(image)

        detector.dedosarriba()
        print(detector.vocal())
        #cv2.rectangle(image, (20,25), (85, 90), (0, 0, 0), cv2.FILLED)
        cv2.putText(image, "Vocal:", (20,250), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 100), 4)
        cv2.putText(image, detector.vocal(), (30,350), cv2.FONT_HERSHEY_PLAIN, 8, (0, 255, 100), 6)
        cv2.imshow("Manos", image)
        k = cv2.waitKey(1)

        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()