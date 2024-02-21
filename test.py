import cv2
import numpy as np
import pyautogui


def main():
    # Cargar las imágenes de entrada y reemplazo
    input_image = cv2.imread('input_image.png', cv2.IMREAD_UNCHANGED)
    replacement_image = cv2.imread(
        'replacement_image.png', cv2.IMREAD_UNCHANGED)

    while True:
        # Capturar la pantalla
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        # Convertir la captura de pantalla a formato BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Intentar encontrar la imagen de entrada en la captura de pantalla
        result = cv2.matchTemplate(frame, input_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Si la coincidencia es lo suficientemente alta, reemplazar la imagen en la captura de pantalla
        threshold = 0.8
        if max_val > threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + input_image.shape[1],
                            top_left[1] + input_image.shape[0])
            frame[top_left[1]:bottom_right[1], top_left[0]
                :bottom_right[0]] = replacement_image

        # Mostrar la captura de pantalla con las imágenes reemplazadas
        cv2.imshow('Replacement', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
