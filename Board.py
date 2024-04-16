# -*- coding: utf-8 -*-

import sys
import time
import matplotlib
import matplotlib.pyplot as plt
from GameManager import Turn, GameManager

matplotlib.use('QtAgg')
plt.ion()
matplotlib.interactive(True)    

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QDialog, QDialogButtonBox, QLabel)

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D    # @UnusedImport
from matplotlib.figure import Figure
import numpy as np

# class CustomDialog(QDialog):
#     def __init__(self, player):
#         super().__init__()

#         self.setWindowTitle("Game Over")

#         QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

#         self.buttonBox = QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)

#         self.layout = QVBoxLayout()
#         message = QLabel(f"{player.value} wins!")
#         self.layout.addWidget(message)
#         self.layout.addWidget(self.buttonBox)
#         self.setLayout(self.layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 859, 395))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pin33 = QPushButton(self.verticalLayoutWidget)
        self.pin33.setObjectName(u"pin33")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pin33.sizePolicy().hasHeightForWidth())
        self.pin33.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin33, 10, 5, 1, 1)

        self.pin01 = QPushButton(self.verticalLayoutWidget)
        self.pin01.setObjectName(u"pin01")
        sizePolicy2.setHeightForWidth(self.pin01.sizePolicy().hasHeightForWidth())
        self.pin01.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin01, 3, 2, 1, 1)

        self.pin03 = QPushButton(self.verticalLayoutWidget)
        self.pin03.setObjectName(u"pin03")
        sizePolicy2.setHeightForWidth(self.pin03.sizePolicy().hasHeightForWidth())
        self.pin03.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin03, 3, 5, 1, 1)

        self.pin00 = QPushButton(self.verticalLayoutWidget)
        self.pin00.setObjectName(u"pin00")
        sizePolicy2.setHeightForWidth(self.pin00.sizePolicy().hasHeightForWidth())
        self.pin00.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin00, 3, 0, 1, 1)

        self.pin32 = QPushButton(self.verticalLayoutWidget)
        self.pin32.setObjectName(u"pin32")
        sizePolicy2.setHeightForWidth(self.pin32.sizePolicy().hasHeightForWidth())
        self.pin32.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin32, 10, 4, 1, 1)

        self.pin23 = QPushButton(self.verticalLayoutWidget)
        self.pin23.setObjectName(u"pin23")
        sizePolicy2.setHeightForWidth(self.pin23.sizePolicy().hasHeightForWidth())
        self.pin23.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin23, 9, 5, 1, 1)

        self.pin21 = QPushButton(self.verticalLayoutWidget)
        self.pin21.setObjectName(u"pin21")
        sizePolicy2.setHeightForWidth(self.pin21.sizePolicy().hasHeightForWidth())
        self.pin21.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin21, 9, 2, 1, 1)

        self.pin10 = QPushButton(self.verticalLayoutWidget)
        self.pin10.setObjectName(u"pin10")
        sizePolicy2.setHeightForWidth(self.pin10.sizePolicy().hasHeightForWidth())
        self.pin10.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin10, 6, 0, 1, 1)

        self.pin20 = QPushButton(self.verticalLayoutWidget)
        self.pin20.setObjectName(u"pin20")
        sizePolicy2.setHeightForWidth(self.pin20.sizePolicy().hasHeightForWidth())
        self.pin20.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin20, 9, 0, 1, 1)

        self.pin30 = QPushButton(self.verticalLayoutWidget)
        self.pin30.setObjectName(u"pin30")
        sizePolicy2.setHeightForWidth(self.pin30.sizePolicy().hasHeightForWidth())
        self.pin30.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin30, 10, 0, 1, 1)

        self.pin02 = QPushButton(self.verticalLayoutWidget)
        self.pin02.setObjectName(u"pin02")
        sizePolicy2.setHeightForWidth(self.pin02.sizePolicy().hasHeightForWidth())
        self.pin02.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin02, 3, 4, 1, 1)

        self.pin11 = QPushButton(self.verticalLayoutWidget)
        self.pin11.setObjectName(u"pin11")
        sizePolicy2.setHeightForWidth(self.pin11.sizePolicy().hasHeightForWidth())
        self.pin11.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin11, 6, 2, 1, 1)

        self.pin22 = QPushButton(self.verticalLayoutWidget)
        self.pin22.setObjectName(u"pin22")
        sizePolicy2.setHeightForWidth(self.pin22.sizePolicy().hasHeightForWidth())
        self.pin22.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin22, 9, 4, 1, 1)

        self.pin31 = QPushButton(self.verticalLayoutWidget)
        self.pin31.setObjectName(u"pin31")
        sizePolicy2.setHeightForWidth(self.pin31.sizePolicy().hasHeightForWidth())
        self.pin31.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin31, 10, 2, 1, 1)

        self.pin13 = QPushButton(self.verticalLayoutWidget)
        self.pin13.setObjectName(u"pin13")
        sizePolicy2.setHeightForWidth(self.pin13.sizePolicy().hasHeightForWidth())
        self.pin13.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin13, 6, 5, 1, 1)

        self.pin12 = QPushButton(self.verticalLayoutWidget)
        self.pin12.setObjectName(u"pin12")
        sizePolicy2.setHeightForWidth(self.pin12.sizePolicy().hasHeightForWidth())
        self.pin12.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pin12, 6, 4, 1, 1)

        for x in range(4):
            for y in range(4):
                curr = eval(f"self.pin{y}{x}")
                curr.clicked.connect(self.generate_button_funcs(y,x))

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)
        self.move_button = QPushButton(self.verticalLayoutWidget)
        self.move_button.setText("Make Move")
        self.move_button.setDown(True)
        self.move_button.setEnabled(False)
        self.move_button.clicked.connect(self.start_button_clicked)
        self.verticalLayout.addWidget(self.move_button)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 955, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.player1_turn = True

        self.figure = Figure(facecolor=(0, 0, 0))
        self.ax = self.figure.add_subplot(projection='3d')

        self.selected_x = -1
        self.selected_y = -1
        self.curr_butt = None

        self.manager = GameManager()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pin33.setText(QCoreApplication.translate("MainWindow", u"[3,3]", None))
        self.pin01.setText(QCoreApplication.translate("MainWindow", u"[0,1]", None))
        self.pin03.setText(QCoreApplication.translate("MainWindow", u"[0,3]", None))
        self.pin00.setText(QCoreApplication.translate("MainWindow", u"[0,0]", None))
        self.pin32.setText(QCoreApplication.translate("MainWindow", u"[3,2]", None))
        self.pin23.setText(QCoreApplication.translate("MainWindow", u"[2,3]", None))
        self.pin21.setText(QCoreApplication.translate("MainWindow", u"[2,1]", None))
        self.pin10.setText(QCoreApplication.translate("MainWindow", u"[1,0]", None))
        self.pin20.setText(QCoreApplication.translate("MainWindow", u"[2,0]", None))
        self.pin30.setText(QCoreApplication.translate("MainWindow", u"[3,0]", None))
        self.pin02.setText(QCoreApplication.translate("MainWindow", u"[0,2]", None))
        self.pin11.setText(QCoreApplication.translate("MainWindow", u"[1,1]", None))
        self.pin22.setText(QCoreApplication.translate("MainWindow", u"[2,2]", None))
        self.pin31.setText(QCoreApplication.translate("MainWindow", u"[3,1]", None))
        self.pin13.setText(QCoreApplication.translate("MainWindow", u"[1,3]", None))
        self.pin12.setText(QCoreApplication.translate("MainWindow", u"[1,2]", None))
    # retranslateUi
        
    
    def draw_voxels(self):
        self.ax.clear()
        ncolors = self.manager.get_player1_moves()
        mcolors = self.manager.get_player2_moves()
        edgecolors = np.where(self.manager.get_full_board(), '#BFAB6E', '#00000000')
        facecolors = np.empty(self.manager.get_board_size(), dtype=object)
        facecolors[ncolors] = '#00D65DC0'
        if self.selected_x != -1:
            facecolors[self.selected_y, self.selected_x, self.manager.get_top_z(self.selected_y, self.selected_x)] = '#0000FFC0'
        facecolors[mcolors] = '#FF0000C0'
        facecolors[np.where(facecolors == None)] = '#00000000'
        filled = np.ones(self.manager.get_board_size(), dtype=object)

        # upscale the above voxel image, leaving gaps
        filled_2 = explode(filled)
        fcolors_2 = explode(facecolors)
        ecolors_2 = explode(edgecolors)
        # Shrink the gaps
        x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
        x[0::2, :, :] += 0.15
        y[:, 0::2, :] += 0.15
        z[:, :, 0::2] += 0.15
        x[1::2, :, :] += 0.85
        y[:, 1::2, :] += 0.85
        z[:, :, 1::2] += 0.85
        self.ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
        self.plotWidget.draw() 

    def start_button_clicked(self):
        y = self.selected_y
        x = self.selected_x
        self.manager.make_move(y,x)
        self.draw_voxels()
        # if self.manager.has_player_won():
            # dlg = CustomDialog(self.centralwidget, self.manager.player_turn)
            # dlg.exec()
        self.selected_x = -1
        self.selected_y = -1
        self.reset_all_buttons()
        self.manager.switch_turns()

    def generate_button_funcs(self, y, x):
        def button_clicked():
            self.selected_x = x
            self.selected_y = y
            curr_butt = eval(f"self.pin{y}{x}")
            if self.manager.is_top(y, x):
                return
            curr_butt.setEnabled(False)
            curr_butt.setDown(True)
            self.draw_voxels()
            if self.curr_butt is None:
                self.move_button.setDown(False)
                self.move_button.setEnabled(True)
            else:
                self.curr_butt.setEnabled(True)
                self.curr_butt.setDown(False)
            self.curr_butt = curr_butt

        return button_clicked

    def reset_all_buttons(self):
        self.curr_butt.setEnabled(True)
        self.curr_butt.setDown(False)
        self.curr_butt = None
        self.move_button.setDown(True)
        self.move_button.setEnabled(False)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # intialize the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # create the matplotlib widget and put it in the frame on the right
        self.ui.plotWidget = Mpwidget(self.ui.figure, parent=self.ui.frame)



def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e


class Mpwidget(FigureCanvas):
    def __init__(self, figure, parent=None):
        self.figure = figure
        super(Mpwidget, self).__init__(self.figure)
        self.setParent(parent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    window = mw
    mw.show()
    

    # adjust the frame size so that it fits right after the window is shown
    s = mw.ui.frame.size()
    mw.ui.plotWidget.setGeometry(0, 0, s.width(), s.height())


    sys.exit(app.exec())
