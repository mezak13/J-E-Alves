import random
from PyQt5 import uic,QtWidgets



def rodar():
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
    33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

    random.shuffle(numeros)

    tela.label.setText(str(numeros[0]))
    tela.label_2.setText(str(numeros[2]))    
    tela.label_3.setText(str(numeros[3]))
    tela.label_4.setText(str(numeros[4]))
    tela.label_5.setText(str(numeros[5]))
    tela.label_6.setText(str(numeros[6]))
    tela.label_7.setText(str(numeros[7]))
    tela.label_8.setText(str(numeros[8]))
    tela.label_9.setText(str(numeros[9]))
    tela.label_10.setText(str(numeros[10]))
    tela.label_11.setText(str(numeros[11]))
    tela.label_12.setText(str(numeros[12]))
    tela.label_13.setText(str(numeros[13]))
    tela.label_14.setText(str(numeros[14]))
    tela.label_15.setText(str(numeros[15]))
    
    
   
    
app=QtWidgets.QApplication([])
tela=uic.loadUi("Quina.ui")
tela.pushButton.clicked.connect(rodar)

tela.show()
app.exec()