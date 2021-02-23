# coding=utf-8
# Importamos las librerías necesarias.
import argparse

import cv2  # OpenCV es la encargada de procesar las imágenes de la webcam.
import imutils  # Librería muy útil para redimensionar imágenes fácilmente, entre otras cosas.

# Definimos el menú del script:
# -c/--camera: Puerto de la cámara que queremos usar. Si sólo tienes una cámara, será el 0.
# -s/--size: Ancho de la ventana donde mostraremos las imágenes de la webcam. La altura se calculará automáticamente
#            para mantener la relación de aspecto.

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-c', '--camera', type=int, default=0,
                             help='Puerto al que está conectada la cámara (0-99).'
                                  'Por defecto es 0. Si sólo tienes una cámara,'
                                  'siempre debes usar 0.')
argument_parser.add_argument('-s', '--size', type=int, default=600, help='Ancho de la ventana donde veremos el stream'
                                                                         'de la cámara. (Mantiene la relación de '
                                                                         'aspecto con respecto al ancho).')
arguments = vars(argument_parser.parse_args())

# La variable camera, que es instancia de VideoCapture, nos permitirá procesar un recuadro a la vez.
camera = cv2.VideoCapture(arguments['camera'])

# Dado que la cámara nos proveerá fotogramas indefinidamente, tenemos que entrar en un ciclo infinito.
while True:
    # Leemos el fotograma actual. La variable 'grabbed' nos dice si la lectura fue exitosa o no, mientras
    # que 'frame' tiene el recuadro como tal.
    grabbed, frame = camera.read()

    # Si no pudimos obtener el fotograma, nos salimos del ciclo.
    if not grabbed:
        break

    # Redimensionamos el cuadro.
    frame = imutils.resize(frame, width=arguments['size'])

    # Mostramos el cuadro.
    cv2.imshow('Yo', frame)

    # Si el usuario presiona la tecla 'q', salimos del ciclo.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas.
camera.release()
cv2.destroyAllWindows()
