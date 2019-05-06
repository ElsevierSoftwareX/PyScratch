import numpy as np
import cv2
import process_contours as proc
import datetime
import os

sufixo_de_saida = '_resultado'
now = datetime.datetime.now()
font = cv2.FONT_HERSHEY_PLAIN
verde = (0, 255, 0)
vermelho = (0, 0, 255)
preto = (0, 0, 0)
azul = (255, 0, 0)
branco = (255, 255, 255)


def process_a_picture(path, nome, formato, corte):
    # carregando imagem
    im = cv2.imread(path + nome + formato)
    contours = proc.treatment(im, corte)
    height, width, channels = im.shape
    tamanho = height * width

    maior_area = 0
    maior_area_index = []

    continua = True
    while continua:
        for c in range(len(contours)):
            if cv2.contourArea(contours[c]) >= tamanho:
                maior_area = maior_area + (cv2.contourArea(contours[c]))
                maior_area_index.append(int(c))

        if len(maior_area_index) > 0:
            # desenhando na figura
            for a in range(len(maior_area_index)):
                cv2.drawContours(im, contours, maior_area_index[a], verde, 2)
                cv2.putText(im, '{}'.format(maior_area_index[a]), (int(contours[maior_area_index[a]][0][0][0]) - 50,
                                                                   int(contours[maior_area_index[a]][0][0][1]) + 25),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, vermelho, 2, cv2.LINE_AA)
                cv2.putText(im, 'File: {}{}'.format(nome, formato), (2, 32), cv2.FONT_HERSHEY_PLAIN, 1.5, preto, 1,
                            cv2.LINE_AA)
                cv2.putText(im, 'File: {}{}'.format(nome, formato), (0, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, verde, 1,
                            cv2.LINE_AA)
                cv2.putText(im, 'Area: {}pixels'.format(maior_area), (2, 62), cv2.FONT_HERSHEY_PLAIN, 1.5, preto, 1,
                            cv2.LINE_AA)
                cv2.putText(im, 'Area: {}pixels'.format(maior_area), (0, 60), cv2.FONT_HERSHEY_PLAIN, 1.5, verde, 1,
                            cv2.LINE_AA)
                cv2.putText(im, 'Date: {}/{}/{}'.format(now.day, now.month, now.year), (2, 92), cv2.FONT_HERSHEY_PLAIN,
                            1.5,
                            preto, 1, cv2.LINE_AA)
                cv2.putText(im, 'Date: {}/{}/{}'.format(now.day, now.month, now.year), (0, 90), cv2.FONT_HERSHEY_PLAIN,
                            1.5,
                            verde, 1, cv2.LINE_AA)
                rect = cv2.minAreaRect(contours[maior_area_index[a]])
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(im, [box], 0, vermelho, 2)
            continua = False
        else:
            tamanho = tamanho - tamanho*0.05

        if tamanho < 2:
            maior_area = 0
            maior_area_index.append(0)
            continua = False

    cv2.imwrite('image.png', im)

    # Salvando imagem de saida
    path = path + '/Output'
    if not os.path.isdir(path):
        os.makedirs(path)
    filename = os.path.join(path, nome + '.tif')
    cv2.imwrite(filename, im)

    return maior_area


if __name__ == '__main__':
    # inicialização de variáveis
    path = 'C:/Users/SVE 1713 Z/Google Drive/Fer/170825_175542_Plate 1/'
    nome = 'A1_03_1_1_Phase Contrast_023'
    formato = '.tif'
    tamanho = 1048576
    corte = 2
    process_a_picture(path, nome, formato, corte)
