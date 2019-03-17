
def find(nome, formato):
    a = 0
    while True:
        if (a + 1) >= 100:
            try:
                fn = open(nome + '' + str(a + 1) + formato)
                fn.close()
            except FileNotFoundError:
                return a

        if (a + 1) >= 10 and (a + 1) < 100:
            try:
                fn = open(nome + '0' + str(a + 1) + formato)
                fn.close()
            except FileNotFoundError:
                return a

        if (a + 1) < 10:
            try:
                fn = open(nome + '00' + str(a + 1) + formato)
                fn.close()
            except FileNotFoundError:
                return a
        a = a+1


if __name__ == '__main__':
    nome = 'C2_03_1_1_Phase Contrast_'
    formato = '.tif'
    quantidade = find(nome, formato)
    print('quantidade: {}'.format(quantidade))
