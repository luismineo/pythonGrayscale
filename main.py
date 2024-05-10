import cv2
import numpy as np
import matplotlib.image as mpimg


def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
    # np.dot é usado para multiplicar matrizes
    # rgb[..., :3] pega os 3 primeiros valores de cada pixel da imagem
    # [0.2989, 0.5870, 0.1140] é a fórmula usada para converter a imagem para escala de cinza


img = mpimg.imread('landscape_m.png')
# mpimg.imread é usado para ler uma imagem e converte-lá para uma matriz

gray = grayscale(img)
# chama a função grayscale e passa a imagem como parâmetro

cv2.imshow('Grayscale Image', gray)
# cv2.imshow é usado para mostrar a imagem na tela
cv2.waitKey(0)
# cv2.waitKey(0) é usado para manter a janela ativa, até o usuário pressionar um botão
cv2.destroyAllWindows()
# cv2.destroyAllWindows() é usado para fechar a janela

