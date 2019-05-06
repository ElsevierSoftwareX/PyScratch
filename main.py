import sys
import cv2
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from PySide.QtGui import *
from PySide.QtCore import *
#from PySide import QtCore
import find_quantity
import normalizer
import image_processing
from ui_files import mainDialog
import pandas as pd
import time
import copy


__appname__ = "PyScratch"
__version__ = "V2"
__cut__ = 2


class MySignal(QObject):
    imagemPronta = Signal(str)
    graficoPronto = Signal(str)
    tempo = Signal(float, float, int)
    terminado = Signal(str)


class GraphThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.tempo = 1000
        self.rodar = False
        self.dadosX = []
        self.dadosY = []
        self.signal = MySignal()

    def run(self):
        while self.rodar:
            plt.figure(figsize=(6.3, 4.35))
            plt.plot(self.dadosX, self.dadosY, 'ro', label='area', markersize=5)
            plt.xlabel('Time [min]')
            plt.ylabel('Area [pixels^2]')
            if len(self.dadosX) > 0:
                plt.axis([0, max(self.dadosX), 0, max(self.dadosY)])
            plt.legend(loc='best')
            plt.grid(color='black', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.savefig('plot' + '.png', format='png', bbox_inches='tight')
            plt.clf()
            plt.close()
            self.signal.graficoPronto.emit('OK')
            time.sleep(0.001 * self.tempo)


class WorkThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.signal = MySignal()
        self.tempo = 80
        self.formato = '.tif'
        self.quantidade = 0
        self.areaOut = 0
        self.tempoOut = 0
        self.corte = 0
        self.nome = ''
        self.path = ''
        self.encerrar = False
        self.tempo = 0

    def run(self):
        for c in range(self.quantidade):
            # if self.tamanho >= 1:
            if (c + 1) >= 100:
                area = (image_processing.process_a_picture(self.path, (self.nome + '' + str(c + 1)), self.formato,
                                                 self.corte))
                self.signal.tempo.emit(c * self.tempo, area, c)
            if (c + 1) >= 10 and c + 1 < 100:
                area = (image_processing.process_a_picture(self.path, (self.nome + '0' + str(c + 1)), self.formato,
                                                 self.corte))
                self.signal.tempo.emit(c * self.tempo, area, c)
            if (c + 1) < 10:
                area = (image_processing.process_a_picture(self.path, (self.nome + '00' + str(c + 1)), self.formato,
                                                 self.corte))
                self.signal.tempo.emit(c * self.tempo, area, c)

            if self.encerrar:
                break

            time.sleep(0.001 * self.tempo)

        self.signal.terminado.emit('OK')


class MainDialog(QDialog, mainDialog.Ui_Dialog):
    print("Loading PyScratch....")

    tempoVec = []
    areaVec = []
    normalizadoVec = []

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent, Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.setWindowTitle(__appname__ + ' - ' + __version__)

        self.graficoThread = GraphThread()
        self.graficoThread.signal.graficoPronto.connect(self.atualizaGrafico)
        self.analisarThread = WorkThread()
        self.analisarThread.signal.tempo.connect(self.gravarTempo)
        self.analisarThread.signal.terminado.connect(self.terminado)

        self.progressBar.setValue(0)
        self.arquivoLine.setEnabled(False)
        self.pararButton.setEnabled(False)
        self.analisarButton.setEnabled(False)
        self.salvarButton.setEnabled(False)

        self.arquivoButton.clicked.connect(self.carregar)
        self.salvarButton.clicked.connect(self.salvar)
        self.analisarButton.clicked.connect(self.analisar)
        self.sairButton.clicked.connect(self.close)
        self.pararButton.clicked.connect(self.encerrar)

        self.statusLabel.setText("Holding")
        self.statusLabel.setStyleSheet("QLabel#statusLabel {color: white; font: bold 12pt; " +
                                         "font-family: Tahoma;}")

    def encerrar(self):
        self.analisarThread.encerrar = True

    def terminado(self):
        self.statusLabel.setText("Finished")
        self.statusLabel.setStyleSheet("QLabel#statusLabel {color: yellow; font: bold 12pt; " +
                                         "font-family: Tahoma;}")
        self.normalizadoVec = normalizer.normalize(self.areaVec)
        self.graficoThread.rodar = False
        self.dados = pd.DataFrame()  # inicializa um dataframe do pandas
        self.dados['Time (min)'] = self.tempoVec
        self.dados['Area (pixel^2)'] = self.areaVec
        self.dados['Normalized '] = self.normalizadoVec
        self.progressBar.setValue(0)
        self.pararButton.setEnabled(False)
        self.salvarButton.setEnabled(True)

    def atualizaImagem(self):
        self.pixmap2 = QPixmap("image.png")
        self.pixmap3 = self.pixmap2.scaledToHeight(400)
        dimensao = self.pixmap3.size()
        self.imageLabel.setGeometry(QtCore.QRect(0, 60, dimensao.width(), dimensao.height()))
        self.imageLabel.setPixmap(self.pixmap3)

    def atualizaGrafico(self):
        self.pixmap = QPixmap("plot.png")
        dimensao = self.pixmap.size()
        self.graficoLabel.setGeometry(QtCore.QRect(560, 60, dimensao.width(), dimensao.height()))
        self.graficoLabel.setPixmap(self.pixmap)

    def gravarTempo(self, tempo, area, atual):
        self.tempoVec.append(tempo)
        self.graficoThread.dadosX = copy.deepcopy(self.tempoVec)
        self.areaVec.append(area)
        self.graficoThread.dadosY = copy.deepcopy(self.areaVec)
        self.atualizaImagem()
        self.progressBar.setValue(100*atual/self.analisarThread.quantidade)

    def analisar(self):
        del self.tempoVec[:]
        del self.areaVec[:]
        self.analisarThread.encerrar = False
        self.analisarThread.corte = float(__cut__)
        self.analisarThread.nome = self.inNome
        self.analisarThread.path = self.inDir
        self.analisarThread.tempo = float(self.tempoLine.text()[:len(self.tempoLine.text()) - 3])
        self.analisarThread.start()
        self.graficoThread.rodar = True
        self.graficoThread.start()
        self.statusLabel.setText("Processing...")
        self.statusLabel.setStyleSheet("QLabel#statusLabel {color: red; font: bold 12pt; " +
                                         "font-family: Tahoma;}")
        self.pararButton.setEnabled(True)

    def carregar(self):
        dir = "."
        self.inFile = QFileDialog.getOpenFileName(self, __appname__, dir=dir, filter="TIF image files (*.tif)")
        if self.inFile[0] != '':
            self.inNome = QtCore.QDir(self.inFile[0]).dirName()[:(len(QtCore.QDir(self.inFile[0]).dirName())-7)]
            self.inDir = QtCore.QDir(self.inFile[0]).path()[:(len(QtCore.QDir(self.inFile[0]).path())-len(QtCore.QDir(self.inFile[0]).dirName()))]
            self.arquivoLine.setText(self.inNome)
            self.analisarThread.quantidade = find_quantity.find(self.inDir + self.inNome, '.tif')
            self.quantidadeLabel.setText(str(self.analisarThread.quantidade))
            self.statusLabel.setText("Ready")
            self.statusLabel.setStyleSheet("QLabel#statusLabel {color: green; font: bold 12pt; " +
                                             "font-family: Tahoma;}")
            self.analisarButton.setEnabled(True)

    def salvar(self):
        dir = "."
        self.outFile = QFileDialog.getSaveFileName(self, __appname__, dir=dir, filter="CSV Files (*.csv)")

        if self.outFile[0] != '':
            self.dados.to_csv(self.outFile[0][:len(self.outFile[0])-4] + '_data.csv', sep='\t', index=False)
            im = cv2.imread('plot.png')
            cv2.imwrite(self.outFile[0][:len(self.outFile[0])-4]+'_plot.png', im)

    def closeEvent(self, event, *args, **kwargs):
        """Ritual de encerramento"""
        result = QMessageBox.question(self, __appname__, "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if result == QMessageBox.Yes:
            """Colocar aqui tudo que tiver que ser feito antes de sair"""
            self.graficoThread.rodar = False
            self.analisarThread.encerrar = True
            time.sleep(1)
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    QCoreApplication.setApplicationName(__appname__)
    QCoreApplication.setApplicationVersion(__version__)
    QCoreApplication.setOrganizationName("Vladimir Gaal")
    QCoreApplication.setOrganizationDomain("")

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()
