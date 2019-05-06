import cv2
from matplotlib import pyplot as plt
import numpy


def treatment(im, corte, mostrar=False):

    ponto = 1
    ponto2 = 25

    if mostrar:
        cv2.imshow('image original', im)
        k = cv2.waitKey(0)

    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(imgray, cv2.CV_8UC1)
    if mostrar:
        cv2.imshow('laplacian', laplacian)
        k = cv2.waitKey(0)

    saida = cv2.GaussianBlur(laplacian, (ponto, ponto), cv2.BORDER_REFLECT101)
    if mostrar:
        cv2.imshow('G Blur', saida)
        k = cv2.waitKey(0)

    saida2 = cv2.GaussianBlur(saida, (ponto2, ponto2), cv2.BORDER_DEFAULT)
    if mostrar:
        cv2.imshow('GBlur2', laplacian)
        k = cv2.waitKey(0)

    ret, thresh = cv2.threshold(saida2, corte, 255, cv2.THRESH_BINARY_INV)
    if mostrar:
        cv2.imshow('thresh', thresh)
        k = cv2.waitKey(0)

    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if mostrar:
        cv2.destroyAllWindows()

    return contours


if __name__ == '__main__':
    corte = 2
    path = "D:\\GDrive\\Fer\\170804_174239_Plate 1 - Copy\\"
    nome = 'A1_03_1_1_Phase Contrast_001'
    formato = '.tif'
    im = cv2.imread(path + nome + formato)
    contours = treatment(im, corte, mostrar=True)
    areas = range(len(contours))
    cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
    cv2.imshow('image', im)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()
    areas = []
    plt.figure(figsize=(15, 5))
    for c in range(len(contours)):
        areas.append(cv2.contourArea(contours[c]))
    counts, bins = numpy.histogram(areas, bins=100, range=(min(areas), max(areas)))
    plt.hist(areas)
    plt.show()
