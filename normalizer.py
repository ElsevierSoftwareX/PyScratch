import csv


def normalize(entrada):
    pontos = []
    normalizado = []

    for a in range(len(entrada)):
        pontos.append(float(entrada[a]))

    for a in range(len(pontos)):
        normalizado.append((pontos[a] - min(pontos)) / (max(pontos) - min(pontos)))

    return normalizado

if __name__ == '__main__':
    with open("A1_03_1_1_Phase Contrast_2areas.csv", 'r') as entrada:
        reader = csv.reader(entrada, delimiter=',')
        dados = list(reader)
        dados.remove(dados[0])
        dados.remove(dados[0])
        dados.remove(dados[0])
        dados.remove(dados[0])
        dados.remove(dados[0])
        dados.remove(dados[0])
        #print(dados)
        normalize(dados)