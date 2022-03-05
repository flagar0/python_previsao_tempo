from PyQt5 import uic, QtWidgets, QtCore, QtGui
import operator
from rest_api import *
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import tempfile
import os
import textwrap
import sys
import os


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def botao(cid):
    clima = Tempo(cid)

    # Pega imagem para clima atual
    url_img = requests.get(
        gera_img(clima.data['condition_code'], clima.data['currently']))
    nuven = Image.open(BytesIO(url_img.content))
    # Cria Arquivo temporario para  imagem
    temp = tempfile.NamedTemporaryFile(prefix='wheater_')
    nuven.save(temp.name+".png")
    window.img.setPixmap(QtGui.QPixmap(temp.name+".png"))
    temp.close()
    os.remove(temp.name+".png")

    # Seta caracteristica  do tempo
    carac = textwrap.fill(text=clima.data['description'], width=12)
    window.lbl_carac.setText(carac)

    # Seta temperatura e cidade
    temperatura = str(clima.data['temp'])+"°"
    window.lbl_temp.setText(temperatura)
    window.lbl_city.setText(clima.data['city'])

    # Seta humidade
    humi = str(clima.data['humidity'])+"%"
    window.lbl_humi.setText(humi)

    # Seta Max e Min
    max = str(clima.data['forecast'][0]['max'])+"°"
    min = str(clima.data['forecast'][0]['min'])+"°"
    window.lbl_max.setText(max)
    window.lbl_min.setText(min)

    window.frame.show()


def botao_sp():
    botao("455827")


def botao_rj():
    botao("455825")


def botao_rc():
    botao("455824")


app = QtWidgets.QApplication([])
window = uic.loadUi(resource_path("windows/janela.ui"))
window.frame.hide()
window.bt_sp.clicked.connect(botao_sp)
window.bt_rj.clicked.connect(botao_rj)
window.bt_rc.clicked.connect(botao_rc)

window.show()
app.exec()
